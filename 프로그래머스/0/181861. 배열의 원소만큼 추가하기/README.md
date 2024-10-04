# [level 0] 배열의 원소만큼 추가하기 - 181861 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181861?language=python3) 

### 성능 요약

메모리: 11 MB, 시간: 0.68 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 05일 03:53:41

### 문제 설명

<p>아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 양의 정수 배열 <code>arr</code>가 매개변수로 주어질 때, <code>arr</code>의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X를 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>arr</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>arr</code>의 원소 ≤ 100</li>
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
<td>[5, 1, 4]</td>
<td>[5, 5, 5, 5, 5, 1, 4, 4, 4, 4]</td>
</tr>
<tr>
<td>[6, 6]</td>
<td>[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]</td>
</tr>
<tr>
<td>[1]</td>
<td>[1]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><p>예제 1번에 대해서 a와 X를 나타내보면 다음 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>a</th>
<th>X</th>
</tr>
</thead>
        <tbody><tr>
<td></td>
<td>[]</td>
</tr>
<tr>
<td>5</td>
<td>[5, 5, 5, 5, 5]</td>
</tr>
<tr>
<td>1</td>
<td>[5, 5, 5, 5, 5, 1]</td>
</tr>
<tr>
<td>4</td>
<td>[5, 5, 5, 5, 5, 1, 4, 4, 4, 4]</td>
</tr>
</tbody>
      </table>
<p>따라서 [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]를 return 합니다.</p></li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><p>예제 2번에 대해서 a와 X를 나타내보면 다음 표와 같습니다. </p>
<table class="table">
        <thead><tr>
<th>a</th>
<th>X</th>
</tr>
</thead>
        <tbody><tr>
<td></td>
<td>[]</td>
</tr>
<tr>
<td>6</td>
<td>[6, 6, 6, 6, 6, 6]</td>
</tr>
<tr>
<td>6</td>
<td>[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]</td>
</tr>
</tbody>
      </table>
<p>따라서 [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]를 return 합니다.</p></li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li><p>예제 2번에 대해서 a와 X를 나타내보면 다음 표와 같습니다. </p>
<table class="table">
        <thead><tr>
<th>a</th>
<th>X</th>
</tr>
</thead>
        <tbody><tr>
<td></td>
<td>[]</td>
</tr>
<tr>
<td>1</td>
<td>[1]</td>
</tr>
</tbody>
      </table>
<p>따라서 [1]을 return 합니다.</p></li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `sum(list_of_lists, start)` : sum() 함수는 기본적으로 숫자들의 합을 계산하기 위해 사용
    - 위 코드와 같이 두번째 인자로 주어진 시작 값과 함께 시퀀스의 아이템들을 더할 수 있도록 일반화되어 있다.
    - `start` = 초기값으로 병합의 시작점을 나타낸다. 이 문제에서는 빈 리스트`[]`를 시작값으로 사용하였다.

### 💻 접근법
인사이트 : arr의 각 요소를 순회하여 answer리스트에 `[i]*i`로 추가를 하여 `sum()` 함수로 리스트 병합하여 풀이

### 📝 슈도코드
```
def solution(양의 정수 배열 arr를 매개변수로 받는다):
    return arr의 각 요소를 순회하여 [i]*i의 새로운 배열을 만들고 []를 기준으로 리스트 병합한 값을 반환
```
```python
# 풀이 코드
def solution(arr):
    return sum([[i]*i for i in arr], [])
```
- `메모리: 11.1 MB, 시간: 1.71 ms`
```python
# 풀이 코드 2
def solution(arr):
    answer = []
    for i in arr:
        answer.append([i] * i)
    return sum(answer , [])
```
- REMIND : `sum(list_of_lists, start)`

### 👍 다른 정답 코드
1.
```python
def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer
```
- `메모리: 11 MB, 시간: 0.10 ms`
2.
```python
def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            answer.append(arr[i])
    return answer
```
- `메모리: 11 MB, 시간: 0.68 ms`
- `range(len(arr))` : arr 리스트의 각 인덱스에 접근할 수 있도록 반복문을 설정
- `for j in range(arr[i])` : arr[i]는 i번째 요소의 값, `j`는 실제로 사용되지 않지만, `arr[i]` 횟수만큼 반복하여 해당 요소를 리스트에 추가하기 위한 카운터 역할을 한다.
