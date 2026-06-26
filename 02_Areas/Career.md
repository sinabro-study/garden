## Identity
나는 백엔드 개발을 기반으로 시스템 설계와 기술 의사결정을 수행하며 조직의 생산성을 높이는 엔지니어가 된다.
  
- Current Role: **Project Lead Engineer** **(회사)**
- Next Role: **Staff Engineer / Tech Lead**

## Current Focus
### Technical
```dataview
TABLE file.ctime as 작성일자
FROM "03_Resources/Technical"  
WHERE file.ctime >= date(2026-01-01)
SORT file.ctime DESC
LIMIT 10
```

### Leadership
```dataview
TABLE file.ctime as 작성일자
FROM "03_Resources/Leadership"
WHERE file.ctime >= date(2026-01-01)
SORT file.ctime DESC
LIMIT 10
```


### Organization
```dataview
TABLE file.ctime as 작성일자
FROM "03_Resources/Organization"
WHERE file.ctime >= date(2026-01-01)
SORT file.ctime DESC
LIMIT 10
```

## Long-term Direction
- 기술 전략 수립
- 시스템 아키텍처 결정
- 조직 기술 방향 설정
- 팀 생산성 극대화

---

## Engineering Career Roadmap

|           | Stage 1 <br>Engineer | Stage 2<br>Senior Engineer | Stage 3<br>Staff / Tech Lead | Stage 4<br>Principal | Stage 5<br>CTO  |
| --------- | -------------------- | -------------------------- | ---------------------------- | -------------------- | --------------- |
| **사고 범위** | 나(개인) & 코드 품질        | 서비스 / 시스템                  | 팀 & 팀 생산성                    | 조직 단위 생산성            | 회사 전체           |
| **협업**    | 요구사항 이해<br>리뷰 반영     | 설계 리뷰<br>멘토링               | 기술 의사결정 주도                   | 여러 팀 조율              | 경영진 협업<br>조직 설계 |
| **비즈니스**  | 기능 개발<br>버그 수정       | 안정성<br>비용 절감               | 생산성<br>속도 향상                 | 플랫폼 효율 극대화           | 매출 성장<br>사업 확장  |
| **핵심 질문** | 어떻게 구현할까?            | 유지 가능한가?                   | 팀 표준은?                       | 3년 뒤에도?              | 회사는 어디로?        |


> [!danger] Stage 1 · Engineer — 나(개인) & 코드 품질
> **기술** — 언어 & 프레임워크, Spring / JPA / DB, API 구현, 테스트 코드, 운영 이슈 해결
> **협업** — 요구사항 이해, 코드 리뷰 반영, 팀 규칙 준수
> **비즈니스** — 기능 개발, 버그 수정, 일정 내 완료
> **핵심 질문** — *"어떻게 구현할까?"*

> [!warning] Stage 2 · Senior Engineer — 서비스 / 시스템 단위 품질
> **기술** — MVCC, Transaction, Isolation, Lock, Redis, Cache, Index, Query Optimization, MSA, 장애 대응, 성능 최적화
> **협업** — 설계 리뷰 참여, 코드 리뷰 주도, 주니어 멘토링
> **비즈니스** — 서비스 안정성, 장애 감소, 운영 비용 절감
> **핵심 질문** — *"이 구조가 장기적으로 유지 가능한가?" / "Trade-off는?"*

> [!tip] Stage 3 · Staff Engineer / Tech Lead — 팀 & 팀 생산성
> **기술** — 시스템 설계, 서비스 경계 정의, API 표준, 데이터 모델, 기술 부채 관리, FE/BE Architecture, Design System
> **협업** — 기술 의사결정 주도, 설계 리뷰 진행, FE/BE/Design 조율, 기술 방향성 제시
> **비즈니스** — 팀 생산성, 개발 속도 향상, 기술 리스크 감소
> **핵심 질문** — *"우리 팀의 표준은?" / "팀 전체가 더 빨라지려면?"*

> [!example] Stage 4 · Principal Engineer / Architect — 조직 단위 생산성
> **기술** — Platform Architecture, Event Driven, Domain Boundary, Data Architecture, Observability, Reliability Engineering
> **협업** — 여러 팀 기술 조율, 조직 기술 전략 수립, Architecture Review
> **비즈니스** — 조직 생산성, 플랫폼 효율 극대화, 기술 투자 방향
> **핵심 질문** — *"5개 팀이 동시에 성장하려면?" / "이 구조가 3년 뒤에도 살아남을까?"*

> [!success] Stage 5 · CTO / Distinguished Engineer — 회사 전체
> **기술** — 기술 전략, 플랫폼 투자, AI 전략, Build vs Buy
> **협업** — 경영진 협업, 조직 설계, 리더 육성
> **비즈니스** — 매출 성장, 비용 절감, 사업 확장
> **핵심 질문** — *"기술이 사업 성장에 어떻게 기여하는가?" / "회사가 어디로 가야 하는가?"*
