# [level 0] 문자열 정수의 합 - 181849 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181849?language=python3) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 28일 16:59:43

### 문제 설명

<p>한 자리 정수로 이루어진 문자열 <code>num_str</code>이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>num_str</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_str</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"123456789"</td>
<td>45</td>
</tr>
<tr>
<td>"1000000"</td>
<td>1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>문자열 안의 모든 숫자를 더하면 45가 됩니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>문자열 안의 모든 숫자를 더하면 1이 됩니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `map()`, `sum()`, for loop

### 💻 접근법
인사이트 : string도 iterable한 객체이기에 for loop로 문제풀이

### 📝 슈도코드
```
def solution(한 자리 정수로 이루어진 문자열 num_str를 매개변수로 받는다):
    answer변수를 선언
    for num_str의 문자열 요소를 순회한다:
        answer변수에 각 요소를 int로 변환하여 더한다.
    return answer 변수 반환
```
```python
# 풀이 코드
def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(num_str):
    return sum(map(int, num_str))
```
- `map(funtion, iterable)` : 문자열의 각 문자를 개별적으로 처리(정수로 변환하는 역할)한다.
