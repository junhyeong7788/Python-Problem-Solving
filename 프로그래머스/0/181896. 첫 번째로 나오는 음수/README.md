# [level 0] 첫 번째로 나오는 음수 - 181896 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181896) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 16일 16:56:50

### 문제 설명

<p>정수 리스트 <code>num_list</code>가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>5 ≤ <code>num_list</code>의 길이 ≤ 100</li>
<li>-10 ≤ <code>num_list</code>의 원소 ≤ 100</li>
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
<td>[12, 4, 15, 46, 38, -2, 15]</td>
<td>5</td>
</tr>
<tr>
<td>[13, 22, 53, 24, 15, 6]</td>
<td>-1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>5번 인덱스에서 음수가 처음 등장하므로 5를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>음수가 없으므로 -1을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `enumerate()` : 반복 가능한 객체에 대해 인덱스와 해당 요소를 동시에 제공하는 함수

### 💻 접근법
인사이트 : enumerate()함수로 풀이할 수 있을 것 같다.

### 📝 슈도코드
```
def solution(매개변수로 num_list를 받는다):
    for num_list의 각 요소를 인덱스와 함께 반복 (enumerate함수로 인덱스와 요소를 동시에 가져온다):
        if num이 0보다 작다면:
            해당 요소의 인덱스 index를 반환
    else (음수를 찾지 못하면):
        return -1을 반환
```
```python
# 풀이 코드
def solution(num_list):
    for index, num in enumerate(num_list):
        if num < 0:
            return index
    else:
        return -1
```

### 👍 다른 정답 코드
1.
```python
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i]<0:
            return i
    return -1
```
- `for i in range(len(num_list))` : for 루프는 리스트 num_list의 인덱스 i를 0부터 len(num_list)-1까지 반복한다, `range(len(num_list))`는 리스트의 길이만큼 인덱스를 생성한다.
- `if num_list[i] < 0` : 리스트의 각 요소 num_list[i]가 음수(0보다 작은 값)인지 확인하는 조건문, 음수를 발견하면 그 음수의 인덱스 i를 반환
- 위 코드를 이해하면서 len(num_list)는 배열의 길이를 반환할것이다 라고 생각을 하였다. (아래 예시로 이해)
```python
num_list = [10, 20, 30, 40]
for i in range(len(num_list)):
    print(num_list[i])  # 인덱스 i를 통해 리스트의 요소를 읽는다

# 결과
10
20
30
40
```
