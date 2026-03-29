# Python과 MySQL을 이용한 CSV 데이터 저장 구현



2026-03-29



금채연



---



## 1. 학습목표



▪ Python을 설치하고 실행할 수 있다



▪ MySQL 데이터베이스를 설치하고 사용할 수 있다



▪ CSV 파일 데이터를 Python으로 읽을 수 있다



▪ Python과 MySQL을 연결하여 데이터를 저장할 수 있다



▪ 파일 데이터를 데이터베이스로 저장하는 과정을 이해한다



---



## 2. 목차



1. 개발 환경 준비

2. 데이터베이스 생성

3. 프로젝트 파일 생성

4. Python 코드 작성

5. 프로그램 실행

6. 실행 결과 확인

7. 활용 예시



---



## 3. 개발 환경 준비



### 1) Python 설치



https://www.python.org/downloads/



설치 시 반드시 아래 항목 체크



Add Python to PATH



설치 후 확인



```bash

python --version

```



### 2) MySQL 설치



https://dev.mysql.com/downloads/installer/



설치 시 설정



▪ Setup Type: Custom



▪ MySQL Server + MySQL Workbench 선택



▪ root 비밀번호 설정 (예: 1234)



### 3) 라이브러리 설치



명령 프롬프트(cmd)에서 실행



```bash

pip install pandas pymysql

```



## 4. 데이터베이스 생성



```bash

"C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe" -u root -p

```



다음 SQL 입력



```sql

CREATE DATABASE tutorial_db;

USE tutorial_db;



CREATE TABLE orders (

id INT AUTO\_INCREMENT PRIMARY KEY,

product VARCHAR(100),

price INT

);

```



---



## 5. 프로젝트 파일 생성



### 1) 폴더 생성



```bash

mkdir csv-to-mysql

cd csv-to-mysql

```



### 2) CSV 파일 생성



파일명: orders.csv



```csv

product,price

Notebook,1200

Pen,500

Pencil,300

Eraser,200

```



### 3) Python 파일 생성



파일명: main.py



---



## 6. Python 코드 작성



```python

import pandas as pd

import pymysql



data = pd.read_csv("orders.csv")



conn = pymysql.connect(

host="localhost",

user="root",

password="1234",

database="tutorial_db"

)



cursor = conn.cursor()



for _, row in data.iterrows():

sql = "INSERT INTO orders (product, price) VALUES (%s, %s)"

cursor.execute(sql, (row["product"], row["price"]))



conn.commit()

conn.close()



print("데이터 저장 완료")

```



---



## 7. 코드 설명



### 1) CSV 파일 읽기

- CSV 데이터를 Python에서 사용할 수 있는 형태로 변환한다.



```python

data = pd.read_csv("orders.csv")

```



### 2) 데이터베이스 연결

- Python 프로그램과 MySQL을 연결한다.



```python

conn = pymysql.connect(

host="localhost",

user="root",

password="1234",

database="tutorial_db"

)

```



### 3) 데이터 저장

- 각 행의 데이터를 반복하여 DB에 저장한다.



```python

cursor = conn.cursor()



for _, row in data.iterrows():

sql = "INSERT INTO orders (product, price) VALUES (%s, %s)"

cursor.execute(sql, (row["product"], row["price"]))

```



### 4) 저장 반영

- 데이터를 실제 DB에 반영한다.



```python

conn.commit()

```



### 5) 연결 종료

- DB 연결을 종료한다.



```python

conn.close()

```



---



## 8. 프로그램 실행



```bash

python main.py

```



---



## 9. 실행 결과



```text

데이터 저장 완료

```



---



## 10. 데이터 확인



MySQL 실행



```bash

"C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe" -u root -p

```



```sql

USE tutorial\_db;

SELECT * FROM orders;

```



```text

+----+----------+-------+

| id | product  | price |

+----+----------+-------+

|  1 | Notebook |  1200 |

|  2 | Pen      |   500 |

|  3 | Pencil   |   300 |

|  4 | Eraser   |   200 |

+----+----------+-------+

```



---



## 11. 전체 흐름 정리



CSV 파일 → Python → MySQL DB



---



## 12. 활용 예시



▪ 회원 데이터 저장



▪ 설문조사 결과 저장



▪ 크롤링 데이터 저장



▪ 주문 데이터 저장



▪ 공공데이터 파일 저장



---



## 13. 주의사항



▪ MySQL 비밀번호는 Python 코드와 동일해야 한다.



▪ CSV 파일과 Python 파일은 같은 폴더에 있어야 한다.



▪ 프로그램을 여러 번 실행하면 데이터가 중복 저장된다.



---



## 14. 결론



본 자료를 통해 CSV 데이터를 Python으로 처리하고 MySQL 데이터베이스에 저장하는 과정을 직접 구현할 수 있으며,

이 기술은 다양한 프로젝트에서 데이터 저장 기능 구현에 활용될 수 있다.

