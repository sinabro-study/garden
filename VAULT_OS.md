# Obsidian PARA 기반 인생 로드맵

## 목표

Obsidian을 단순 노트앱이 아니라 인생 로드맵으로 사용한다.

- 입력 → 자동 분류 → 지식 축적 → 커리어 관리
- 수동 정리 최소화
- 메타데이터 기반 구조화

## 전체 구조 (PARA OS)

| 폴더             | 역할          |
| -------------- | ----------- |
| `00_Inbox`     | 모든 입력 (미처리) |
| `01_Areas`     | 지속 관리 영역    |
| `02_Projects`  | 진행 중 작업     |
| `03_Resources` | 지식 저장소      |
| `04_Archive`   | 완료 기록       |
| `attachments`  | 첨부파일 통합 관리  |

## 핵심 개념

### Areas = 상태 관리
- 계속 책임지는 영역 (삶 / 커리어 / 기술 상태)
- **Area는 폴더가 아니라 문서다** — `Engineering.md`, `Career.md` 형태
- 내용: 목적 정의 / 현재 집중 영역 / 진행 중 프로젝트 링크 / 핵심 리소스 링크 / 성장 방향
- 예: `Career`, `Engineering`, `Finance`, `Family`

### Projects = 실행 단위
- 시작과 끝이 존재하는 행동 중심 작업
- 예: `MVCC Deep Dive`, `Redis Pipeline 분석`, `코테 준비`

### Resources = 지식
- 재사용 가능한 정보 (문제 풀이 + 개념 + 코드)
- 예: `MVCC.md`, `JPA Transaction.md`, `System Design Notes`

### Archive = 종료 기록
- 끝난 프로젝트 저장, 수정하지 않음


## Engineering Area 구조

```
Engineering (Area)
├── Backend
├── System Design
├── Database
├── Coding Test
└── DevOps
```


## 자동화 핵심

### 메타데이터 기반

```yaml
---
type: project
area: Engineering
status: active
---
```

### Dataview 자동 집계
- Area → Project 자동 리스트
- Resource 자동 분류
- Archive 자동 조회

### Area 자동 업데이트 구조
- Project 생성 시 `area` 지정
- `status` 변경 시 자동 반영
- `Area.md`는 항상 "자동 대시보드"


## 핵심 철학

| 레이어      | 의미         |
| -------- | ---------- |
| Area     | 삶 / 커리어 상태 |
| Project  | 행동         |
| Resource | 지식         |
| Archive  | 기록         |

> **Obsidian PARA OS는 "노트를 정리하는 시스템"이 아니라
> "개발자의 사고와 행동을 자동으로 축적하는 운영체제다"**
