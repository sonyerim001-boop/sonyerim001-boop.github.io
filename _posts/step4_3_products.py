import mysql.connector

# ① DB 연결
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qhdrbs0511!",
    database="key_db",
    charset="utf8mb4"
)
cursor = conn.cursor()
print("DB 연결 성공!")

# ② 학생 목록 조회
print("\n[학생 목록]")
cursor.execute("SELECT id, name FROM students")
for row in cursor.fetchall():
    print(f"  번호: {row[0]}, 이름: {row[1]}")

# ③ 두 테이블 연결해서 점수 조회
print("\n[학생별 점수]")
sql = """
SELECT students.name, scores.subject, scores.score
FROM scores
WHERE scores.student_id = students.id
"""
cursor.execute(sql)
for row in cursor.fetchall():
    print(f"  {row[0]} | {row[1]} | {row[2]}점")

# ④ 연결 종료
cursor.close()
conn.close()
print("\n프로그램 종료")
