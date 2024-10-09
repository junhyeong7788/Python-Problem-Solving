# [level 0] 특별한 이차원 배열 1 - 181833 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181833) 

### 성능 요약

메모리: 10.4 MB, 시간: 0.06 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 09일 21:03:29

### 문제 설명

<p>정수 <code>n</code>이 매개변수로 주어질 때, 다음과 같은 <code>n</code> × <code>n</code> 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.</p>

<ul>
<li>arr[i][j] (0 ≤ i, j &lt; <code>n</code>)의 값은 i = j라면 1, 아니라면 0입니다.</li>
</ul>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>[[1, 0, 0], [0, 1, 0], [0, 0, 1]]</td>
</tr>
<tr>
<td>6</td>
<td>[[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]</td>
</tr>
<tr>
<td>1</td>
<td>[[1]]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><p>예제 1번의 <code>n</code>의 값은 3으로 다음과 같이 2차원 배열을 채울 수 있습니다.</p>
<table class="table">
        <thead><tr>
<th>i \ j</th>
<th>0</th>
<th>1</th>
<th>2</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
</tbody>
      </table>
<p>따라서 [[1, 0, 0], [0, 1, 0], [0, 0, 1]]을 return 합니다.</p></li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><p>예제 2번의 <code>n</code>의 값은 6으로 다음과 같이 2차원 배열을 채울 수 있습니다.</p>
<table class="table">
        <thead><tr>
<th>i \ j</th>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
</tbody>
      </table>
<p>따라서 [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]을 return 합니다.</p></li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li><p>예제 1번의 <code>n</code>의 값은 1이고 다음과 같이 2차원 배열을 채울 수 있습니다.</p>
<table class="table">
        <thead><tr>
<th>i \ j</th>
<th>0</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>1</td>
</tr>
</tbody>
      </table>
<p>따라서 [[1]]을 return 합니다.</p></li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `answer = [[0]*n for _ in range(n)]`: 변수 i대신 _를 사용하여 불필요한 변수 삭제 가능

### 💻 접근법
인사이트 : 2차원 배열 생성 후, 2차원 배열 요소를 순회하면서 특별한 위치에 1을 추가

### 📝 슈도코드
```
def solution(정수 n를 매개변수로 받는다):
    answer 변수 선언 = n * n 크기의 2차원 리스트 생성
    for 0부터 n-1까지 반복:
        answer배열의 각 [i][i] 행과 열의 인덱스, 대각선 요소에 1로 설정
    return answer 리스트를 반환
```
```python
# 풀이 코드
def solution(n):
    answer = [[0]*n for i in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer
```
- `answer = [[0]*n for _ in range(n)]`: 변수 i대신 _를 사용하여 불필요한 변수 삭제 가능
