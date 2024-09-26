# [level 0] 카운트 업 - 181920 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181920?language=python3) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 26일 16:28:41

### 문제 설명

<p>정수 <code>start_num</code>와 <code>end_num</code>가 주어질 때, <code>start_num</code>부터 <code>end_num</code>까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>start_num</code> ≤ <code>end_num</code> ≤ 50</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>start_num</th>
<th>end_num</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>10</td>
<td>[3, 4, 5, 6, 7, 8, 9, 10]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>3부터 10까지의 숫자들을 담은 리스트 [3, 4, 5, 6, 7, 8, 9, 10]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `range(start, end, step)`
- `lambda함수`

### 💻 접근법
인사이트 : range()를 사용하여 리스트를 생성

### 📝 슈도코드
```
def solution(정수 start_num와 end_num을 매개변수로 받는다):
    return start_num부터 end_num까지 list를 선언한 리스트를 반환
```
```python
# 풀이 코드 1
def solution(start_num, end_num):
    return list(range(start_num, end_num+1))
```
```python
# 풀이 코드 2
solution = lambda start, end : [i for i in range(start, end+1)]
```

### 👍 다른 정답 코드
1.
```python
def solution(start, end):
    return [i for i in range(start,end+1)]
```
- list comprehension으로 리스트 생성하여 풀이하는 방법
