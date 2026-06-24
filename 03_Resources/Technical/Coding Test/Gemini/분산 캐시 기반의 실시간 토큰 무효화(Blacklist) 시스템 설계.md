> Gemini에게 요청하여 만들어진 문제입니다.

## 요구사항

- **상황:** 서버가 수십 대로 늘어났습니다. 사용자가 로그아웃하거나 계정이 해킹되었을 때 해당 JWT를 즉시 모든 서버에서 무효화해야 합니다.

- **조건 1:** 각 토큰은 고유 ID(`jti`)를 가집니다.
- **조건 2:** 무효화된 토큰 리스트는 메모리 효율을 위해 남은 유효시간(TTL)이 지나면 자동으로 삭제되어야 합니다.
- **조건 3:** 초당 수만 건의 검증 요청이 들어오므로 블랙리스트 확인은 $O(1)$의 시간 복잡도를 지향해야 합니다.
- **조건 4:** (고급 추가) 시스템 아키텍처 설계 관점에서 **키 로테이션(Key Rotation)**이 발생했을 때 구버전 키로 발행된 토큰을 처리하는 로직의 복잡도를 계산해야 합니다.

## 문제

사용자의 토큰 무효화 요청을 처리하고 특정 토큰이 유효한지 검사하는 `TokenManager` 클래스를 구현하십시오.

- `add_blacklist(jti, expiry_timestamp)`: 토큰을 블랙리스트에 추가합니다.
- `is_valid(jti, current_timestamp)`: 토큰이 블랙리스트에 있는지 확인합니다.
- `cleanup_expired(current_timestamp)`: 유효기간이 지난 블랙리스트 데이터를 정리하여 메모리를 확보합니다.

**(제한 사항)**

- **시간 복잡도:** `add_blacklist`와 `is_valid`는 반드시 $O(1)$이어야 합니다.
- **공간 복잡도:** 만료된 토큰을 계속 들고 있으면 안 되며 $O(N)$ (무효화된 토큰 수) 내에서 관리되어야 합니다.

```python
import time

class TokenManager:
    def __init__(self):
        self.blacklist = {} # jti: expiry
        self.expiry_heap = [] # 만료 시간 순 정렬을 위한 팁 (선택 사항)

    def add_blacklist(self, jti: str, expiry_timestamp: int):
        """
        토큰 ID와 만료 시간을 블랙리스트에 등록합니다.
        Time Complexity: O(1)
        """
        pass

    def is_valid(self, jti: str, current_timestamp: int) -> bool:
        """
        현재 토큰이 사용 가능한지 확인합니다. (블랙리스트에 없어야 함)
        Time Complexity: O(1)
        """
        pass

    def cleanup_expired(self, current_timestamp: int):
        """
        유효기간(expiry_timestamp)이 현재 시간보다 작으면 삭제합니다.
        가이드: 전체를 다 돌면 O(N)입니다. 더 효율적인 방법이 있을까요?
        """
        pass

# --- Test Case Template ---
def test_token_manager():
    manager = TokenManager()
    now = int(time.time())

    manager.add_blacklist("token_A", now + 10)
    assert manager.is_valid("token_A", now) == False, "Test 1 Failed: 블랙리스트 토큰은 invalid해야 함"
    assert manager.is_valid("token_B", now) == True, "Test 1 Failed: 일반 토큰은 valid해야 함"

    manager.add_blacklist("token_C", now - 5) # 이미 만료된 토큰 가정
    manager.cleanup_expired(now)

    print("모든 테스트 케이스 통과 가능성이 보입니다! 로직을 완성해 보세요.")

if __name__ == "__main__":
    test_token_manager()
```

- **시간 복잡도 측정:**
  - `time.perf_counter()`를 사용하여 10만 건의 `is_valid` 호출 시 소요 시간을 측정해 보세요.
  - 평균 $1\mu s$ (마이크로초) 이하로 나와야 고급 레벨 합격입니다.
- **공간 복잡도 측정:**
  - `sys.getsizeof()`를 통해 `blacklist` 자료구조의 크기 변화를 관찰하세요.
  - `cleanup_expired` 호출 전후로 메모리 점유율이 유의미하게 줄어드는지 확인해야 합니다.

```python
import time
import sys
import random
import string
import heapq

# --- 성능 측정 도구 ---
def run_performance_test():
    manager = TokenManager()
    data_size = 100000  # 10만 건 테스트
    jtis = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(data_size)]
    now = int(time.time())

    print(f"--- [성능 테스트 시작: 데이터 {data_size}건] ---")

    # 1. 삽입(Add) 성능 측정
    start_time = time.perf_counter()
    for i in range(data_size):
        manager.add_blacklist(jtis[i], now + random.randint(1, 100))
    end_time = time.perf_counter()
    print(f"1. 삽입 시간(Add): {end_time - start_time:.4f}초 (평균 {(end_time - start_time)/data_size*10**6:.2f}μs)")

    # 2. 조회(is_valid) 성능 측정
    start_time = time.perf_counter()
    for i in range(data_size):
        manager.is_valid(jtis[i], now)
    end_time = time.perf_counter()
    print(f"2. 조회 시간(is_valid): {end_time - start_time:.4f}초 (평균 {(end_time - start_time)/data_size*10**6:.2f}μs)")

    # 3. 공간 복잡도(Memory) 측정
    mem_size = sys.getsizeof(manager.blacklist) + sys.getsizeof(manager.min_heap)
    print(f"3. 현재 메모리 사용량: {mem_size / 1024 / 1024:.2f} MB")

    # 4. 정리(Cleanup) 성능 측정
    # 일부 데이터를 강제로 만료시킴
    past_time = now + 101
    start_time = time.perf_counter()
    manager.cleanup_expired(past_time)
    end_time = time.perf_counter()
    print(f"4. 정리 시간(Cleanup): {end_time - start_time:.4f}초")

    # 정리 후 메모리 확인
    new_mem_size = sys.getsizeof(manager.blacklist) + sys.getsizeof(manager.min_heap)
    print(f"5. 정리 후 메모리 사용량: {new_mem_size / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    run_performance_test()
```

## 완성 코드
```python
class TokenManager:
  def __init__(self):
    self.blacklist = {}
    self.expiry_heap = []

  def add_blacklist(self, jti: str, expiry_timestamp: int):
    now = int(time.time())
    
    if now > expiry_timestamp:
      return

    self.blacklist[jti] = expiry_timestam
    heapq.heappush(self.expiry_heap, (expiry_timestamp, jti))

  def is_valid(self, jti: str, current_timestamp: int) -> bool:
    if jti not in self.blacklist:
      return True

    if self.blacklist[jti] < current_timestamp:
      return True
    else:
      return False

    def cleanup_expired(self, current_timestamp: int):
      while self.expiry_heap and self.expiry_heap[0][0] < current_timestamp:
        heapq.heappop(self.expiry_heap)
```
