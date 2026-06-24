## Pull Request란?
- 내가 작업한 브랜치의 변경사항을 다른 브랜치에 병합해 달라고 요청하는 것
- 해당 단계에서 [[Code Review]]가 이루어짐

## 작성 해야하는 이유는?
- 변경 사항의 명확한 전달
- 해당 방식으로 구현한 Code 이외의 Background 설명
- 일관된 방식으로 message를 작성하여 협업 추진

## 작성 방법
- Background
	- 코드를 추가/변경하게 된 배경
- Changes
	- 코드 추가/변경 사항
- Test
	- 로컬 환경에서 테스트 진행한 결과물

```
[Background]
- Jira: {Jira URL}
- Figma: {Figma URL}
  
[Changes]
- {코드 추가/변경 사항 간략한 내용}
  
[Test]
# 상황에 따라 유연하게 선택
- Request
- Response
- Data
  
- AS-IS
- TO-BE
```

## Template 생성 방법

#### 단일 Project 적용
1. .github folder 생성
2. pull_request_template.md 작성

#### Organization 내부 전체 Project 적용
1. .github Repository 생성
2. pull_request_template.md 작성
