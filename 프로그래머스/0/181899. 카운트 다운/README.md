# [level 0] 카운트 다운 - 181899 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181899) 

### 성능 요약

메모리: 9.97 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 19일 15:20:52

### 문제 설명

<p>정수 <code>start_num</code>와 <code>end_num</code>가 주어질 때, <code>start_num</code>에서 <code>end_num</code>까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>end_num</code> ≤ <code>start_num</code> ≤ 50</li>
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
<td>10</td>
<td>3</td>
<td>[10, 9, 8, 7, 6, 5, 4, 3]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>10부터 3까지 1씩 감소하는 수를 담은 리스트는 [10, 9, 8, 7, 6, 5, 4, 3]입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- python range() 함수 : `list(range(시작, 끝, 간격)`
- 간격에 실수(float)를 사용하려고 하면 numpy패키지의 arange()함수를 사용해야한다.

### 💻 접근법
인사이트 : range()함수를 사용해서 풀이

### 📝 슈도코드
```
def solution(매개변수로 start_num과 end_num을 받는다.
    return 첫번째 숫자부터 마지막 숫자 -1 까지 -1간격으로 리스트 생성한다.
```
```python
# 풀이 코드
def solution(start_num, end_num):
    return list(range(start_num, end_num-1, -1))
```

### 👍 다른 정답 코드
1.
```python
def solution(start, end):
    return [i for i in range(start,end-1,-1)]
```
- 리스트 컴프리헨션으로 리스트 생성
