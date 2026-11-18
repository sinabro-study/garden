# 05. JDBC Batch와 flush·clear

## 기술 개념 전체 설명

### Batch의 목적

여러 SQL을 묶어 드라이버·DB 왕복 비용을 줄인다. JDBC batch가 하나의 SQL이 되는 것은 아니다. 실행 결과·부분 실패 처리는 드라이버와 트랜잭션 설정을 확인한다.

### JPA와 식별자

IDENTITY는 INSERT 후 DB가 생성한 키를 받아야 하므로 JPA가 INSERT를 지연·묶기 어렵다. 이력 INSERT를 JdbcTemplate batch로 처리했다면 키가 필요한지와 순서 보장을 확인해야 한다.

### flush·clear

flush는 변경 SQL을 DB에 보내지만 commit은 아니다. clear는 관리 Entity를 분리하므로 미반영 변경이 유실될 수 있다. 대량 작업은 적절한 단위마다 flush 후 clear하고 실패 시 전체 롤백 경계를 확인한다.

## 흐름 그림

```mermaid
flowchart LR
 N0["Entity 변경"]
 N1["flush"]
 N0 --> N1
 N2["JDBC batch 이력 INSERT"]
 N1 --> N2
 N3["commit<br/>clear는 flush 이후"]
 N2 --> N3
```

## 이력서·포트폴리오 사례 연결

669개 상품 요청에서 반복 DB 호출을 줄였다는 주장과 평균 쿼리 2,571→34의 측정 단위를 확인한다. 수량과 이력의 원자성도 검증한다.

## Level 1~5 문제

### Level 1 · 정의

JDBC batch와 단일 bulk SQL은 어떻게 다른가?

### Level 2 · 내부 동작

IDENTITY가 JPA batching을 어렵게 하는 이유는?

### Level 3 · 장애·한계

clear 전 flush를 빠뜨리면 어떤 일이 생기나?

### Level 4 · 대안과 Trade-off

JPA batch, JdbcTemplate, bulk UPDATE의 Trade-off는?

### Level 5 · 실제 적용과 검증

669개 상품 재현·쿼리 계수·부분 실패 롤백·정합성 대사를 설명하라.

## 학습 기록

- 상태: 미응시
- 무자료 2분 답변:
- 틀린 개념:
- 확인한 실제 근거:
- 아직 미확인인 주장:
- 다음 복습일:
