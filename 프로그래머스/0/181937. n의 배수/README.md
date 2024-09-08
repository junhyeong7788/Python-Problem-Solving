# [level 0] n의 배수 - 181937 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181937) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 08일 22:38:28

### 문제 설명

<p>정수 <code>num</code>과 <code>n</code>이 매개 변수로 주어질 때, <code>num</code>이 <code>n</code>의 배수이면 1을 return <code>n</code>의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>num</code> ≤ 100</li>
<li>2 ≤ <code>n</code> ≤ 9</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>98</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>34</td>
<td>3</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>98은 2의 배수이므로 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>32는 3의 배수가 아니므로 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `lambda함수`, `num이 n의 배수 : num % n == 0`

### 💻 접근법
인사이트 : 정수 num이 n의 배수인지 확인하려면 num을 n으로 나눴을 때 나머지는 0 이여야한다.

### 📝 슈도코드
```
def solution함수 (num, n):
    answer변수를 0으로 생성
    if num을 n으로 나눴을 때 나머지가 0과 같다
        answer는 1
    그 외:
        answer는 0
    return answer변수
```

```python
# 풀이 코드
def solution(num, n):
    answer = 0
    if num % n == 0 :
        answer = 1
    else :
        answer = 0
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(num, n):
    return int(num % n == 0)
```
```python
def solution(num, n):
    return 1 if num % n == 0 else 0
```
- 가독성과 간결함을 가진 코드

2.
```python
solution = lambda num, n : 1 if num % n == 0 else 0
```
- lambda함수 사용
