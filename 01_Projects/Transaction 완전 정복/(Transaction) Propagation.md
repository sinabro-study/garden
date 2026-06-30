### Propagation
현재 실행 컨텍스트에 이미 존재하는 트랜잭션과 새로운 실행 사이의 참여 정책

### Join
- 기존 트랜잭션 참여

| 옵션        | 설명                    |
| --------- | --------------------- |
| REQUIRED  | 있으면 편승, 없으면 생성        |
| SUPPORT   | 있으면 편승, 없으면 Non-TX    |
| MANDATORY | 있으면 편승, 없으면 Exception |
![[Screenshot 2026-06-30 at 5.00.54 AM.png]]

### Suspend
- 기존 트랜잭션 잠시 중단

| 옵션            | 설명                     |
| ------------- | ---------------------- |
| REQUIRED_NEW  | 기존 TX 중단 후, 신규 TX 생성   |
| NOT_SUPPROTED | 기존 TX 중단 후, Non-TX로 실행 |
| NEVER         | TX 존재하면 Exception      |
![[Screenshot 2026-06-30 at 5.09.33 AM.png]]

### Savepoint
- 같은 트랜잭션 안에 복구 지점 생성

| 옵션     | 설명                 |
| ------ | ------------------ |
| NESTED | 동일 TX 내에서 부분 롤백 가능 |
![[Screenshot 2026-06-30 at 5.01.32 AM.png]]