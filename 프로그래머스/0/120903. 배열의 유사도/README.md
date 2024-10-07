# [level 0] 배열의 유사도 - 120903 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120903?language=python3) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 07일 10:31:51

### 문제 설명

<p>두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 <code>s1</code>과 <code>s2</code>가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 원소의 길이 ≤ 10</li>
<li><code>s1</code>과 <code>s2</code>의 원소는 알파벳 소문자로만 이루어져 있습니다</li>
<li><code>s1</code>과 <code>s2</code>는 각각 중복된 원소를 갖지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s1</th>
<th>s2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["a", "b", "c"]</td>
<td>["com", "b", "d", "p", "c"]</td>
<td>2</td>
</tr>
<tr>
<td>["n", "omg"]</td>
<td>["m", "dot"]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"b"와 "c"가 같으므로 2를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>같은 원소가 없으므로 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `set()` : 집합은 중복된 요소를 허용하지 않으며, 각 요소는 고유하게 유지된다.

### 💻 접근법
인사이트 : 불리언 연산자, 리스트 생성 후 길이를 구하는 것으로 풀이

### 📝 슈도코드
```
def solution(문자열 배열 s1과 s2를 매개변수로 받는다):
    return s1의 요소를 순회하는 i가 s2안에 있는 i를 리스트로 생성, 리스트의 길이를 반환
```
```python
# 풀이 코드 1
def solution(s1, s2):
    return len(list(i for i in s1 if i in s2))
```
```python
# 풀이 코드 2
def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(s1, s2):
    return len(set(s1)&set(s2))
```
- 주어진 두 리스트 s1과 s2를 집합으로 변환하여 교집합을 구하고, 그 교집합의 크기를 반환
- `set()` : 집합은 중복된 요소를 허용하지 않으며, 각 요소는 고유하게 유지된다.
