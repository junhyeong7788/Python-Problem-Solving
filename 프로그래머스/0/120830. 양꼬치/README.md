# [level 0] 양꼬치 - 120830 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120830?language=python3) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 18일 23:08:39

### 문제 설명

<p>머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 <code>n</code>과 <code>k</code>가 매개변수로 주어졌을 때, 양꼬치 <code>n</code>인분과 음료수 <code>k</code>개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>n</code> &lt; 1,000</li>
<li>n / 10 ≤ <code>k</code> &lt; 1,000</li>
<li>서비스로 받은 음료수는 모두 마십니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>3</td>
<td>124,000</td>
</tr>
<tr>
<td>64</td>
<td>6</td>
<td>768,000</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>10인분을 시켜 서비스로 음료수를 하나 받아 총 10 * 12000 + 3 * 2000 - 1 * 2000 = 124,000원입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>64인분을 시켜 서비스로 음료수를 6개 받아 총 64 * 12000 + 6 * 2000 - 6 * 2000 =768,000원입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- if문 한줄 코딩 (삼항연산자) : `if {조건}: 결과` `변수 = A if {조건} else B` `변수 = A if {조건1} else B if {조건2} else C`

### 💻 접근법
인사이트 : if문을 사용하여 풀이하려고 하였다.

### 📝 슈도코드
```
def solution(매개변수 n과 k를 받는다):
    양꼬치 가격의 변수 선언
    음료수 가격의 변수 선언
    지불금액 변수 = 양꼬치 가격 * n + 음료수 가격 * n
    할인금액 변수 = (n//10) * 음료수 가격

    return n이 10이상이면 payment-discount이고 그 외는 payment값을 반환
```
```python
# 풀이 코드 1
def solution(n, k):
    lambSkewers = 12000
    drink = 2000
    count = n//10
    if n >= 10:
        return ((lambSkewers * n) + (drink * k)) - (2000 * count)
    else:
        return ((lambSkewers * n) + (drink * k))
```
```python
# 풀이 코드 2
def solution(n, k):
    lambSkewers = 12000
    drink = 2000
    payment = (lambSkewers * n) + (drink * k)
    discount = (n//10) * drink
    
    return payment-discount if n >= 10 else payment
```

### 👍 다른 정답 코드
1.
```python
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)
```
- 내가 풀이한 코드는 변수를 정의하고 계산을 단계별로 나누어 수행하므로, 전체적인 로직이 명확하게 드러난다. (유지보수나 디버깅에 용이)
- 다른 정답 코드는 코드의 의도를 한눈에 파악하기 어렵다. 매우 간결하다. 메모리 사용 측면에서 조금 더 효율적이다. (최적화가 잘되어있고 수행속도가 빠름) 
