# UUID를 CHAR(36)보다 BINARY(16)으로 먼저 검토하는 이유

## 같은 UUID를 문자와 바이트로 저장하기

UUID는 본래 128비트이며 **16바이트**다.  
`CHAR(36)`은 하이픈 네 개를 포함한 사람이 읽는 문자열 표현을 저장한다.  
`BINARY(16)`은 16바이트 값을 그대로 저장한다.

```text
문자열:  018f5b72-90ab-7cde-8f12-34567890abcd   → 36개 문자
바이너리: 0x018F5B7290AB7CDE8F1234567890ABCD   → 16바이트
```

`CHAR(36)`이 **항상 디스크에서 정확히 36바이트**라는 뜻은 아니다.  
문자 집합과 InnoDB 행 형식에 따라 실제 저장량이 달라진다.

그래도 UUID가 ASCII 문자로만 표현된다는 점을 고려하면 바이너리 16바이트가 보통 더 짧은 키를 만든다.  
MySQL은 긴 PK가 모든 보조 인덱스에 포함되므로 공간·I/O 부담이 늘어난다고 설명한다. [MySQL: 저장 레이아웃](https://dev.mysql.com/doc/refman/8.4/en/optimizing-innodb-storage-layout.html), [MySQL: 인덱스 종류](https://dev.mysql.com/doc/refman/8.4/en/innodb-index-types.html)

## 왜 먼저 검토하나?

1. **클러스터드 PK 크기:** 같은 128비트 값을 더 짧게 보관할 수 있다.
2. **보조 인덱스 크기:** InnoDB는 각 보조 인덱스 레코드에 PK를 넣으므로 PK 축소 효과가 반복된다.
3. **비교 규칙:** 바이너리 값은 문자 collation의 대소문자·문자 비교 규칙을 고려할 필요가 없다.
4. **버퍼 풀 효율:** 같은 메모리 공간에 더 많은 인덱스 엔트리가 들어갈 가능성이 있다.  
   실제 성능은 데이터와 워크로드로 확인한다.

## 변환과 정렬 순서가 중요하다

MySQL에서는 `UUID_TO_BIN(uuid_string)`과 `BIN_TO_UUID(binary_value)`로 표현을 변환할 수 있다.  
`UUID_TO_BIN(..., 1)`의 `swap_flag`는 특정 시간 필드를 재배열하는 기능이다.

UUIDv7은 이미 앞부분에 시간순 필드가 있으므로 **v7에 `swap_flag=1`을 습관적으로 적용하지 않는다.**  
앱 생성기와 DB 변환의 바이트 순서를 비교한다.  
UUID를 저장했다가 읽어 원래 값과 일치하는지 확인한다.

`ORDER BY id`가 기대한 정렬을 만드는지도 확인한다. [MySQL: UUID_TO_BIN/BIN_TO_UUID](https://dev.mysql.com/doc/refman/8.4/en/miscellaneous-functions.html), [RFC 9562 §6.11](https://www.rfc-editor.org/rfc/rfc9562.html)

```mermaid
flowchart LR
 A[애플리케이션 UUIDv7] --> B[16바이트 순서 확인]
 B --> C[DB BINARY 16 저장]
 C --> D[다시 UUID로 변환]
 D --> E[원본 값·정렬 순서 대조]
```

## 비용과 대안

`BINARY(16)`은 SQL 콘솔에서 바로 읽기 어렵다.  
또 JDBC/JPA 타입 매핑과 기존 문자열 API의 변환 계층이 필요하다.

운영자가 직접 조회할 때는 `BIN_TO_UUID()` 같은 변환을 쓴다.  
`CHAR(36)`은 디버깅과 외부 연동이 편하지만 PK·보조 인덱스가 커질 수 있다.

UUID를 외부 식별자로만 쓰고 내부 PK를 짧은 정수로 두는 설계도 가능하다.  
어느 쪽이 빠른지는 실제 쿼리·쓰기 비중·보조 인덱스 수로 판단한다.

## Level 1~5 면접 문제

1. UUID가 16바이트인데 문자열은 왜 36문자인가?
2. InnoDB 보조 인덱스에 PK가 포함되면 저장 타입 선택이 왜 중요해지는가?
3. 문자 집합·collation·바이트 순서에서 어떤 문제가 생길 수 있는가?
4. `BINARY(16)`과 `CHAR(36)` 및 정수 PK와 UUID UNIQUE를 조합한 설계의 Trade-off는?
5. 실제 스키마에서 저장 크기·성능·변환 round-trip을 어떻게 검증하겠는가?
