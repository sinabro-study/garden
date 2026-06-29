### Isolation
동시에 여러 Transaction 이 수행될 때 충돌을 어디까지 허용할 것인가?

| **격리 수준**        | **의미**                  |
| ---------------- | ----------------------- |
| READ_UNCOMMIED   | 커밋이 되지 않아도 읽기           |
| READ_COMMITED    | 커밋된 것만 읽기               |
| REPEATEABLE_READ | 트랜잭션 시작 시점 스냅샷 기준으로 읽기  |
| SERIALIZABLE     | 트랜잭션이 순차적으로 실행하는 것처럼 동작 |

#### 격리 별 발생 상황

|                | **Dirty Read** | **Non-Repeatable Read** | **Phantom Read**                   |
| -------------- | -------------- | ----------------------- | ---------------------------------- |
| READ_UNCOMMIED | 발생             | 발생                      | 발생                                 |
| READ_COMMITED  | 방지             | 발생                      | 발생                                 |
| REPEATEABLE    | 방지             | 방지                      | 발생 (Oracla, MySQL, Postrgresql 방지) |
| SERIALIZABLE   | 방지             | 방지                      | 방지                                 |

##### Dirty Read
- 다른 트랜잭션이 아직 Commit 하지 않은 데이터를 읽는 현상
	- Commit 여부를 확인하지 않고 다른 트랜잭션의 변경을 읽기 때문, 다른 트랜잭션이 Rollback이 되는 경우 존재하지 않은 데이터 읽기
- 예시
	- T1: Select balance 1,000
	- T1: Update balance 500 (Before Commit)
	- T2: Select balance 500 **(실제 DB 값: 500, undo 값: 1,000)**
	- T1: Update balance 500 (After Commit)

![[Screenshot 2026-06-29 at 4.22.38 AM.png|846]]

##### Non-Repeatable Read
- 같은 트랜잭션에서 동일한 데이터를 다시 조회했을 때 결과가 달라질 수 있는 현상
	- 조회할 때마다 새로운 스냅샷을 생성하여 최신 Commit 데이터를 읽기 때문에 발생
- 예시
	- T1: Select balance 1.000
	- T2: Select balance 1,000
	- T2: Update balance 500 (Before Commit)
	- T2: Update balance 500 (After Commit)
	- T1: Select balance 500
![[Screenshot 2026-06-29 at 4.25.04 AM.png|844]]

##### Phantom Read
- 같은 조건으로 다시 조회했을 때 조회되는 행의 개수가 달라질 수 있는 현상
	- 조회할 때마다 새로운 스냅샷을 생성하여 최신 Commit 데이터를 읽기 때문에 발생
- 예시
	- T1: Select balance >= 500 (3 row)
	- T2: Update Balance 1,000 (300 -> 1,000)
	- T1: Select balance >= 500 (4 row)
 
![[Screenshot 2026-06-29 at 4.37.42 AM.png|847]]

