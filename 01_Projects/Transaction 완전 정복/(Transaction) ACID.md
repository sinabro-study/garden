## Transaction?
하나 이상의 연산을 하나의 논리적 실행 단위로 묶어 ACID 속성을 보장하는 실행 모델

## ACID?
#### A (Atomicity, 원자성)
- 트랜잭션은 전부 수행 (Commit) 하거나 전부 미수행 (Rollback)

![[Screenshot 2026-06-28 at 7.29.37 AM.png]]

#### C (Consisteny, 일관성)
- 트랜잭션 전후 데이터베이스 제약 조건 유지

| **제약 조건**   | **Consistency 규칙** |
| ----------- | ------------------ |
| primary key | 행을 유일하게 식별         |
| foreign key | 참조 대상이 반드시 존재      |
| unique      | 특정 값은 중복 불가        |
| check       | 지정한 조건 항상 만족       |
| not null    | 반드시 값 존재           |
| trigger     | 정의한 비즈니스 규칙 만족     |

```mysql
####################
# Primary key
####################
create table users (
  id            bigint      primary key,
  name     varchar(20)
);

-- (가능) PK 제약조건 충족
insert into users values (1, 'Abc');
insert into users values (2, 'Zxy');

-- (불가능) PK 제약조건 위반
insert into users values (1, '123');


####################
# Foreign key
####################
create table orders (
  id            bigint      primary key,
 user_id   bigint
 foreign key (user_id) references users(id)
);

-- (가능) FK 제약조건 충족
insert into orders values (1, 1);

-- (불가능) FK 제약조건 위반
insert into orders values (2, 999);  -- 회원 미존재
delete from users where id = 1;      -- 주문 내역 존재


####################
# Unique
####################
create table users (
  id            bigint      primary key,
  email     varchar(20)  unique
);

-- (가능) Unique 제약조건 충족
insert into users values (1, 'a@test.com');
insert into users values (2, 'b@test.com');

-- (불가능) Unique 제약조건 위반
insert into users values (3, 'b@test.com');


####################
# Check
####################
create table stocks (
  id                bigint      primary key,
  quantity     int           check(quantity >= 0)
);

-- (가능) Check 제약조건 충족
insert into stocks values (1, 100);

-- (불가능) Check 제약조건 위반
update stocks set quantity = quantity - 110 where id = 1;


####################
# not null
####################
create table users (
  id            bigint      primary key,
  name     varchar(20) not null
);

-- (가능) not null 제약조건 충족
insert into users values (1, 'Name');

-- (불가능) not null 제약조건 위반
insert into users values (2, null);


####################
# Trigger
####################
create trigger check_balance
before update on account
for each row
begin
    if NEW.balance < 0 then
        signal sqlsate '45000'
        set message_text = 'balance cannot be negative';
    end if;
end;
```


### Isolation
동시에 여러 Transaction 이 수행될 때 충돌을 어디까지 허용할 것인가?

|     |     |
| --- | --- |
|     |     |
