# [level 0] 가까운 1 찾기 - 181898 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181898) 

### 성능 요약

메모리: 10.8 MB, 시간: 4.60 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 13일 23:28:42

### 문제 설명

<p>정수 배열 <code>arr</code>가 주어집니다. 이때 <code>arr</code>의 원소는 1 또는 0입니다. 정수 <code>idx</code>가 주어졌을 때, <code>idx</code>보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.</p>

<p>단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>arr</code>의 길이 ≤ 100'000

<ul>
<li><code>arr</code>의 원소는 전부 1 또는 0입니다. </li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr</th>
<th>idx</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[0, 0, 0, 1]</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td>[1, 0, 0, 1, 0, 0]</td>
<td>4</td>
<td>-1</td>
</tr>
<tr>
<td>[1, 1, 1, 1, 0]</td>
<td>3</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>1보다 크면서 원소가 1인 가장 작은 인덱스는 3입니다. 따라서 3을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>4번 인덱스 이후에 1은 등장하지 않습니다. 따라서 -1을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>3번 인덱스의 값이 1입니다. 따라서 3을 return 합니다. </li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `try-except` : try블록 안의 코드에서 예외가 발생할 가능성이 있는 코드를 실행
    - except : try블록에서 예외가 발생하면 except 블록으로 제어가 넘어가고, 여기서 예외 상황을 처리한다.

### 💻 접근법
인사이트 : 조건으로 찾은 인덱스 배열에서 가장 작은 값을 찾으면 첫 번째 인덱스이다.

### 📝 슈도코드
```
def solution(정수 배열 arr와 정수 idx를 매개변수로 받는다):
    answer 리스트 선언
    for arr의 각 요소와 인덱스를 순회:
        if 배열의 값이 1이고, 인덱스가 idx 이상인 겨웅:
            해당 인덱스를 answer리스트에 추가
    if answer리스트가 비어 있지 않으면:
        return answer리스트의 가장 작은 값 반환 (= 첫 번째 1의 인덱스)
    else (리스트가 비어있으면):
        return -1
```
```python
# 풀이 코드
def solution(arr, idx):
    answer = [i for i, a in enumerate(arr) if a == 1 and i >= idx]
    return min(answer) if answer != [] else -1
```
```python
def solution(arr, idx):
    answer = []  # 결과를 저장할 빈 리스트 생성
    
    # 배열 arr의 각 요소와 인덱스를 순회
    for i, a in enumerate(arr):
        # 배열의 값이 1이고, 인덱스가 idx 이상인 경우
        if a == 1 and i >= idx:
            # 해당 인덱스를 answer 리스트에 추가
            answer.append(i)
    
    # answer 리스트가 비어 있지 않으면 가장 작은 값을 반환 (즉, 첫 번째 1의 인덱스)
    if answer != []:
        return min(answer)
    else:
        # answer 리스트가 비어 있으면 -1 반환
        return -1
```

### 👍 다른 정답 코드
1.
```python
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer
```
- `try 블록` : try블록 안에 예외가 발생할 수 잇는 코드를 넣는다. 이 경우 arr.index(1, idx)가 실행, 배열에 1이 없는 경우 ValueError가 발생
- `arr.index(1, idx)`: 배열 arr에서 값 x가 처음으로 등장하는 인덱스를 반환하는 메서드
    - 여기서는 값 1을 찾으며, idx 이후부터 검색을 시작, 즉, 배열의 인덱스 idx부터 배열 arr에서 1이 처음 등장하는 위치를 반환
- `except 블록` : try블록에서 예외가 발생하면 except블록이 실행, answer에 -1 저장
2. 
```python
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1
```
- `for i in range(idx, len(arr)):` : 인덱스 `idx`부터 배열의 마지막 인덱스 `len(arr)-1`까지의 범위를 생성하여 각 요소 반복
- ` if arr[i] == 1:` : 배열 arr의 i번째 요소를 확인하여 값이 1인지 검사하는 조건
