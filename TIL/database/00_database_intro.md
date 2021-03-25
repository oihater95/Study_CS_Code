# Database

## 1. Database

> 여러 사람이 공유하여 사용할 목적으로 체계화하여 관리하는 데이터의 집합

- RDB 관계형 데이터베이스

  - SQLite, MySQL, ORACLE, PostgreSQL

- NoSQL: 전통적인 RDBMS와 달리 유여한 스키마를 가진 데이터베이스

  - mongoDB, redis, cassandra

  

## 2. RDB (관계형 데이터베이스)

> 관계형 모델을 기반으로 하는 전통적인 데이터베이스

- 여러 사람이 동시에 수정할 수 있는 거대한 스프레드 시트의 집합
- **RDBMS(Relational Database Management System)**:  관계형 데이터베이스를 생성하고 수정하고 관리하는 시스템
- **스키마(schema)**: 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술한 것
- **테이블(table)**: 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
- **컬럼(column)**: 고유한 데이터 형식이 지정되는 열
- **레코드(record)**: 단일 구조 데이터 항목을 가리키는 행
- **기본키(primary key)**: 각 행의 고유 값



## 3. SQL 문법

### 데이터 정의 언어 DDL

- CREATE : 테이블 생성
- DROP : 테이블 삭제 (테이블 자체가 삭제됨)
- ALTER
- TRUNCATE



### 데이터 조작 언어 DML

- SELECT:  데이터 선택
- INSERT: 테이블에 데이터 삽입
- UPDATE: 테이블의 데이터 수정
- DELETE: 테이블 내 데이터 삭제



### 데이터 제어 언어 DCL

- GRANT
- REVOKE
- CONNECT
- SELECT
- INSERT
- UPDATE
- DELETE
- USAGE



## 4. SQLite

bash창에서 명령어로 바로 써도 되지만 기록이 남지 않고 오타에 취약하므로 파일로 만들어서 read

```sqlite
$ sqlite3 tutorial.sqlite3
sqlite> ;
sqlite> .databases
sqlite> .mode csv
sqlite> .import hellodb.csv examples  -- examples table생성
sqlite> .read ./03_select.sql
```



### Create

- Table 생성 

- CREATE

```sql
-- 변수명은 소문자, 명령어는 대문자
-- 테이블 생성
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- id 자동으로 하나씩 올라감
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

```

- PRIMARY KEY를 안쓰고 AUTOINCREMENT만 쓰면 row_id => 데이터 삭제 시 재활용





### Delete

#### Table 전체 삭제

- DROP

```sql
-- Table 삭제
DROP TABLE classmates;
```



#### Table 내 데이터 삭제

- DELETE 

```sql
-- row 삭제
DELETE FROM classmates WHERE id=1;  -- id=1인 row 삭제

-- table내 데이터 전체 삭제 => table은 남아있으므로 이 뒤에 INSERT해도 id(PRIMARY KEY)는 재활용하지 않음
DELETE FROM classmates
```





### Insert

- Table에 데이터 넣기

- INSERT

```sql
-- 한줄로 써도 되지만 가독성 고려 엔터
INSERT INTO classmates (name, age, address)
VALUES 
('홍길동', 25, '서울'),
('김길동', 26, '부산'),
('박길동', 27, '경기'),
('문길동', 28, '강원'),
('최길동', 30, '인천');
```



### Read

- SELECT

```sql
-- 전체 조회 (* col)
SELECT * FROM classmates;

-- 컬럼 지정 조회
SELECT name, address FROM classmates;

-- 개수 제한(지정)
SELECT id, name FROM classmates LIMIT 1; -- id, name 1개씩만

-- from LIMIT N OFFSET M (M+1번째 부터 N 개 순서 중요)
SELECT id, name FROM classmates LIMIT 2 OFFSET 2;
>>>
1|홍길동|25|서울
2|김길동|26|부산
3|박길동|27|경기
4|문길동|28|강원
5|최길동|30|인천
홍길동|서울
김길동|부산
박길동|경기
문길동|강원
최길동|인천
1|홍길동
3|박길동
4|문길동
```



- WHERE

```sql
-- 해당 값을 가진 데이터 가져오기
SELECT id, name FROM classmates
WHERE address='경기';

-- 나이의 값을 가져오기 (중복없이)
SELECT DISTINCT age FROM classmates;

>>> 
3|박길동
25
26
27
28
30
```



### Update

