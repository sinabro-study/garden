## Reviewer?
: 작성자를 제외한 코드 리뷰를 요청받은 동료

### Check List
- Coding Convention
	- [Google Java Convention](https://google.github.io/styleguide/javaguide.html)
	- [Kotlin Convention](https://kotlinlang.org/docs/coding-conventions.html)
- 기능 동작: 기능이 올바로 수행하는지 확인
- 테스트 코드: 통합/단위 테스트를 수행할 수 있는지 확인
- 버그 가능성: 비즈니스 규칙에 어긋나거나 문법상 에러가 발생할 수 있는 부분 확인
- 설계: 시스템에 적합하고 확장 가능한지 확인

### Mindset
- 개선이 필요한 이유를 명확히 설명합니다.
	- 근거가 부족하다면 개인 의견이거나 개선이 필요한 내용이 아닐 가능성이 있습니다.
- [[Reviewee]] 스스로 고민하고 개선할 수 있도록 합니다.
	- 떠먹여주지 않고 스스로 성장할 수 있도록 해야합니다.

```
(지항) OOO 으로 구현하면 어떤 현상이 일어날까요?
(지양) OOO 으로 구현해주세요. XXX 하기 때문입니다.
```
- Reviewee에게 피드백을 줄 수도 있고 받을 수도 있습니다.
	- 알고 있는 지식을 공유하고 새로운 내용을 배우려는 태도를 지향합니다.
- 개선할 내용이 없다면 칭찬합니다.
	- 리뷰를 위한 리뷰를 진행할 필요는 없습니다.
