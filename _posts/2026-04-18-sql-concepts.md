---
title: "[데이터베이스] SQL 주관식 핵심 개념 정리 (DDL, GROUP BY, ACID)"
date: 2026-04-18
categories: [Database]
tags: [SQL, MySQL, Database, GROUPBY, HAVING]
---

# SQL 핵심 개념 정리

## 📌 개요  
데이터베이스 이론 문제를 정리하며 SQL의 핵심 개념을 정리하였다.  

---

## 🔍 SQL 명령어 분류  

- DDL: CREATE, DROP, ALTER  
- DML: SELECT  

---

## 🔑 PRIMARY KEY  

- 유일성: 중복 불가  
- NOT NULL: NULL 불가  

---

## 📊 GROUP BY와 HAVING  

- WHERE → 그룹화 이전  
- HAVING → 그룹화 이후  

---

## ⚙ 트랜잭션 ACID  

- Atomicity  
- Consistency  
- Isolation  
- Durability  

---

## 📈 COUNT 함수 차이  

- COUNT(*) → 전체  
- COUNT(column) → NULL 제외  

---

## 🔗 FOREIGN KEY  

- 참조 무결성 유지  

---

## 🔄 SQL 실행 순서  

FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY  

---

## 💡 정리  

SQL은 단순 암기가 아니라 실행 흐름 이해가 중요하다.  

👉 실습 정리 글: ([text](<../../../Users/rkcjs/OneDrive/문서/주관식 문제 250520.docx>))