# [level 1] 자릿수 더하기 - 12931 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12931) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 06일 23:44:40

### 문제 설명

<p>자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.<br>
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.</p>

<h5>제한사항</h5>

<ul>
<li>N의 범위 : 100,000,000 이하의 자연수</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>N</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>123</td>
<td>6</td>
</tr>
<tr>
<td>987</td>
<td>24</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
문제의 예시와 같습니다.</p>

<p>입출력 예 #2<br>
9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- list comprehension, map(), sum()

### 💻 접근법
인사이트 : 자연수 N의 각 자릿수를 배열의 요소로 만들어서 배열의 합을 구하는 방법으로 풀이

### 📝 슈도코드
```
def solution(자연수 N을 매개변수로 받는다):
    return n을 각 자릿수의 문자열을 정수형으로 반환하여 리스트를 생성하고 그 리스트의 각 요소를 모두 더한 값을 반환
```
```python
# 풀이 코드
def solution(n):
    return sum(list(map(int, str(n))))
```
- `map(int, str(n)` : 첫 번째 인자인 함수 int를 두 번째 인자인 반복 가능한 객체(str(n))의 각 요소에 적용
    - ex : `'1', '2', '3'`이라는 문자는 `int('1'), int('2'), int('3')` 을 통해 각각 정수 1,2,3으로 변환

### 👍 다른 정답 코드
1.
```python
def solution(n):
    return sum(int(i) for i in str(n))
```
- 리스트 컴프리헨션으로 풀이
