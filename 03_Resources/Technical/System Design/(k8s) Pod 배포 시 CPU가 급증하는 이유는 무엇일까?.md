
![[Screenshot 2026-02-22 at 6.49.48 AM.png]]

트래픽이 없는 상태에서 재배포시 CPU spike 현상을 확인할 수 있다.
이유는 무엇일까? CPU는 계산 + 명령 실행하는 기계이다.
JVM 환경에서 배포 시 단계 별 프로세스가 필요하다.
각 프로세스 별 CPU 사용하는 구간을 확인할 필요가 있다.

1. 클래스 로딩 
2. bytecode verification  
3. JIT 컴파일 (C1 → C2)  
4. hotspot profiling


### 클래스 로딩
- JVM이 .class 파일을 메모리 구조로 바꾸는 작업

(1) 파일 읽기 + 파싱
```
.class binary -> JVM internal structure

= binary parsing
= constant pool 해석
= symbol resolution
```


(2) 메타데이터 생성
- Reflection으로 Annotation Scanning을 하기 때문에 CPU 사용량이 증가
	- 문자열 parsing + hashing + lookup 과정을 거쳐야하기 때문

```
Method Table
Field Table
Annotation Metadata
Reflection Info
```

### Bytecode Verification
- JVM 보안 + 안정성 체크 단계

(1) 타입 체크
```
int -> String 캐스팅 시도

= 스택 상태 시뮬레이션
코드 실행하면 스택 상태가 어떻게 변하는지 가상으로 실행
컴파일러 수준의 정적 분석 작업
```

### JIT 컴파일
- bytecode -> interpreter 실행 느림
- hot code 발견 -> native machine code로 컴파일

```
[profiling 정보 분석]
method call frequency
branch predictinon (= 분기 [if, switch])
loop

[최적화 컴파일]
inlining  
dead code 제거  
loop unrolling  
escape analysis
```

C1 vs C2 차이
- C1: 빠른 컴파일 (간단 최적화)
	- 단순 API 환경에서 필요
- C2: 느린 컴파일 (전역 최적화)
	- 추천, 검색, 이미지, 암호화 등 서비스에서 필요

### Hotspot profiling
-  JVM이 runtime 행동을 계속 관찰

```
method call frequency
branch predictinon
lock contention  
allocation rate
```


### CPU 사용량이 큰 순서

(1) JIT 컴파일 (C2)
(2) 클래스 로딩  
(3) bytecode verification  
(4) profiling


---
## Phase 1) JIT 컴파일 C1으로 변경
