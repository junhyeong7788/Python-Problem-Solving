# [level 0] 접미사인지 확인하기 - 181908 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181908) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 30일 21:47:05

### 문제 설명

<p>어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.<br>
문자열 <code>my_string</code>과 <code>is_suffix</code>가 주어질 때, <code>is_suffix</code>가 <code>my_string</code>의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>is_suffix</code>의 길이 ≤ 100</li>
<li><code>my_string</code>과 <code>is_suffix</code>는 영소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>is_suffix</th>
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
<td>"nan"</td>
<td>0</td>
</tr>
<tr>
<td>"banana"</td>
<td>"wxyz"</td>
<td>0</td>
</tr>
<tr>
<td>"banana"</td>
<td>"abanana"</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사이기 때문에 1을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>예제 3번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>

<p>입출력 예 #4</p>

<ul>
<li>예제 4번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `endswith()` : 문자열이 특정 접미사로 끝나는지 여부를 확인하는 파이썬 내장 문자열 메서드
- `my_string[-len(is_suffix):]` : 리스트 슬라이싱을 사용하여 my_string의 끝부분에서 is_suffix와 깉이가 같은 부분을 추출

### 💻 접근법
- 문자열 my_string의 모든 접미사를 리스트로 생성한 다음, 특정 문자열 is_suffix가 그 리스트에 포함되어 있는지를 확인

### 📝 슈도코드
```
def solution(문자열 my_string과 문자열 is_suffix를 매개변수로 받는다):
    answer 리스트 변수 선언
    my_string 문자열 길이의 배열을 생성하여 순회한다.
        answer_list변수에 my_syring[i에서부터 끝까지] 값을 순차적으로 저장한다.

    if is_suffix의 값이 answer 리스트에 있다면
        return 1을 반환
    else 없다면
        return 0을 반환
```
```python
# 풀이 코드 1
def solution(my_string, is_suffix):
    answer_list = []
    for i in range(len(my_string)):
        answer_list.append(my_string[i:])
    
    if is_suffix in answer_list:
        return 1
    else:
        return 0
```
```python
# 풀이 코드 2
def solution(my_string, is_suffix):
    answer = [my_string[i:] for i in range(len(my_string))]
    return 1 if is_suffix in answer else 0
```

### 👍 다른 정답 코드
1.
```python
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))
```
- `endswith()` : 문자열이 특정 접미사로 끝나는지 여부를 확인하는 파이썬 내장 문자열 메서드
    - 참 또는 거짓 값을 반환
- `int()` : endswith()의 불리언 값을 정수로 변환한다.
    - `int(my_string.endswith(is_suffix))`는 접미사가 맞을 때 1, 아니면 0을 반환 
2.
```python
def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):]==s: return 1
    return 0
```
- `my_string[-len(is_suffix):]` : 리스트 슬라이싱을 사용하여 my_string의 끝부분에서 is_suffix와 깉이가 같은 부분을 추출
- `-len(is_suffix) : 문자열의 끝에서부터 is_suffix의 길이만큼 거슬러 올라간 인덱스를 의미
    - 예 : `my_string = "hello"`이고 `is_suffix = "lo"`라면, `len(is_suffix)`는 2이므로 `my_string[-2:]`이 "lo"를 반환합니다. 즉, 문자열의 끝 두 문자를 추출
