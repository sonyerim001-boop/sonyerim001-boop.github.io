---
title: "프로젝트명"
date: 2026-03-01 12:00:00 +0900
categories: [Portfolio, 보안프로젝트]
tags: [dvwa, burp-suite, sql-injection]
toc: true
math: true
mermaid: true
image:
  path: /assets/img/posts/preview.png
  alt: 프로젝트 미리보기
description: "프로젝트 한 줄 요약."
---

## 프로젝트 개요

프로젝트 설명...

> ⚠️ 본 실습은 허가된 환경에서만 수행해야 함.
{: .prompt-warning }

---

## 실습 환경

| 구분    | 도구       | 버전      |
| ------- | ---------- | --------- |
| 공격 OS | Kali Linux | 2024.1    |
| 대상    | DVWA       | 1.10      |
| 프록시  | Burp Suite | Community |

---

## 구현 과정

### 1단계 - 환경 구성

`/etc/hosts`{: .filepath } 파일 수정 후 진행.

```bash
sudo nmap -sV 192.168.1.1
```
{: .nolineno }

```python
# SQL 인젝션 페이로드
payload = "' OR '1'='1"
```
{: file="exploit.py" }

![](/assets/img/posts/screenshot.png){: w="700" h="400" .shadow }
_실습 화면 캡처_

---

## 취약점 분석 흐름

```mermaid
flowchart LR
    A[취약점 발견] --> B[패치 적용] --> C[재검증] --> D[완료]
```

---

## 수식 활용 (CVSS 점수 계산)

$$ CVSS = \frac{Impact \times Exploitability}{10} $$

---

## 배운 점

- [x] SQL 인젝션 원리 이해
- [x] Burp Suite 활용법
- [ ] 자동화 스크립트 작성
