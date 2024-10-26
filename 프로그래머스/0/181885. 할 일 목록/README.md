# [level 0] 할 일 목록 - 181885 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181885) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 26일 22:54:47

### 문제 설명

<p>오늘 해야 할 일이 담긴 문자열 배열 <code>todo_list</code>와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 <code>finished</code>가 매개변수로 주어질 때, <code>todo_list</code>에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>todo_list</code>의 길이 1 ≤ 100</li>
<li>2 ≤ <code>todo_list</code>의 원소의 길이 ≤ 20

<ul>
<li><code>todo_list</code>의 원소는 영소문자로만 이루어져 있습니다.</li>
<li><code>todo_list</code>의 원소는 모두 서로 다릅니다.</li>
</ul></li>
<li><code>finished[i]</code>는 true 또는 false이고 true는 <code>todo_list[i]</code>를 마쳤음을, false는 아직 마치지 못했음을 나타냅니다.</li>
<li>아직 마치지 못한 일이 적어도 하나 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>todo_list</th>
<th>finished</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["problemsolving", "practiceguitar", "swim", "studygraph"]</td>
<td>[true, false, true, false]</td>
<td>["practiceguitar", "studygraph"]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>todo_list</code> 중에서 "problemsolving"과 "swim"은 마쳤고, "practiceguitar"와 "studygraph"는 아직 마치지 못했으므로 <code>todo_list</code>에서 나온 순서대로 담은 문자열 배열 ["practiceguitar", "studygraph"]를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `zip()` : 여러 개의 iterable 객체를 받아, 동일한 인덱스의 요소들을 하나의 튜플로 묶어 반환

### 💻 접근법
인사이트 : 두 배열을 동일한 인덱스로 묶어 조건에 맞는 값을 반환

### 📝 슈도코드
```
def solution(문자열 배열 todo_list와 불리언 배열 finished를 매개변수로 받는다):
    unfinished_tasks 리스트변수 선언
    for todo_list와 finished배열을 동일한 인덱스 순서로 묶어(zip) 튜플로 만들어 반복:
        if is_done이 False인 경우:
            unfinished_tasks에 task값을 추가
    return unfinished_tasks 리스트를 반환
```
```python
# 풀이 코드
def solution(todo_list, finished):
    unfinished_tasks = [task for task, is_done in zip(todo_list, finished) if not is_done]
    return unfinished_tasks
```
- zip 함수는 여러 개의 iterable 객체를 받아, 동일한 인덱스의 요소들을 하나의 튜플로 묶어 반환
