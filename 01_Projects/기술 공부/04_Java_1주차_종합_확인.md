# 1주차 종합 확인 · Java 실행과 주문 금액 계산

## 목표

- 소스 수정부터 출력까지 `javac`와 `java`의 역할을 연결한다.
- 기본형 값과 배열 참조의 변화를 구분한다.
- 조건문, 메서드 반환값, 배열 반복을 이용해 주문 금액을 계산한다.

## 핵심 흐름

`javac OrderCalculator.java`는 소스 파일을 컴파일해 `OrderCalculator.class`를 만든다.
`java OrderCalculator`는 그 클래스의 `main`을 실행한다.
`main`에서 배열을 메서드에 전달하면 메서드는 배열 요소를 순서대로 읽고 합계를 반환한다.
합계가 25,000원 이상이면 배송비 0원, 그보다 작으면 2,500원을 반환한다.

```mermaid
flowchart LR
    source["OrderCalculator.java"] -->|javac| class["OrderCalculator.class"]
    class -->|java| main["main 실행"]
    main --> subtotal["항목 합산"]
    subtotal --> shipping["배송비 판단"]
    shipping --> output["총액 출력"]
```

## 주문 금액 계산기 실습

아래 코드를 `OrderCalculator.java`로 저장하고 직접 컴파일·실행한다.
문제 답변에는 사용한 명령과 실제 출력값을 함께 적는다.

```java
public class OrderCalculator {
    public static void main(String[] args) {
        int[] itemTotals = {5000, 8000, 12000};
        int subtotal = calculateSubtotal(itemTotals);
        int shipping = calculateShipping(subtotal);
        int total = subtotal + shipping;
        System.out.println(total);
    }

    static int calculateSubtotal(int[] itemTotals) {
        int subtotal = 0;
        for (int i = 0; i < itemTotals.length; i++) {
            subtotal += itemTotals[i];
        }
        return subtotal;
    }

    static int calculateShipping(int subtotal) {
        if (subtotal >= 25000) {
            return 0;
        }
        return 2500;
    }
}
```

```sh
javac OrderCalculator.java
java OrderCalculator
```

## 종합 확인 문제

정답과 이유를 각 문항 번호에 맞춰 적는다. 5문항을 모두 답한 뒤 해설을 제공한다.

1. 소스의 `itemTotals`를 `{5000, 8000}`으로 바꾼 뒤 `java OrderCalculator`만 다시 실행했다. 이전에 만든 `.class` 파일은 그대로다. 어떤 코드가 실행되는지, 새 소스 변경을 반영하려면 무엇을 해야 하는지 설명한다.
2. `int[] items = {5000, 8000, 12000}; int[] alias = items; alias[0] = 6000;`을 실행했다. `items[0]`의 값과 이유를 설명한다. 이어서 `alias = new int[]{7000};`으로 재대입하면 `items[0]`이 얼마인지도 적는다.
3. 실습 코드의 `itemTotals`에 대해 반복이 끝날 때까지 각 `i`에서 읽는 값과 더한 직후 `subtotal`을 순서대로 적는다. 반복이 끝나는 첫 `i`도 적는다.
4. `itemTotals`를 `{10000, 14999}`로 바꾸면 `calculateSubtotal`과 `calculateShipping`의 반환값, `main`의 출력값은 각각 얼마인가? 배송비 조건식이 참인지 거짓인지 설명한다.
5. `itemTotals`를 빈 배열 `{}`로 바꾸면 반복문 본문 실행 횟수와 두 메서드의 반환값, 최종 출력값은 각각 얼마인가? 첫 반복 조건을 근거로 설명한다.

실습 실행이 어려우면 환경과 시도한 명령, 나타난 오류를 적는다. 실제 실행 여부와 계산으로 예측한 값을 구분해 평가한다.
