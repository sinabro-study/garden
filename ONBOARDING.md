# CGKR 팀 개발 환경 설정

팀 가이드라인·커맨드·도구를 설정하는 1회 온보딩이다. 아래 스크립트 하나로 끝난다.

## 실행

```bash
git clone https://github.com/colosseumcoinckr/cgkr_team_guidelines ~/cgkr_team_guidelines
bash ~/cgkr_team_guidelines/setup.sh
```

- 멱등 스크립트 — 재실행 안전 (이미 클론돼 있으면 clone 생략하고 setup.sh만)
- 실행 중 프롬프트 2개가 나온다: **Graphite 토큰**(안내되는 URL에서 발급 후 붙여넣기), **담당 레인**(BE 또는 FE 입력)

## 실행 후 안내

1. MCP 인증: Claude Code에서 `/mcp` 실행 → atlassian / slack / github 각각 브라우저 OAuth (회사 계정, 1회)
2. 새 세션부터 팀 가이드라인·커맨드(/dd-publish, /dev-epic 등)가 자동 적용되며, 업데이트는 세션 시작 시 자동 반영됨
3. 상세 내용은 레포 README 참조
