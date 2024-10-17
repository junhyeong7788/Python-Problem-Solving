# [level 1] x만큼 간격이 있는 n개의 숫자 - 12954 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12954) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.11 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 17일 21:46:20

### 문제 설명

<p>함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.</p>

<h4>제한 조건</h4>

<ul>
<li>x는 -10000000 이상, 10000000 이하인 정수입니다.</li>
<li>n은 1000 이하인 자연수입니다.</li>
</ul>

<h4>입출력 예</h4>
<table class="table">
        <thead><tr>
<th>x</th>
<th>n</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>2</td>
<td>5</td>
<td>[2,4,6,8,10]</td>
</tr>
<tr>
<td>4</td>
<td>3</td>
<td>[4,8,12]</td>
</tr>
<tr>
<td>-4</td>
<td>2</td>
<td>[-4, -8]</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 💻 접근법
인사이트 : 간단하게 리스트 컴프리헨션으로 풀이

### 📝 슈도코드
```
def solution(정수 x와 자연수 n을 매개변수로 받는다):
    return 1부터 n까지의 리스트요소를(인덱스) 반복, 현재 인덱스와 x를 곱한 값을 리스트에 추가 후 반환
```
```python
# 풀이 코드
def solution(x, n):
    return [x*i for i in range(1, n+1)]
```
