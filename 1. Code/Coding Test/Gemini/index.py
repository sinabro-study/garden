import time
import sys
import random
import string
import heapq

class TokenManager:
    def __init__(self):
        self.blacklist = {}
        self.expiry_heap = []

    def add_blacklist(self, jti: str, expiry_timestamp: int):
        now = int(time.time())

        if now > expiry_timestamp:
            return
        
        self.blacklist[jti] = expiry_timestamp
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
    mem_size = sys.getsizeof(manager.blacklist) + sys.getsizeof(manager.expiry_heap)
    print(f"3. 현재 메모리 사용량: {mem_size / 1024 / 1024:.2f} MB")

    # 4. 정리(Cleanup) 성능 측정
    # 일부 데이터를 강제로 만료시킴
    past_time = now + 101
    start_time = time.perf_counter()
    manager.cleanup_expired(past_time)
    end_time = time.perf_counter()
    print(f"4. 정리 시간(Cleanup): {end_time - start_time:.4f}초")

    # 정리 후 메모리 확인
    new_mem_size = sys.getsizeof(manager.blacklist) + sys.getsizeof(manager.expiry_heap)
    print(f"5. 정리 후 메모리 사용량: {new_mem_size / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    test_token_manager()
    run_performance_test()