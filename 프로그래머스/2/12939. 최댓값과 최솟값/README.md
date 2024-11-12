# [level 2] 최댓값과 최솟값 - 12939 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12939) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 11월 12일 22:21:43

### 문제 설명

<p>문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.<br>
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.</p>

<h5>제한 조건</h5>

<ul>
<li>s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>"1 2 3 4"</td>
<td style="text-align: center">"1 4"</td>
</tr>
<tr>
<td>"-1 -2 -3 -4"</td>
<td style="text-align: center">"-4 -1"</td>
</tr>
<tr>
<td>"-1 -1"</td>
<td style="text-align: center">"-1 -1"</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `.split()` : 문자열을 특정 구분자를 기준으로 나누어, 각 부분을 리스트 형태로 반환하는 파이썬의 문자열 메서드
    - Default : 공백(space)

### 💻 접근법
인사이트 : split() 함수 사용

### 📝 슈도코드
```
def solution(문자열 s를 매개변수로 받는다):
    numbers = 문자열 s를 
```
```python
# 풀이 코드
def solution(s):
    numbers = list(map(int, s.split()))
    return f"{min(numbers)} {max(numbers)}"
```
- `s.split()` : 공백을 기준으로 문자열을 나눠 문자를 리스트로 반환
- numbers : s 문자열을 공백을 기준으로 문자를 정수로 바꿔 리스트 생성
