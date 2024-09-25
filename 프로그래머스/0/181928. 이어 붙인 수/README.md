# [level 0] 이어 붙인 수 - 181928 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181928) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 25일 23:49:14

### 문제 설명

<p>정수가 담긴 리스트 <code>num_list</code>가 주어집니다. <code>num_list</code>의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>num_list</code>의 길이 ≤ 10</li>
<li>1 ≤ <code>num_list</code>의 원소 ≤ 9</li>
<li><code>num_list</code>에는 적어도 한 개씩의 짝수와 홀수가 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[3, 4, 5, 2, 1]</td>
<td>393</td>
</tr>
<tr>
<td>[5, 7, 8, 3]</td>
<td>581</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>홀수만 이어 붙인 수는 351이고 짝수만 이어 붙인 수는 42입니다. 두 수의 합은 393입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>홀수만 이어 붙인 수는 573이고 짝수만 이어 붙인 수는 8입니다. 두 수의 합은 581입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `map(funtion, iterable)` : 시퀀스의 각 요소에 지정된 함수를 적용하여 그 결과를 반환하는 함수
    - function : 각 요소에 적용할 함수
    - iterable : 함수가 적용될 시퀀스 또는 반복 가능한 객체

### 💻 접근법
인사이트 : for loop와 if문을 사용하여 짝수리스트와 홀수리스트를 만들어 join으로 결합 후 합을 구하여 풀이하려고 생각

### 🚫 문제해결 중 발생한 에러
- `TypeError: sequence item 0: expected str instance, int found ` : 파이썬에서 리스트나 튜플과 같은 시퀀스를 문자열로 변환하려고 할 때, 그 시퀀스 안에 숫자형(int)이 포함되어 있어서 발생하는 오류
    - 해결 : 숫자를 문자열로 변환해주면 오류 해결 (`int(''.join(map(str, even_num)))`)

### 📝 슈도코드
```
def solution(정수가 담긴 리스트 num_list를 매개변수롤 받는다):
    홀수 리스트 변수 선언
    짝수 리스트 변수 선언

    for num_list의 요소를 순회한다:
        if i가 짝수일때:
            짝수 리스트 변수에 i를 추가한다.
        else i가 홀수일떄:
            홀수 리스트 변수에 i를 추가한다.
    return 짝수리스트 내 요소를 문자열로 반환 후 문자열을 하나의 숫자 형태로 join한 후 정수형으로 변환 + 홀수 리스트 내 요소를 문자열로 반환한 후 문자열을 하나의 숫자형태로 join한 후 정수형으로 변환
```
```python
# 풀이 코드 1
def solution(num_list): 
    odd_num = []
    even_num = []

    for i in num_list:
        if i % 2 == 0:
            even_num.append(i)
        else :
            odd_num.append(i)

    return int(''.join(map(str, even_num))) + int(''.join(map(str, odd_num)))
```
```python
# 풀이 코드 2
def solution(num_list): 
    odd_num = [i for i in num_list if i%2 == 1]
    even_num = [i for i in num_list if i%2 == 0]
    return int(''.join(map(str, even_num))) + int(''.join(map(str, odd_num)))
```
- `map(str, even_num)`: 리스트 내 요소를 문자열로 반환
- `''.join()` : 변환된 문자열을 하나의 숫자 형태로 결합
- `int()`: 결합된 문자열을 정수형으로 변환

### 👍 다른 정답 코드
1.
```python
def solution(num_list):
    return int(''.join([str(x) for x in num_list if x % 2])) + int(''.join([str(x) for x in num_list if not x % 2]))
```
- 리스트 컴프리헨션으로 바로 `str(x)`를 받아서 `join`을 해주고 `int`형으로 변환할 수 있다.
2.
```python
def solution(num_list):
    o=[]
    e=[]
    for n in num_list:
        if n%2:o.append(str(n))
        else:e.append(str(n))
    return int(''.join(o))+int(''.join(e))
```
- `.append()` : 해당 함수의 매개변수로 `str(n)` 즉, 바로 문자열로 받을 수 있다.

