# [level 1] 짝수와 홀수 - 12937 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12937) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 06일 03:22:32

### 문제 설명

<p>정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.</p>

<h5>제한 조건</h5>

<ul>
<li>num은 int 범위의 정수입니다.</li>
<li>0은 짝수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td style="text-align: center">"Odd"</td>
</tr>
<tr>
<td>4</td>
<td style="text-align: center">"Even"</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- 

### 💻 접근법
인사이트 : 짝수, 홀수에 따라 문자열 반환

### 📝 슈도코드
```
def solution( 정수 num을 매개변수로 받는다):
    return 만약 num을 2로 나눴을 때 나머지가 0일 경우 문자열 Even을 반환 홀수일 경우 문자열 Odd를 반환
```
```python
# 풀이 코드
def solution(num):
    return 'Even' if num % 2 == 0 else 'Odd'
```
- 조건부 표현식 사용 : 짧고 명확하게 조건 처리

```python
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else: 
        answer = 'Odd'
    return answer
```
### 👍 다른 정답 코드
1.
```python
def solution(num): return ["Even", "Odd"].pop(num % 2)
```
- 리스트와 pop() 메소드 사용
- `.pop(num % 2)` : 리스트에서 주어진 인덱스의 아이템을 제거하고 그 값을 반환, num % 2의 결과에 따라 0 또는 1을 반환
- 가독성과 유지보수 측면에서 어려움을 초래할 수 있다.
