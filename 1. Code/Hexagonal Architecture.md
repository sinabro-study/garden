## Layerd Architecture의 문제점
- 서비스 계층이 비대해진다.
    - 많은 내용이 함축되어 있기 때문에 테스트를 진행하기 어렵다.
    - 영속성 계층에 많은 의존성을 지니게 된다.
- 동시 작업이 어려워진다.
    - 서비스/웹 계층은 영속성 계층위에 만들어지기 때문에 영속성 계층이 가장 먼저 개발되어야 한다.

## Hexagonal Architecture

![[hexagonal-architecture.png]]


|   용어    |                   설명                   |             예시             |
| :-----: | :------------------------------------: | :------------------------: |
| Adapter |        Application과 상호작용하는 시스템         |       Web, Database        |
|  Port   |    Application Core와 Adapter의 통신 수단    |  Input Port, Output Port   |
| Usecase |        Domain Entity와 상호작용하는 계층        | Usecase (SendMoneyUsecase) |
| Entity  | Application을 구성하기 위해 필요한 Domain Entity |      Entity (Account)      |

```folder
account
ㄴ adapter
  ㄴ in
    ㄴ AcountApiAdapter
  ㄴ out
    ㄴ persistence
      ㄴ AccountPersistenceAdapter
      ㄴ AccountJpaRepository
ㄴ application
  ㄴ port
    ㄴ in
      ㄴ SendMoneyUsecase
    ㄴ out
      ㄴ LoadAccountPort
      ㄴ UpdateAccountStatePort
  SendMoneyService
ㄴ domain
  ㄴ Account
  ㄴ Activity
```

## Usecase 둘러보기
- 비즈니스 규칙을 검증할 책임
	- 비즈니스 규칙을 충족하면 Usecase는 입력을 기반으로 어떤 방법으로든 모델의 상태 변경
		- 유효성 검증: 사용자가 올바르지 않은 값을 예바하는 규칙 (ex. 음수는 입력 불가)
		- 비즈니스 검증: 회사에서 정하는 규칙 (ex. 최대 OOO 만원까지 송금 가능)
	- 일반적으로 도메인 객체의 상태를 바꾸고 Persistence Adapter를 통해 구현된 Port로 이 상태를 전달해서 저장
	- Usecase는 또 다른 outgoing adapter 호출 가능
- 도메인 엔티티와 책임을 공유

## 입력 유효성 검증하기
- 입력 모델에서 입력 유효성을 검증한다.
- [Bean Validation API](https://beanvalidation.org/)를 사용한다.
- Kotlin을 사용하는 경우 require()를 사용한다.

```kotlin
data class SendMoneyCommand(
  val name: String
) {

  init {
    require(name.isNotBlank()) { "이름은 비어 있을 수 없습니다." }
  }
}
```


## Usecase 마다 다른 출력 모델
- 입력과 비슷하게 출력도 각 Usecase에 맞게 구체적일 것 (호출자에게 필요한 데이터만)
- Usecase들 간에 같은 출력 모델을 공유하게 되면 Usecase 들도 강하게 결합된다.
	- 공유 모델은 장기적으로 봤을 때 갖가지 이유로 커지게 되어있다.
	- Domain Entity를 출력 모델로 사용하지 않아야 한다.

## 읽기 전용 Usecase
- Incoming 전용 Port를 만들고 Query Service에 구현하는 것
- Read Only Query는 Write가 가능한 Usecase와 코드 상에서 명확하게 구분
	- CQS(Command-Query Seperation)와 CQRS(Command-Query Responsibility Segregation) 개념과 잘 맞는다.
