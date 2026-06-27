## Current Focus
```dataview
TABLE file.ctime as 작성일자
FROM "03_Resources/Technical"
WHERE file.ctime >= date(2026-01-01)
SORT file.ctime DESC
LIMIT 10
```

## Long-term Direction
- 기술 전략 수립
- 시스템 아키텍처 결정

## Stage별 기술 역량

> [!danger] Stage 1 · Engineer
> 언어 & 프레임워크, Spring / JPA / DB, API 구현, 테스트 코드, 운영 이슈 해결

> [!warning] Stage 2 · Senior Engineer
> MVCC, Transaction, Isolation, Lock, Redis, Cache, Index, Query Optimization, MSA, 장애 대응, 성능 최적화

> [!tip] Stage 3 · Staff Engineer / Tech Lead
> 시스템 설계, 서비스 경계 정의, API 표준, 데이터 모델, 기술 부채 관리, FE/BE Architecture, Design System

> [!example] Stage 4 · Principal Engineer / Architect
> Platform Architecture, Event Driven, Domain Boundary, Data Architecture, Observability, Reliability Engineering

> [!success] Stage 5 · CTO / Distinguished Engineer
> 기술 전략, 플랫폼 투자, AI 전략, Build vs Buy
