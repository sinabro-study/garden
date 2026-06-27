## Current Focus
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
- 조직 기술 방향 설정
- 팀 생산성 극대화

## Stage별 협업 역량

> [!danger] Stage 1 · Engineer
> 요구사항 이해, 코드 리뷰 반영, 팀 규칙 준수

> [!warning] Stage 2 · Senior Engineer
> 설계 리뷰 참여, 코드 리뷰 주도, 주니어 멘토링

> [!tip] Stage 3 · Staff Engineer / Tech Lead
> 기술 의사결정 주도, 설계 리뷰 진행, FE/BE/Design 조율, 기술 방향성 제시

> [!example] Stage 4 · Principal Engineer / Architect
> 여러 팀 기술 조율, 조직 기술 전략 수립, Architecture Review

> [!success] Stage 5 · CTO / Distinguished Engineer
> 경영진 협업, 조직 설계, 리더 육성
