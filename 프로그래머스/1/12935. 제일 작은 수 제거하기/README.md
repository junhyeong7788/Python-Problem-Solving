# [level 1] 제일 작은 수 제거하기 - 12935 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12935) 

### 성능 요약

메모리: 15.7 MB, 시간: 1.10 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 08일 20:22:10

### 문제 설명

<p>정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.</p>

<h5>제한 조건</h5>

<ul>
<li>arr은 길이 1 이상인 배열입니다.</li>
<li>인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[4,3,2,1]</td>
<td>[4,3,2]</td>
</tr>
<tr>
<td>[10]</td>
<td>[-1]</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `max()`, `min()`
- `return [-1]` : 바로 [-1]값을 반환

### 💻 접근법
인사이트 : 처음에는 arr의 요소를 answer리스트에 저장하여 제거하려고 하였는데 시간초과 발생
- 바로 arr의 길이에 따라 if문을 작성하여 풀이

### 📝 슈도코드
```
def solution(정수를 저장한 배열 arr를 매개변수로 받는다):
    if arr의 길이가 1 초과이면:
        arr리스트에서 가장 작은 값을 제거한다.
        return arr리스트 반환
    else (arr의 길이가 1 이하이면) :
        return [-1]값을 반환
```
```python
# 풀이 코드
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]
```

### 👍 다른 정답 코드
1.
```python
def solution(arr):
    answer = []
    if len(arr) <= 1:
        answer.append(-1) 
    else:
        arr.remove(min(arr))
        answer = arr
    return answer
```
