# [level 1] 같은 숫자는 싫어 - 12906 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12906) 

### 성능 요약

메모리: 27.9 MB, 시간: 40.87 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

정확성: 71.9<br/>효율성: 28.1<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 11월 10일 21:55:25

### 문제 설명

<p>배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,</p>

<ul>
<li>arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.</li>
<li>arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.</li>
</ul>

<p>배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.</p>

<h5>제한사항</h5>

<ul>
<li>배열 arr의 크기 : 1,000,000 이하의 자연수</li>
<li>배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>[1,1,3,3,0,1,1]</td>
<td>[1,3,0,1]</td>
</tr>
<tr>
<td>[4,4,4,3,3]</td>
<td>[4,3]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1,2<br>
문제의 예시와 같습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 📝 슈도코드
```
def solution(리스트 arr를 매개변수로 받는다):
    answer 변수 생성 = []
    for arr의 요소를 반복:
        if answer리스트의 마지막 요소와 현재 요소가 같다면:
            continue # 건너 뛴다
        answer.append(i)
    return answer리스트 반환
```
```python
# 풀이 코드
def solution(arr):
    answer = []  # 결과를 저장할 리스트
    
    # 리스트의 모든 요소를 순회
    for i in arr:
        # answer 리스트의 마지막 요소와 현재 요소가 같다면 건너뛴다
        if answer[-1:] == [i]:  
            continue
        # 현재 요소를 answer에 추가
        answer.append(i)
    
    return answer  # 중복이 제거된 리스트 반환
```

### 👍 다른 정답 코드
1.
```python
def solution(arr):
    answer = []
    previous = None  # 이전 값을 추적하기 위한 변수
    for i in arr:
        # 이전 값과 다를 때만 answer에 추가
        if i != previous:
            answer.append(i)
            previous = i  # 현재 값을 이전 값으로 업데이트
    return answer
```
- **previous 변수를 사용하여 연속된 숫자를 건너뛰는 방식으로 중복을 제거하기 때문에 메모리와 시간 면에서 최적화된 코드**
- for 루프 : 배열 arr의 모든 요소를 순회하면서 previous와 비교
    - 현재 값 i가 previous와 다를 경우에만 answer에 추가하고, previous를 현재 값으로 업데이트
- 시간 복잡도 : $O(n)$
