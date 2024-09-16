# [level 0] 문자 리스트를 문자열로 변환하기 - 181941 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181941) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 16일 17:19:31

### 문제 설명

<p>문자들이 담겨있는 배열 <code>arr</code>가 주어집니다. <code>arr</code>의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>arr</code>의 길이 ≤ 200

<ul>
<li><code>arr</code>의 원소는 전부 알파벳 소문자로 이루어진 길이가 1인 문자열입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["a","b","c"]</td>
<td>"abc"</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `.join()` : 리스트 내에 문자들만 있는 경우나 숫자가 섞여있는 경우에 해당 리스트를 문자열로 변환할 수 있는 방법

### 💻 접근법
인사이트 : `.join` 함수 사용, 처음에는 for loop으로 풀이하려고 하였다.

### 📝 슈도코드
```
def solution(매개변수로 arr를 받는다):
    빈 문자열에 리스트 arr의 모든 요소를 이어 붙인다. (하나의 문자열로 결합)
    return answer을 반환
```
```python
# 풀이 코드
def solution(arr):
    answer = ''.join(arr)
    return answer
```
```python
def solution(arr):
    return ''.join(arr)
```

### 👍 다른 정답 코드
1.
```python
def solution(arr):
    answer = ''
    for i in arr:
        answer = answer + i  # answer += i
    return answer
```
