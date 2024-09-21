# [level 0] 문자열 뒤집기 - 120822 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120822) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 21일 22:55:19

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어집니다. <code>my_string</code>을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"jaron"</td>
<td>"noraj"</td>
</tr>
<tr>
<td>"bread"</td>
<td>"daerb"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>my_string</code>이 "jaron"이므로 거꾸로 뒤집은 "noraj"를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>my_string</code>이 "bread"이므로 거꾸로 뒤집은 "daerb"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- list slicing : `sequence[start:stop:step]`
- `my_list.reverse()` , `reversed(my_list)`

### 💻 접근법
인사이트 : list slicing

### 📝 슈도코드
```
def solution(매개변수로 문자열 my_string을 받는다):
    return 문자열my_string 처음부터 끝까지 -1 간격으로 리스트 슬라이싱을 반환
```
```python
# 풀이 코드
def solution(my_string):
    return my_string[::-1]
```
- `my_string[::-1]` : 처음부터 끝까지 -1 간격으로 리스트 슬라이싱 = 문자열을 뒤집는다.

### 👍 다른 정답 코드
1.
```python
def solution(my_string):
    answer = ''
    for i in my_string:
        answer = i + answer
    return answer
```
2.
```python
def solution(my_string):
    list_str = list(my_string)
    list_str.reverse()
    answer = ''.join(list_str)
    return answer
```
3.
```python
def solution(my_string):
    list_str = list(reversed(my_string))
    reverse_str = ''.join(list_str)
    return reverse_str
```
- `reverse()` : 호출된 리스트 자체를 변경하며, 반환 값이 없다.
- `reversed()` : 원본은 그대로 두고, 역방향으로 순회할 수 있는 이터레이터를 반환, 원본 데이터 타입에 관계 없이 사용할 수 있다.
