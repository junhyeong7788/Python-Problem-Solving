# [level 1] 자연수 뒤집어 배열로 만들기 - 12932 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12932?language=python3) 

### 성능 요약

메모리: 10.4 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 06일 23:33:53

### 문제 설명

<p>자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.</p>

<h5>제한 조건</h5>

<ul>
<li>n은 10,000,000,000이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>12345</td>
<td>[5,4,3,2,1]</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `map()` : 각 요소에 함수가 적용된 결과를 담고 있는 map 객체를 반환
- `reversed()` : 반복 가능한 객체를 역순으로 뒤집어서 반환하는 기능을 제공

### 💻 접근법
인사이트 : `reversed()` 함수를 사용, 형변환 사용

### 📝 슈도코드
```
def solution(정수 n을 매개변수로 받는다):
    return n을 문자형으로 바꾸고 뒤집은 문자열을 순회한다. 그리고 정수형으로 변환한 값으로 리스트 생성 후 반환한다.
```
```python
# 풀이 코드
def solution(n):
    return [int(i) for i in reversed(str(n))]
```
```python
def solution(n):
    answer = []
    for i in reversed(str(n)):
        answer.append(int(i))
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(n):
    return list(map(int, str(n)[::-1]))
```
- `str(n)[::-1]`: 문자열로 변환된 n을 슬라이싱을 이용해 뒤집는다.
- `map(int, ...)` : 뒤집어진 문자열의 각 문자들을 정수로 변환
