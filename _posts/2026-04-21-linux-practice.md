---

title: "Ubuntu Linux 실습 20문제 수행 정리 (리눅스 포트폴리오)"
date: 2026-04-21 21:00:00 +0900
categories: [Linux, Portfolio]
tags: [Linux, Ubuntu, Shell, Bash, 실습, 포트폴리오]
toc: true
---

# Ubuntu Linux 실습 20문제 수행 정리 (리눅스 포트폴리오)

보안 실습용 셸 스크립트를 기반으로 Linux 환경을 구성한 뒤,
20개의 실습 문제를 수행하며 핵심 명령어와 시스템 구조를 정리하였다.

---

## 📌 실습 환경

* OS: Ubuntu (VirtualBox)
* 실습 위치: `~/security`
* 사용 도구: Bash Shell
* 학습 범위: 파일 시스템, 권한, 로그 분석, 텍스트 처리

---

## ⚙️ 사전 실습

### 1. wget 설치

```bash
sudo apt update
sudo apt install -y wget
```

---

### 2. 실습 스크립트 다운로드

```bash
cd ~
wget https://raw.githubusercontent.com/sbaek100/security-training/main/setup-script.sh
ls -l setup-script.sh
```

✔ 파일이 정상적으로 다운로드되었는지 확인

---

### 3. 스크립트 실행

```bash
cat setup-script.sh
chmod +x setup-script.sh
./setup-script.sh
```

✔ 실행 후 `~/security` 디렉터리 생성됨

---

### 4. 환경 구조 확인

```bash
sudo apt install -y tree
tree ~/security
```

✔ 실습용 디렉터리 및 파일 구조 확인

---

## 🧪 주요 실습 내용 정리

### 1️⃣ 디렉터리 및 파일 탐색

```bash
pwd
cd ~/security
ls
ls -la
```

* 현재 위치 확인 및 이동
* 숨김 파일 포함 전체 목록 확인

---

### 2️⃣ 파일 내용 및 권한 확인

```bash
cat ~/security/config/sshd_config
ls -l ~/security/scripts
```

* 파일 내용 출력
* 권한 (rwx) 구조 확인

---

### 3️⃣ 로그 및 문자열 검색

```bash
grep "error" ~/security/logs/auth.log
grep -i "failed" ~/security/logs/auth.log
grep -c "root" ~/security/logs/auth.log
```

* 로그 파일에서 특정 문자열 검색
* 발생 횟수 확인

---

### 4️⃣ 텍스트 처리

```bash
awk '{print $1}' ~/security/logs/auth.log
sed 's/error/ERROR/g' ~/security/logs/auth.log
```

* 특정 컬럼 추출
* 문자열 치환

---

### 5️⃣ 파일 검색 및 권한 변경

```bash
find ~/security -name "*.log"
chmod +x ~/security/scripts/*.sh
```

* 파일 탐색
* 실행 권한 부여

---

### 6️⃣ Bash 스크립트 활용

```bash
cat << 'EOF' > ~/security/scripts/check_log.sh
#!/bin/bash
if [ -f ~/security/logs/auth.log ]; then
    echo "[OK] auth.log file exists"
else
    echo "[ERROR] auth.log file does not exist"
fi
EOF

chmod +x ~/security/scripts/check_log.sh
~/security/scripts/check_log.sh
```

✔ 파일 존재 여부 자동 확인 스크립트

---

## 💡 핵심 정리

* Linux는 파일 중심 구조로 모든 작업이 이루어진다.
* `grep`, `awk`, `sed`는 로그 분석의 핵심 도구이다.
* 권한(`rwx`)은 보안과 직접적으로 연결된다.
* Bash 스크립트를 통해 반복 작업을 자동화할 수 있다.

---

## 📝 느낀 점

이번 실습을 통해 단순 명령어 암기가 아니라,
실제 파일과 로그를 기반으로 Linux 시스템을 다루는 방법을 익힐 수 있었다.

특히 로그 분석과 권한 관리의 중요성을 직접 확인할 수 있었고,
Bash 스크립트를 활용한 자동화 과정이 인상적이었다.

앞으로 서버 관리나 보안 분야에서도 활용할 수 있는 기반을 만들었다.

---

👉 [보안시스템 실습](/assets/files/보안시스템 실습.docx)