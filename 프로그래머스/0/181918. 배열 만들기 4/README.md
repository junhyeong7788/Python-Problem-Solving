# [level 0] 배열 만들기 4 - 181918 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181918) 

### 성능 요약

메모리: 14 MB, 시간: 55.68 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 24일 00:21:38

### 문제 설명

<p>정수 배열 <code>arr</code>가 주어집니다. <code>arr</code>를 이용해 새로운 배열 <code>stk</code>를 만드려고 합니다.</p>

<p>변수 <code>i</code>를 만들어 초기값을 0으로 설정한 후 <code>i</code>가 <code>arr</code>의 길이보다 작으면 다음 작업을 반복합니다.</p>

<ul>
<li>만약 <code>stk</code>가 빈 배열이라면 <code>arr[i]</code>를 <code>stk</code>에 추가하고 <code>i</code>에 1을 더합니다.</li>
<li><code>stk</code>에 원소가 있고, <code>stk</code>의 마지막 원소가 <code>arr[i]</code>보다 작으면 <code>arr[i]</code>를 <code>stk</code>의 뒤에 추가하고 <code>i</code>에 1을 더합니다.</li>
<li><code>stk</code>에 원소가 있는데 <code>stk</code>의 마지막 원소가 <code>arr[i]</code>보다 크거나 같으면 <code>stk</code>의 마지막 원소를 <code>stk</code>에서 제거합니다.</li>
</ul>

<p>위 작업을 마친 후 만들어진 <code>stk</code>를 return 하는 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>arr</code>의 길이 ≤ 100,000

<ul>
<li>1 ≤ <code>arr</code>의 원소 ≤ 100,000</li>
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
<td>[1, 4, 2, 5, 3]</td>
<td>[1, 2, 3]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>각 작업을 마친 후에 배열의 변화를 나타내면 다음 표와 같습니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>i</th>
<th>arr[i]</th>
<th>stk</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>1</td>
<td>[]</td>
</tr>
<tr>
<td>1</td>
<td>4</td>
<td>[1]</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>[1, 4]</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>[1]</td>
</tr>
<tr>
<td>3</td>
<td>5</td>
<td>[1, 2]</td>
</tr>
<tr>
<td>4</td>
<td>3</td>
<td>[1, 2, 5]</td>
</tr>
<tr>
<td>4</td>
<td>3</td>
<td>[1, 2]</td>
</tr>
<tr>
<td>-</td>
<td>-</td>
<td>[1, 2, 3]</td>
</tr>
</tbody>
      </table>
<ul>
<li>따라서 [1, 2, 3]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `pop()` : 배열의 가장 마지막 원소를 제거하고 그 값을 반환하는 메서드
    - `pop(index)` : 특정 인덱스의 값을 제거할 수도 있다.

### 💻 접근법
인사이트 : for문과 if-elif-else로 해결하였으나 테스트케이스에서는 통과였지만 시간복잡도면에서 틀렸다.
- while문과 pop()을 사용하여 재풀이

### 🚫 틀린 문제 해결 코드
```python
def solution(arr):
    stk = []
    i = 0
    for x in range(len(arr)):
        if len(stk) == 0:
            i += 1
            stk.append(arr[x])
        elif stk[-1] < arr[-1]:
            i += 1
            stk.append(arr[i])
        else:
            stk.remove(stk[-1])
    return stk
```
- 시간복잡도 문제로 틀림
- for문과 `stk.remove(stk[-1])`코드의 최악 경우 시간복잡도가 $O(n)$에 실행될 수 있으므로 총 $O(n^2)$의 시간복잡도를 가질 수 있다.
- `remove()`: 사용하여 배열의 값을 제거하게 되면 모든 반복에서 마지막 값을 참조하게 되므로 비효율적이다.

### 📝 슈도코드
```
def solution(정수배열 arr를 매개변수로 받는다):
    stk(스택) 빈 리스트 생성 (스택 역할)
    변수 i를 0으로 초기화 (arr의 인덱스 역할)
    while i가 arr의 길이보다 작을 때까지 :
        if stk가 비어있다면:
            arr[i]값을 stk에 추가
            i를 1 증가
        elif stk의 마지막 값이 arr[i]보다 작다면:
            arr[i]값을 stk에 추가
            i를 1 증가
        else (stk의 마지막값이 arr[i]보다 크거나 같다면):
            stk의 마지막 값을 제거
    return stk
```
```python
# 풀이 코드
def solution(arr):
    stk = []  
    i = 0  
    while i < len(arr):  
        if not stk:  
            stk.append(arr[i]) 
            i += 1  
        elif stk[-1] < arr[i]: 
            stk.append(arr[i])  
            i += 1  
        else:  
            stk.pop()  
    return stk 
```
- 배열 arr를 한 번 순회하므로 시간 복잡도는 $**O(n)**$ 이다.

### 👍 다른 정답 코드
1.
```python
def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk
```
- for문을 사용하여 배열의 인덱스를 자동으로 처리
- while루프를 사용하여 스택의 마지막 값이 현재 배열 값보다 크거나 같을 때까지 계속 값을 제거
