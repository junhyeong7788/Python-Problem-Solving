# [level 0] 배열 만들기 3 - 181895 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181895?language=python3) 

### 성능 요약

메모리: 15.9 MB, 시간: 0.99 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 23일 22:35:38

### 문제 설명

<p>정수 배열 <code>arr</code>와 2개의 구간이 담긴 배열 <code>intervals</code>가 주어집니다.</p>

<p><code>intervals</code>는 항상 <code>[[a1, b1], [a2, b2]]</code>의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.</p>

<p>이때 배열 <code>arr</code>의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>arr</code>의 길이 ≤ 100,000

<ul>
<li>1 ≤ <code>arr</code>의 원소 &lt; 100</li>
</ul></li>
<li>1 ≤ <code>a1</code> ≤ <code>b1</code> &lt; <code>arr</code>의 길이</li>
<li>1 ≤ <code>a2</code> ≤ <code>b2</code> &lt; <code>arr</code>의 길이</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr</th>
<th>intervals</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5]</td>
<td>[[1, 3], [0, 4]]</td>
<td>[2, 3, 4, 1, 2, 3, 4, 5]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>첫 번째 구간에 해당하는 배열은 [2, 3, 4] 입니다.</li>
<li>두 번째 구간에 해당하는 배열은 [1, 2, 3, 4, 5] 입니다.</li>
<li>따라서 이 두 배열을 앞뒤로 붙인 배열인 [2, 3, 4, 1, 2, 3, 4, 5]를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 💻 접근법
인사이트 : 간단하게 리스트 슬라이싱으로 더함으로 해결

### 📝 슈도코드
```
def solution(정수 배열 arr와 2개의 구간이 담긴 배열 intervals를 매개변수로 받는다):
    return arr intervals[0][0]에서 [0][1]+1 까지 슬라이싱 한것과 [1][0]에서 [1][1]+1ㅓ까지 슬라이싱 한것을 더한 배열을 반환한다.
```
```python
# 풀이 코드
def solution(arr, intervals):
    return arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]
```

### 👍 다른 정답 코드
1.
```python
def solution(arr, intervals):
    return [arr[i:j+1] for i, j in intervals][0] + [arr[i:j+1] for i, j in intervals][1]
```
```python
def solution(arr, intervals):
    answer = []
    for i, j in intervals:
        answer.append(arr[i:j+1])
    return answer[0] + answer[1]
```
- intervals는 이차원 배열이기에 `for i, j in intervals` 하였을 때 i는 0행 0열과 0행 1열을 반복, j는 1행 0열과 1행 1열을 반복
    - `arr[i:j+1]` : arr의 i와 j+1값으로 슬라이싱한 값을 answer변수에 저장 (저장된 값 : `[[2, 3, 4], [5, 6]]`)
    - answer리스트의 첫번째 요소와 두번째 요소를 더하여 하나의 리스트로 만든다.
