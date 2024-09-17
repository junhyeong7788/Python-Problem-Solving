# [level 0] 숨어있는 숫자의 덧셈 (1) - 120851 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120851) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 17일 18:42:48

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어집니다. <code>my_string</code>안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이&nbsp;≤ 1,000</li>
<li><code>my_string</code>은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.</li>
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
<td>"aAb1B2cC34oOp"</td>
<td>10</td>
</tr>
<tr>
<td>"1a2b3c4d123"</td>
<td>16</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"aAb1B2cC34oOp"안의 한자리 자연수는 1, 2, 3, 4 입니다. 따라서 1 + 2 + 3 + 4 = 10 을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"1a2b3c4d123Z"안의 한자리 자연수는 1, 2, 3, 4, 1, 2, 3 입니다. 따라서 1 + 2 + 3 + 4 + 1 + 2 + 3 = 16 을 return합니다.</li>
</ul>

<hr>

<h5>유의사항</h5>

<ul>
<li>연속된 숫자도 각각 한 자리 숫자로 취급합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `.isdigit()`: python 문자열(str)객체에서 사용되는 내장함수, 문자열이 숫자(digits)로만 이루어져 있는지 확인하는 데 사용, 이 함수는 문자열의 모든 문자가 숫자 (0~9)로 이루어져 있으면 True를 반환, 그렇지 않으면 False를 반환

### 💻 접근법
인사이트 : 내장함수로 간단하게 풀이할수있을 것 같다.
- for문으로도 해결해보자.

### 📝 슈도코드
```
def solution(매개변수로 my_string 문자열을 받는다):
    for 문자열 my_string의 각 문자를 순회:
        if 문자가 숫자인지 확인:
            문자가 숫자인 경우, 해당 문자를 정수로 변환하고 sum에 더한다.
    return sum의 값을 반환한다.
```
```python
# 풀이 코드
def solution(my_string):
    return sum([int(num) for num in my_string if num.isdigit()])
```
- 리스트 컴프리헨션 사용 : my_string에서 찾은 숫자들로 이루어진 정수 리스트를 만든다.
- 메모리 오버헤드 : 이 코드는 sum()함수로 넘기기 전에 전체 리스트를 생성하기 때문에, 리스트를 저장하는 데 추가 메모리를 사용한다.
```python
def solution(my_string):
    return sum(int(num) for num in my_string if num.isdigit())
```
- 제너레이터 표현식 사용 : 중간 리스트를 생성하지 않기 때문에, 특히 입력 문자열이 클 경우 메모리를 적게 사용한다.
### 👍 다른 정답 코드
1.
```python
def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i) # answer += int(i)
        except:
            pass

    return answer
```
- `try-except 구조` : 주어진 문자를 숫자로 변환할 때 발생할 수 있는 예외를 처리하기 위해 사용
    - try블록 : int(i)로 문자를 정수로 변환 시도
    - except블록 : int(i)에서 오류가 발생하면(즉, i가 숫자가 아닌 문자일 경우), 오류를 무시하고 그냥 넘어감

