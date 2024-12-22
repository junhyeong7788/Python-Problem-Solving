# [level 1] 문자열 내 마음대로 정렬하기 - 12915 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12915?language=python3) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 22일 20:49:11

### 문제 설명

<p>문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.</p>

<h5>제한 조건</h5>

<ul>
<li>strings는 길이 1 이상, 50이하인 배열입니다.</li>
<li>strings의 원소는 소문자 알파벳으로 이루어져 있습니다.</li>
<li>strings의 원소는 길이 1 이상, 100이하인 문자열입니다.</li>
<li>모든 strings의 원소의 길이는 n보다 큽니다.</li>
<li>인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>strings</th>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>["sun", "bed", "car"]</td>
<td>1</td>
<td>["car", "bed", "sun"]</td>
</tr>
<tr>
<td>["abce", "abcd", "cdx"]</td>
<td>2</td>
<td>["abcd", "abce", "cdx"]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p><strong>입출력 예 1</strong><br>
"sun", "bed", "car"의 1번째 인덱스 값은 각각 "u", "e", "a" 입니다. 이를 기준으로 strings를 정렬하면 ["car", "bed", "sun"] 입니다.</p>

<p><strong>입출력 예 2</strong><br>
"abce"와 "abcd", "cdx"의 2번째 인덱스 값은 "c", "c", "x"입니다. 따라서 정렬 후에는 "cdx"가 가장 뒤에 위치합니다. "abce"와 "abcd"는 사전순으로 정렬하면 "abcd"가 우선하므로, 답은 ["abcd", "abce", "cdx"] 입니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `lambda 함수`
- `sorted(iterable, key=None)` : 반복 가능한 객체를 정렬하여 새로운 리스트를 반환
    - key : 정렬 기준을 지정한느 함수, 각 '요소에 대해 호출되어 반환된 값을 기준으로 정렬 (기본 : 오름차순)

### 📝 슈도코드
```
def solution(매개변수 리스트 strings와 정수 n을 받음):
    return 정렬, 새로운 리스트 생성 (strings, key값은 strings 의 각 요소(문자열)의 n번째 문자를 기준으로 정렬)
```
```python
# 풀이 코드
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
```
- `x[n]` : 각 문자열의 n번째 문자를 기준으로 정렬
- `x`: n번째 문자가 동일할 경우, 문자열 자체를 사전순으로 정렬
