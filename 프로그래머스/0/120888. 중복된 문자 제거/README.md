# [level 0] 중복된 문자 제거 - 120888 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120888) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 11월 10일 21:25:21

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어집니다. <code>my_string</code>에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code> ≤ 110</li>
<li><code>my_string</code>은 대문자, 소문자, 공백으로 구성되어 있습니다.</li>
<li>대문자와 소문자를 구분합니다.</li>
<li>공백(" ")도 하나의 문자로 구분합니다.</li>
<li>중복된 문자 중 가장 앞에 있는 문자를 남깁니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"people"</td>
<td>"peol"</td>
</tr>
<tr>
<td>"We are the world"</td>
<td>"We arthwold"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"people"에서 중복된 문자 "p"와 "e"을 제거한 "peol"을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"We are the world"에서 중복된 문자 "e", " ", "r" 들을 제거한 "We arthwold"을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `''.join` : 리스트나 딕셔너리의 키와 같은 이터러블 객체를 하나의 문자열로 합치는 함수
- `dict.fromkeys()` : 중복을 제거한 후 입력 순서를 유지한 딕셔너리를 생성

### 📝 슈도코드
```
def solution(문자열 my_string을 매개변수로 받는다):
    unique_chars = my_string의 문자들을 키로 가지는 딕셔너리 생성(원래 순서 유지)
    result = unique_chars의 모든 키를 하나의 문자열로 결합
    return result반환
```
```python
# 풀이 코드
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
```
- `dict.fromkeys(my_string)`: 전달된 키들로 구성된 딕셔너리를 생성하는 메서드
    - my_styring 문자열의 각 문자를 키로 하는 딕셔너리를 생성하여, 중복된 문자는 하나만 남기고 제거하는 효과가 있다.

```python
# 코드 풀어쓰기
def solution(my_string):
    # Step 1: 중복 제거를 위해 딕셔너리 생성
    unique_chars = dict.fromkeys(my_string)
    
    # Step 2: 딕셔너리의 키를 문자열로 결합하여 반환
    result = ''.join(unique_chars)
    
    return result
```
- my_string이 hello라면 `unique_chars의 값 : {'h' : None, 'e' : None, 'l' : None, 'o' : None}`

### 👍 다른 정답 코드
1.
```python
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer
```
- answer에 i의 값이 없으면 answer 문자열에 추가.


