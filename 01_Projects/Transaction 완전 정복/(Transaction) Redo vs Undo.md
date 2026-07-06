## Redo Log
- 변경 된 이후의 내역을 저장 (After Image)
	- 어떤 변경 사항을 재실행할 것인가?
- 크래시 전 Commit 은 완료되었지만 dirty page가 디스크에 flush 되지 않은 경우
	- Commit 반영
	- Dirty Page -> Disk 미반영 (Flush X)


![[Screenshot 2026-07-06 at 4.55.43 AM.png]]



![[Screenshot 2026-07-06 at 4.56.00 AM.png]]

| 용어       | 설명                                       | 특징                                                                               |
| -------- | ---------------------------------------- | -------------------------------------------------------------------------------- |
| Steal    | 미완료 TX dirty page flush 가능               |                                                                                  |
| No-Steal | 완료 TX dirty page flush 가능                | 미완료 TX는 commit 전까지 buffer pool 대기 -> buffer pool 고갈 가능<br>undo log로 미완료 tx 롤백 보장 |
| Force    | commit 즉시 .ibd flush                     |                                                                                  |
| No-Force | commit 시 redo log만 flush, ibd는 나중에 (WAL) | WAL (Write-Ahead Logging) Commit 시<br>Redo Log를 먼저 디스크에 fsync                    |

| 조합                  | Undo 필요 | Redo 필요 | 특징                  |
| ------------------- | ------- | ------- | ------------------- |
| Steal + Force       | ✅       | ❌       | COMMIT 시 I/O 부담 큼   |
| Steal + No-Force    | ✅       | ✅       | InnoDB 방식, 성능 최적    |
| No-Steal + Force    | ❌       | ❌       | 구현 단순, 현실적으로 불가     |
| No-Steal + No-Force | ❌       | ✅       | Buffer Pool이 무한해야 함 |

## Undo Log
- 변경 전 내역을 저장 (Before Image)
	- 어떤 변경사항으로 되돌릴 것인가?
- 크래시 전 dirty page가 디스크에 flush 되었지만 commit 되지 않은 내역
	- Dirty Page -> Disk 반영 (Flush)
	- Commit 미반영

![[Screenshot 2026-07-07 at 4.41.48 AM.png]]


>[!info] WAL
> Redo / Undo 모두 WAL 기반으로 동작
> - 규칙 1: Data Page 디스크 write 전에 반드시 로그 먼저 write
> - 규칙 2: COMMIT 전에 해당 트랜잭션의 모든 로그 flush 완료

## 결론

| 정책 선택    | 부작용              | 해결책      | 보장         |
| -------- | ---------------- | -------- | ---------- |
| Steal    | 미완료 TX가 .ibd에 반영 | Undo Log | Atomicity  |
| No-Force | 완료 TX가 .ibd에 미반영 | Redo Log | Durability |
- Steal + No-Force = 성능 최적화를 위한 선택 (I/O)
- Undo + Redo = 그 선택의 부작용을 커버