# [level 0] 삼각형의 완성조건 (1) - 120889 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120889?language=python3) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 20일 23:28:13

### 문제 설명

<p>선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.</p>

<ul>
<li>가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.</li>
</ul>

<p>삼각형의 세 변의 길이가 담긴 배열 <code>sides</code>이 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>sides</code>의 원소는 자연수입니다.</li>
<li><code>sides</code>의 길이는 3입니다.</li>
<li>1 ≤ <code>sides</code>의 원소 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>sides</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3]</td>
<td>2</td>
</tr>
<tr>
<td>[3, 6, 2]</td>
<td>2</td>
</tr>
<tr>
<td>[199, 72, 222]</td>
<td>1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>가장 큰 변인 3이 나머지 두 변의 합 3과 같으므로 삼각형을 완성할 수 없습니다. 따라서 2를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>가장 큰 변인 6이 나머지 두 변의 합 5보다 크므로 삼각형을 완성할 수 없습니다. 따라서 2를 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>가장 큰 변인 222가 나머지 두 변의 합 271보다 작으므로 삼각형을 완성할 수 있습니다. 따라서 1을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `sum()` : 리스트, 튜플 등의 반복 가능한 객체의 모든 요소를 더한 값을 반환 / 정수, 실수 등 다양한 숫자형 데이터 타입에서 사용가능
    - 반복 가능한 객체에 포함된 값들이 숫자가 아니면 에러가 발생
- `max()` : 반복 가능한 객체에서 가장 큰 값을 반환
    - 반복 가능한 객체 내의 요소들이 비교 가능 (ex : 숫자끼지 비교가능, 문자열끼리 사전순 비교 가능)
- `list.remove()` : 리스트에서 첫 번째로 등장하는 특정 값을 삭제하는 함수 / `list.remove(num)` : 리스트에서 num을 삭제하는 함수
- 삼항연산자 : 조건부 표현식, 간단한 조건문을 한 줄로 표현할 수 있는 문법
    - `<참일 때 반환할 값> if <조건식> else <거짓일 때 반환할 값>`

### 💻 접근법
인사이트 : list method ( `sum(), max(), remove()` )

### 📝 슈도코드
```
def solution(매개변수로 sides 리스트를 받는다):
    최대숫자 변수 생성 = sides리스트에서 최대값
    삭제숫자 변수 생성 = sides리스트에서 최대숫자를 삭제
    리스트합 변수 생성 = 최대숫자가 삭제된 sides리스트의 합
    if 최대숫자 < 리스트합 :
        return 1
    else:
        return 2
```
```python
# 풀이 코드 1
def solution(sides):
    max_num = max(sides)
    del_num = sides.remove(max_num)
    sum_list = sum(sides)
    if max_num < sum_list :
        return 1
    else :
        return 2
```
```python
# 풀이 코드 2
def solution(sides):
    max_num = max(sides)
    sides.remove(max_num)
    sum_list = sum(sides)
    return 1 if max_num < sum_list else 2
```
- 삼항연산자를 사용하여 if문을 one-line coding 했다.
- `sides.remove(max_num)`: 해당 코드는 값을 삭제하지만 아무것도 반환하지 않는다. 그 결과 풀이 코드1은 `del_num = None`이 나왔다. **즉, 변수 선언이 불필요하다.**
  
### 👍 다른 정답 코드
1.
```python
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
```
- 삼각형이 되기 위한 조건 : (세변의 총합 - 최대 변 길이) > 최대 변 길이
- 삼항연산자를 사용하여 조건문을 간단하게 표현하고 반환
2.
```python
def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2
```
- 리스트를 정렬하여 리스트 인덱스로 풀이