- UPDATE, SET, WHERE

```sql
-- 순서 주의 바꿀 내용(SET)을 먼저 쓰고 바꿀 위치(WHERE)을 나중에 씀
UPDATE classmates
SET name='Mr.Moon', address='경기', age=27
WHERE id=4
;
```



### Practice

```sqlite
sqlite> .mode csv
sqlite> .import users.csv users
```



#### 특정 조건에 맞는 레코드 가져오기

- `SELECT`로 데이터 가져오고 `WHERE`로 조건 설정

- WHERE, AND, OR

```sql
-- users에서 age 30 이상 가져오기
SELECT * FROM users  --모두 가져오기
WHERE age >= 30;  -- age>=30 이면 가져오기

-- 나이 30이상인 사람의 first name만 가져오기
SELECT first_name, last_name FROM users  
WHERE age >= 30;

-- 나이가 30이상이고 성이 김인 사람 겨져오기
SELECT age, last_name FROM users
WHERE age >= 30 AND last_name='김';

-- 나이가 30이상이거나 성이 김인 사람 겨져오기
SELECT age, last_name FROM users
WHERE age >= 30 OR last_name='김';
```



- COUNT(개수), AVG(평균), SUM(평균)

```sql
-- users 레코드의 개수, COUNT
SELECT COUNT(*) FROM users;

-- 30살 이상인 사람 평균 나이
SELECT AVG(age) FROM users
WHERE age >= 30;

-- 계좌 잔액이 가장 높은 사람의 액수와 이름, 해당 레코드만 가져올 땐 WHERE안써도 됨
SELECT country, first_name, MAX(balance) FROM users;

-- 전체 계좌 잔액
SELECT SUM(blance), COUNT(*), AVG(balance) FROM users; 
```



- LIKE

```sql
-- 나이 20이상 30미만 20대
SELECT * FROM users
WHERE age >= 20 and age < 30;

-- 값의 비교가 아닌 패턴의 비교 (LIKE)
-- 20대, 2_ => 2다음에 한자리만
SELECT * FROM users
WHERE age LIKE '2_';

-- 지역번호 02, 02-% => 02-다음에 어떤것이든 올 수 있음, 아무것도 안와도 가능
SELECT phone, country FROM users
WHERE phone LIKE '02-%';

-- 준으로 끝나는 사람의 이름 가져오기
SELECT first_name FROM users
WHERE first_name LIKE '%준';

-- 박씨 이면서 준으로 끝나는 사람의 이름 가져오기
SELECT last_name, first_name FROM users
WHERE first_name LIKE '%준' AND last_name LIKE '박';

-- 전화번호 중간 번호가 5114인 사람만
SELECT phone From users
WHERE phone LIKE '%-5114-%';
```



#### 정렬(ORDER)

- `ORDER BY`

- `ASC`: 오름차순 (default)
- `DESC`: 내림차순

```sql
-- 준으로 끝나는 사람중 마지막사람 이름 가져오기, DESC = 내림차순
SELECT first_name FROM users 
ORDER BY blance DESC LIMIT 1;

-- 나이순으로 오름차순 정렬하여 상위 10개만 출력, ASC = 오름차순
SELECT * From users
ORDER BY age ASC LIMIT 10;

-- 나이 + 성으로 오름차순 정렬 상위 10개 => 순서 필요
-- age, last_name 순서 => 나이가 어린 사람들 중에서 이름 순
-- last_name, age 순서 => 이름 순 정렬 기준에서 나이 순으로 정렬
SELECT * From users
ORDER BY age, last_name ASC LIMIT 10;

-- 계좌 잔액 순으로 내림차순 정렬하여 상위 10명 성과 이름 출력
SELECT first_name, last_name FROM users
ORDER BY blance DESC LIMIT 10;
```



#### 그룹화(Group)

- `GROUP BY`

```sql
-- 어떤 성씨가 있는 지, 가나다 순 배열
SELECT last_name FROM users
GROUP BY last_name;

-- 어떤 성씨가 있는 지, DB에 있는 순서대로(중복 제거)
SELECT DISTINCT last_name FROM users;

-- 각 성씨가 몇 명 있는지
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;  -- last_name이 같은 사람들만 따로 집합으로 빼서 COUNT


-- 각 성씨가 몇 명 있는지, 컬럼명 변경
SELECT last_name, COUNT(*) AS name_count
FROM users
GROUP BY last_name; 
```



