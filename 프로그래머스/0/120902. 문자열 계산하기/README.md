# [level 0] 문자열 계산하기 - 120902 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120902) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 24일 02:51:30

### 문제 설명

<p><code>my_string</code>은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 <code>my_string</code>이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>연산자는 +, -만 존재합니다.</li>
<li>문자열의 시작과 끝에는 공백이 없습니다.</li>
<li>0으로 시작하는 숫자는 주어지지 않습니다.</li>
<li>잘못된 수식은 주어지지 않습니다.</li>
<li>5 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>my_string</code>을&nbsp;계산한 결과값은 1 이상 100,000 이하입니다.

<ul>
<li><code>my_string</code>의 중간 계산 값은 -100,000 이상 100,000 이하입니다.</li>
<li>계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수입니다.</li>
<li><code>my_string</code>에는 연산자가 적어도 하나 포함되어 있습니다.</li>
</ul></li>
<li>return type 은 정수형입니다.</li>
<li><code>my_string</code>의 숫자와 연산자는 공백 하나로 구분되어 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"3 + 4"</td>
<td>7</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>3 + 4 = 7을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `eval(expression, globals=None, locals=None)` : 문자열로 된 파이썬 표현식을 실행하는 함수
    - expression : 문자열로된 파이썬 표현식
    - globals (선택사항) : 전역 변수를 담는 사전 객체로, 어떤 전역 변수가 평가에 사용될지 정의
    - locals (선택사항) : 변수를 담는 사전 객체로 어떤 지역 변수가 평가에 사용될지 정의

### 💻 접근법
인사이트 : eval 함수를 사용

### 📝 슈도코드
```
def solution( 문자열 my_string을 매개변수로 받는다 ):
    return eval(my_string)
```
```python
# 풀이 코드
def solution(my_string):
    return eval(my_string)
```

### 👍 다른 정답 코드
1.
```python
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
```
- 문자열 내에서 뺼셈 기호 ' - ' 를 덧셈과 음수형식으로 변환
    - 뺄셈을 덧셈과 음수로 처리하기 위함
- `split(' + ')` : ' + '를 기준으로 문자열을 나눈다.
