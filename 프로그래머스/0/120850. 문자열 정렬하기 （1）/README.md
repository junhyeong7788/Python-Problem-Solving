# [level 0] 문자열 정렬하기 (1) - 120850 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120850) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 09일 20:34:31

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어질 때, <code>my_string</code> 안에 있는 숫자만 골라 오름차순 정렬한 리스트를&nbsp;return 하도록 solution 함수를 작성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>my_string</code>에는 숫자가 한 개 이상 포함되어 있습니다.</li>
<li><code>my_string</code>은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다.
- - -</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"hi12392"</td>
<td>[1, 2, 2, 3, 9]</td>
</tr>
<tr>
<td>"p2o4i8gj2"</td>
<td>[2, 2, 4, 8]</td>
</tr>
<tr>
<td>"abcde0"</td>
<td>[0]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"hi12392"에 있는 숫자 1, 2, 3, 9, 2를 오름차순 정렬한 [1, 2, 2, 3, 9]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"p2o4i8gj2"에 있는 숫자 2, 4, 8, 2를 오름차순 정렬한 [2, 2, 4, 8]을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"abcde0"에 있는 숫자 0을 오름차순 정렬한 [0]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `isdigit()` : 파이썬의 문자열 메서드 중 하나, 문자열이 숫자로만 구성되어 있는지 확인하는 데 사용
    - 숫자외에 다른 문자가 포함되어 있으면 False를 반환, 0~9로만 이루어져 있을 때 True를 반환
- `filter(lambda s: s.isdigit(), my_string)` : my_string에서 숫자인 문자들만 추출하여 반환
    - filter함수는 특정 조건을 만족하는 요소들만 추출하여 반환하는 함수

### 💻 접근법
인사이트 : 메서드 생각이 안나 `문자열내 숫자요소 찾는 함수`를 구글링해서 풀이

### 📝 슈도코드
```
def solution(문자열 my_string을 매개변수로 받는다):
    return 문자열 요소를 순회, 만약에 i가 숫자이면: int(i)로 리스트 생성, 리스트 정렬된 값을 반환한다.
```
```python
def solution(my_string):
    return sorted(int(i) for i in my_string if i.isdigit())
```
```python
# 풀이 코드
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    return sorted(answer)
```

### 👍 다른 정답 코드
1.
```python
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))
```
- `filter(lambda s: s.isdigit(), my_string)` : my_string에서 숫자인 문자들만 추출하여 반환
    - filter함수는 특정 조건을 만족하는 요소들만 추출하여 반환하는 함수
- `map(int, ...)`: `filter()`로 추출된 숫자 형태의 문자들을 실제 정수형으로 변환
