# 10주차 다섯 번째 수업 · EventBridge와 이벤트 라우팅

![AWS 공식 EventBridge 이벤트 버스 구성도](https://docs.aws.amazon.com/images/eventbridge/latest/userguide/images/bus-overview_eventbridge_conceptual.svg)

## 이벤트 버스와 규칙

**이벤트**는 이미 일어난 일을 설명하는 데이터다. 예를 들어 주문 결제 완료 이벤트에는 주문 번호와 결제 상태가 들어간다.
**이벤트 버스**는 이벤트를 받아 목적지로 전달하는 역할을 한다.
이번 수업은 버스 소유자가 규칙과 대상을 설정하는 **Classic 이벤트 버스**를 다룬다.
**규칙**은 어떤 이벤트를 전달할지 정하는 패턴과 어디에 전달할지 정하는 대상을 연결한다.
예를 들어 결제 완료 이벤트만 배송 SQS 큐로 보내고 주문 취소 이벤트만 환불 SQS 큐로 보낼 수 있다.

## 패턴 읽기

아래 배송 규칙은 이벤트의 `source`가 `shop.orders`이고 `detail-type`이 `OrderPaid`일 때 일치한다.

```json
{
  "source": ["shop.orders"],
  "detail-type": ["OrderPaid"]
}
```

두 필드가 모두 맞아야 이 규칙의 대상에 전달된다.
EventBridge는 같은 버스의 규칙을 각각 평가한다.
이벤트가 여러 규칙에 맞으면 각 규칙의 대상으로 전달한다.
일치하는 규칙이 없으면 규칙을 통한 대상 전달은 일어나지 않는다.
대상이 SQS라면 큐에 들어간 메시지를 워커가 나중에 받아 처리한다.

## 공식 문서 핵심 요약

- Classic 이벤트 버스는 이벤트를 여러 규칙과 비교하고 일치하는 규칙의 대상으로 전달한다. 이벤트 하나가 여러 규칙에 일치하거나 하나도 일치하지 않을 수 있다. [AWS 이벤트 버스 문서](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
- 이벤트 패턴은 이벤트의 출처나 유형, 세부 데이터 등으로 전달 조건을 표현한다. 조건에 맞는 이벤트만 해당 규칙의 대상으로 전달한다. [AWS 이벤트 패턴 문서](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html)

## 확인 문제

대상 권한은 정상이고 버스에는 아래 두 규칙만 있다.

| 규칙 | source | detail-type | 대상 |
|---|---|---|---|
| 배송 | `shop.orders` | `OrderPaid` | 배송 SQS 큐 |
| 고객 알림 | `shop.orders` | `OrderPaid` 또는 `OrderCancelled` | 알림 SQS 큐 |

**1-1.** `shop.orders`의 `OrderPaid` 이벤트 하나를 발행하면 어느 큐에 들어가는가?

**1-2.** `shop.orders`의 `OrderCancelled`는 어느 큐에 들어가는가? 배송 규칙도 일치하는가?

**2-1.** `shop.test`에서 `OrderPaid`를 발행했다. 두 규칙 중 어느 것과 일치하고 대상에 전달되는가?

**2-2.** 취소 이벤트를 받을 새 환불 워커를 붙이되 기존 고객 알림은 계속 동작해야 한다. 새 환불 큐에 연결할 규칙의 출처와 이벤트 유형은 무엇이며 고객 알림 규칙도 수정해야 하는가?

## 확인 문제 평가 · 2026-11-10

하위 4/4 정답.

- **1-1.** 결제 완료는 두 규칙에 일치하므로 배송 큐와 알림 큐에 모두 들어간다.
- **1-2.** 주문 취소는 알림 규칙에만 일치하므로 알림 큐에만 들어간다.
- **2-1.** 출처가 `shop.test`이면 두 규칙에 모두 불일치하므로 전달되지 않는다.
- **2-2.** `shop.orders`와 `OrderCancelled`를 조건으로 환불 큐를 대상으로 하는 규칙을 추가한다. 기존 알림 규칙은 그대로 작동한다.
