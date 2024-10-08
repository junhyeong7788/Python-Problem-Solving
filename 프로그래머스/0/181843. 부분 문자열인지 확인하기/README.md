# [level 0] 부분 문자열인지 확인하기 - 181843 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181843) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 08일 20:28:14

### 문제 설명

<p>부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다. 예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만, "aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.</p>

<p>문자열 <code>my_string</code>과 <code>target</code>이 매개변수로 주어질 때, <code>target</code>이 문자열 <code>my_string</code>의 부분 문자열이라면 1을, 아니라면 0을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>my_string</code>은 영소문자로만 이루어져 있습니다.</li>
<li>1 ≤ <code>target</code>의 길이 ≤ 100</li>
<li><code>target</code>은 영소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>target</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"banana"</td>
<td>"ana"</td>
<td>1</td>
</tr>
<tr>
<td>"banana"</td>
<td>"wxyz"</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>문제 설명과 같습니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>문제 설명과 같습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `int()`

### 💻 접근법
인사이트 : 불리안 연산자를 사용하여 문자열 내에 부분 문자열이 있는지 여부를 반환

### 📝 슈도코드
```
def solution(문자열 my_string과 target를 매개변수로 받는다):
    return my_string안에 target문자열이 있으면 1 반환 없으면 0 반환
```
```python
# 풀이 코드
def solution(my_string, target):
    return 1 if target in my_string else 0
```
```python
def solution(my_string, target):
    if target in my_string:
        return 1
    else: 
        return 0
```

### 👍 다른 정답 코드
1.
```python
def solution(my_string, target):
    return int(target in my_string)
```
- `int()`와 불리안 연산자를 사용하여 True값은 1로 False값은 0으로 바꾼 값을 반환한다.
