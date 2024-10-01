# [level 0] flag에 따라 다른 값 반환하기 - 181933 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181933) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 02일 00:58:46

### 문제 설명

<p>두 정수 <code>a</code>, <code>b</code>와 boolean 변수 <code>flag</code>가 매개변수로 주어질 때, <code>flag</code>가 true면 <code>a</code> + <code>b</code>를 false면 <code>a</code> - <code>b</code>를 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>-1,000 ≤ <code>a</code>, <code>b</code> ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>a</th>
<th>b</th>
<th>flag</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>-4</td>
<td>7</td>
<td>true</td>
<td>3</td>
</tr>
<tr>
<td>-4</td>
<td>7</td>
<td>false</td>
<td>-11</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번에서 <code>flag</code>가 true이므로 <code>a</code> + <code>b</code> = (-4) + 7 = 3을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번에서 <code>flag</code>가 false이므로 <code>a</code> - <code>b</code> = (-4) - 7 = -11을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `lambda()`

### 💻 접근법
인사이트 : 불리언 변수 flag의 값이 1일때 참으로 평가, 그 외의 값일때 거짓으로 평가하게 하여 풀이하였다.

### 📝 슈도코드
```
def solution(두 정수 a,b 와 불리언 변수 flag를 매개변수로 받는다):
    return flag가 1(true)일때 a + b를 반환하고 false일때 a-b를 반환
```
```python
# 풀이 코드
def solution(a, b, flag):
    return a + b if flag == 1 else a - b
```

### 👍 다른 정답 코드
1.
```python
def solution(a, b, flag):
    return a + b if flag else a - b
```
- `if flag`: flag 자체의 진리성을 평가한다. 0이 아닌 값(불리언 등)은 모두 참으로 간주
2.
```python
solution=lambda a,b,f:[a-b,a+b][f]
```
- `[f]`: f는 리스트의 인덱스로 사용됨, f가 0이면 a-b, f가 1이면 a+b를 선택한다.
- 리스트 인덱싱을 통해 간단하게 조건에 따라 다른 연산 결과를 반환한 풀이
