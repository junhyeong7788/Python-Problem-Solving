# [level 0] 글자 이어 붙여 문자열 만들기 - 181915 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181915) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.08 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 22일 23:47:43

### 문제 설명

<p>문자열 <code>my_string</code>과 정수 배열 <code>index_list</code>가 매개변수로 주어집니다. <code>my_string</code>의 <code>index_list</code>의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
<li><code>my_string</code>의 원소는 영소문자로 이루어져 있습니다.</li>
<li>1 ≤ <code>index_list</code>의 길이 ≤ 1,000</li>
<li>0 ≤ <code>index_list</code>의 원소 &lt; <code>my_string</code>의 길이</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>index_list</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"cvsgiorszzzmrpaqpe"</td>
<td>[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]</td>
<td>"programmers"</td>
</tr>
<tr>
<td>"zpiaz"</td>
<td>[1, 2, 0, 0, 3]</td>
<td>"pizza"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>my_string</code>에서 인덱스 3, 5, 6, 11, 12, 14, 16, 17에 해당하는 글자는 각각 g, o, r, m, r, a, p, e이므로 <code>my_string</code>에서 <code>index_list</code>에 들어있는 원소에 해당하는 인덱스의 글자들은 각각 순서대로 p, r, o, g, r, a, m, m, e, r, s입니다. 따라서 "programmers"를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>my_string</code>에서 인덱스 0, 1, 2, 3에 해당하는 글자는 각각 z, p, i, a이므로 <code>my_string</code>에서 <code>index_list</code>에 들어있는 원소에 해당하는 인덱스의 글자들은 각각 순서대로 p, i, z, z, a입니다. 따라서 "pizza"를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- list indexing
- list comprehension
- `''.join()`

### 💻 접근법
인사이트 : for loop, list indexing으로 해결가능

### 📝 슈도코드
```
def solution(문자열my_string과 정수 배열index_list를 매개변수로 받는다.):
    answer 문자열 변수 선언 = ''
    for i in 정수배열 index_list를 순회한다:
        answer변수 = answer변수 + my_string[i]를 순차적으로 더한다.
    return 문자열이 저장된 answer변수 반환
```
```python
# 풀이 코드
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])
```
- index_list의 각 요소 i를 순회하면서, my_string[i]를 통해 my_string의 해당 인덱스에 있는 문자 선택
- `''.join()` : 리스트 컴프리헨션을 통해 생성된 문자 리스트를 하나의 문자열로 결합한다.
