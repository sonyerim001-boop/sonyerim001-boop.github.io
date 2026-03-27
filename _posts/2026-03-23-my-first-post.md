---
title: "내 첫 Chirpy 글"
date: 2026-03-23 12:00:00 +0900
categories: [Blog, Practice]
tags: [chirpy, test]
toc: 
math: true                 
mermaid: true                 
pin: false   
comments: true
description: "테스트 글입니다."
image:
  path: /assets/img/posts/preview.png
  alt: 미리보기 이미지 설명
---
# H1 제목 (가장 큼 - 포스트 제목으로 자동 사용)
## H2 제목 (섹션 구분)
### H3 제목 (소제목)
#### H4 제목 (세부 항목)

**굵게**
*기울임*
~~취소선~~
**_굵게 + 기울임_**
`인라인 코드`

- 항목 1
- 항목 2
  - 하위 항목 (스페이스 2칸)
  - 하위 항목*
  
1. 첫 번째
2. 두 번째
3. 세 번째

- [x] 완료된 항목
- [ ] 미완료 항목
- [x] GitHub Pages 설정
- [ ] 포트폴리오 작성
  
Nmap
: 네트워크 스캐닝 도구. 포트 스캔 및 서비스 탐지에 사용.

Burp Suite
: 웹 취약점 분석 도구. HTTP 트래픽을 프록시로 분석.

DVWA
: 웹 해킹 실습용 취약한 웹 애플리케이션.

> 이것은 기본 인용문임.

> 팁 내용을 여기에 작성.
{: .prompt-tip }

> 정보 내용을 여기에 작성.
{: .prompt-info }

> 주의 내용을 여기에 작성.
{: .prompt-warning }

> 위험 내용을 여기에 작성.
{: .prompt-danger }

| 항목       | 내용         | 비고           |
| ---------- | ------------ | -------------- |
| Kali Linux | 모의해킹 OS  | 무료           |
| Burp Suite | 웹 분석 도구 | Community 무료 |
| DVWA       | 실습 환경    | 오픈소스       |

| 왼쪽 정렬 | 가운데 정렬 | 오른쪽 정렬 |
| :-------- | :---------: | ----------: |
| 내용      |    내용     |        내용 |

[GitHub](https://github.com/sonyermim001-boop)
[내 블로그](https://sonyermim001-boop.github.io)

보안 취약점[^1]은 반드시 패치해야 함.
CVSS[^2] 점수가 높을수록 위험도가 높음.

[^1]: 소프트웨어나 시스템의 약점으로 공격자가 악용할 수 있는 결함.
[^2]: Common Vulnerability Scoring System, 취약점 심각도 평가 지표.

```python
def scan_ports(host):
    for port in range(1, 1025):
        print(f"Scanning port {port}")
        
---

```md id="file01"
```python
print("Hello Security!")

---

```md id="noln01"
```bash
echo 'No line numbers!'

---

```md id="path01"
`/etc/passwd`{: .filepath }
`_config.yml`{: .filepath }
`C:\work\20240001_project`{: .filepath }

![](/assets/img/posts/screenshot.png)
_이미지 아래 캡션 텍스트_

![](/assets/img/posts/screenshot.png){: w="700" h="400" }

![](/assets/img/posts/screenshot.png){: .shadow }

![라이트모드용](/assets/img/posts/light.png){: .light }
![다크모드용](/assets/img/posts/dark.png){: .dark }

---
media_subpath: /assets/img/posts/
---

![](screenshot.png)
_캡션_

---
image:
  path: /assets/img/posts/preview.png
  alt: 이미지 설명
---

<iframe
  class="embed-video"
  loading="lazy"
  src="https://www.youtube.com/embed/OH73Sg8qLAg"
  title="YouTube video player"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen
></iframe>

