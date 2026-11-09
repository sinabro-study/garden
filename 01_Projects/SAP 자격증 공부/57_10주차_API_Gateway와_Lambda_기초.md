# 10주차 첫 수업 · API Gateway와 Lambda 기초

![AWS 공식 REST API 참조 구성](https://docs.aws.amazon.com/images/wellarchitected/latest/serverless-applications-lens/images/reference-architecture-for-restful-microservices.png)

[AWS가 발행한 원본 구성도](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/restful-microservices.html)

## 1. 주문 요청의 흐름

**API Gateway**는 클라이언트의 HTTP 요청을 받는 API 엔드포인트를 제공한다.
어떤 HTTP 메서드와 경로를 어떤 백엔드에 연결할지 설정한다.
예를 들어 `POST /orders`를 `CreateOrder` Lambda 함수에 연결한다.

**Lambda**는 AWS가 관리하는 실행 환경에서 함수 코드를 실행한다.
이 예에서 주문 수량을 검증하고 주문을 저장하는 코드는 함수에 들어간다.
사용자는 함수 코드와 설정을 관리하고 AWS는 실행에 필요한 서버를 관리한다.
**서버리스**란 이처럼 앱을 운영할 때 서버를 직접 관리할 필요가 없는 방식이다.

## 2. 저장과 응답

`POST /orders` 요청을 받으면 API Gateway가 연결된 Lambda 함수를 호출한다.
이 예는 **동기 호출**이므로 API Gateway는 함수의 결과를 기다려 클라이언트에 HTTP 응답을 돌려준다.
함수는 주문 데이터를 검증한 뒤 DynamoDB에 저장하고 성공 시 HTTP 201에 해당하는 결과를 반환한다.
나중에 다른 함수 실행에서도 주문을 조회할 수 있도록 주문 상태는 DynamoDB에 저장한다.

## 3. 호출 권한과 저장 권한

API Gateway가 함수 호출을 시작하려면 Lambda 함수의 리소스 기반 정책에서 해당 API의 호출을 허용한다.
함수가 주문을 저장하려면 Lambda의 **실행 역할**에 주문 테이블의 `dynamodb:PutItem` 권한을 부여한다.
하나는 API Gateway에서 함수로 가는 권한이고 다른 하나는 함수에서 DynamoDB로 가는 권한이다.

[AWS Lambda와 API Gateway 실습 문서](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-tutorial.html)
[AWS API Gateway의 Lambda 통합 문서](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integrations.html)

## 확인 문제

클라이언트가 `POST /orders`를 보내면 API Gateway가 `CreateOrder`를 동기 호출한다.
함수는 주문 수량을 검증하고 DynamoDB의 `Orders` 테이블에 저장한다.

**1-1.** HTTP 요청을 처음 받는 서비스와 주문 수량을 검증하는 코드를 실행하는 서비스는 각각 무엇인가?

**1-2.** 함수가 주문을 저장하고 HTTP 201에 해당하는 결과를 반환했다. 그 결과를 HTTP 응답으로 클라이언트에 보내는 서비스는 무엇인가? 이 흐름에서 함수 결과를 기다리는가?

**2-1.** API Gateway가 함수를 호출할 수 있고 함수도 실행됐다. 그런데 함수가 `Orders`에 `PutItem`을 할 때 권한 거부가 발생했다. 어느 역할에 어떤 권한을 추가해야 하는가?

**2-2.** 반대로 함수의 실행 역할에 `PutItem`은 허용되어 있지만 API Gateway에 함수 호출 권한이 없다. API Gateway가 함수를 호출할 수 있는가? 어느 쪽 정책을 확인해야 하는가?

## 확인 문제 평가 · 2026-11-09

하위 문항 정답 3개, 부분 정답 1개.

- **1-1 정답.** API Gateway가 HTTP 요청을 받고 Lambda가 주문 수량을 검증한다.
- **1-2 정답.** 동기 호출이므로 API Gateway는 함수 결과를 기다려 클라이언트에 HTTP 응답을 보낸다.
- **2-1 부분 정답.** `dynamodb:PutItem`은 맞다. 이 권한은 `Orders` 테이블을 대상으로 Lambda 함수의 실행 역할에 부여한다.
- **2-2 정답.** 함수 실행 역할의 저장 권한과 별개로, API Gateway가 호출하려면 이 구성에서는 Lambda 함수의 리소스 기반 정책에 해당 API의 `lambda:InvokeFunction`을 허용해야 한다.

**2-1 보완.** `Orders`에 대한 `dynamodb:PutItem`을 어느 IAM 역할에 부여하는지 확인한다.

**2-1 보완 정답.** Orders 테이블에 대한 `dynamodb:PutItem` 권한은 Lambda 함수의 IAM 실행 역할에 부여한다.
