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

실행 흐름: `OrderCalculator.java` → `javac` → `OrderCalculator.class` → `java OrderCalculator` → `main` → 항목 합산 → 배송비 판단 → 총액 출력.

## 주문 금액 계산기 실습

아래 **Java 코드 블록만** 복사해 `OrderCalculator.java`라는 파일로 저장하고 직접 컴파일·실행한다.
위의 실행 흐름 설명은 파일에 넣지 않는다.
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

## 최초 평가 · 2026-11-16

정답 1개, 부분 정답 4개. 실제 컴파일·실행 명령과 출력 결과는 아직 제출되지 않았다.

| 문항 | 평가 | 답변과 해설 |
|---|---|---|
| 1 | 부분 정답 | 이전 `.class` 파일이 실행된다는 설명은 맞다. 재컴파일 명령에는 소스 파일의 확장자를 포함해 `javac OrderCalculator.java`라고 써야 한다. 그다음 `java OrderCalculator`를 실행한다. |
| 2 | 정답 | `alias`가 같은 배열을 가리킬 때 요소를 바꾸므로 `items[0]`은 6,000이다. `alias`를 새 배열로 재대입한 뒤에도 `items[0]`은 6,000이다. |
| 3 | 부분 정답 | 누적값 5,000 → 13,000 → 25,000과 종료 시 `i = 3`은 맞다. 각 반복에서 읽는 값은 `itemTotals[0] = 5000`, `itemTotals[1] = 8000`, `itemTotals[2] = 12000`이다. |
| 4 | 부분 정답 | 반환값 24,999와 2,500, 출력값 27,499는 맞다. 배송비 조건 `24999 >= 25000`의 결과는 거짓이다. |
| 5 | 부분 정답 | 빈 배열에서 첫 조건 `0 < 0`이 거짓이고 본문 0회, 두 반환값 0과 2,500은 맞다. `main`의 최종 출력값 `2500`이 빠졌다. 답변의 `lenght`는 `length`의 오타다. |

### 보완 확인

- **6-1.** `javac`로 컴파일할 때 지정하는 정확한 파일 이름과, 이어서 실행할 명령을 적는다.
- **6-2.** `{5000, 8000, 12000}`에서 `i = 0, 1, 2`가 각각 읽는 `itemTotals[i]`와 누적값을 짝지어 적는다.
- **6-3.** 상품 합계가 24,999원일 때 `subtotal >= 25000`의 참·거짓을 적고 배송비를 설명한다.
- **6-4.** 빈 배열일 때 `main`의 최종 출력값을 적는다.

실습 코드의 컴파일·실행을 직접 시도했다면 사용한 명령과 터미널의 실제 출력도 함께 적는다. 실행하지 못했다면 그 사실과 오류를 적는다.
