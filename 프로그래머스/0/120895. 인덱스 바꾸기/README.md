# [level 0] 인덱스 바꾸기 - 120895 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120895?language=python3) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 11일 12:39:03

### 문제 설명

<p>문자열 <code>my_string</code>과 정수 <code>num1</code>, <code>num2</code>가 매개변수로 주어질 때, <code>my_string</code>에서 인덱스 <code>num1</code>과 인덱스 <code>num2</code>에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 &lt; <code>my_string</code>의 길이 &lt; 100</li>
<li>0 ≤ <code>num1</code>, <code>num2</code> &lt; <code>my_string</code>의 길이</li>
<li><code>my_string</code>은 소문자로 이루어져 있습니다.</li>
<li><code>num1</code> ≠ <code>num2</code></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>num1</th>
<th>num2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"hello"</td>
<td>1</td>
<td>2</td>
<td>"hlelo"</td>
</tr>
<tr>
<td>"I love you"</td>
<td>3</td>
<td>6</td>
<td>"I l veoyou"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"hello"의 1번째 인덱스인 "e"와 2번째 인덱스인 "l"을 바꾸면 "hlelo"입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"I love you"의 3번째 인덱스 "o"와 " "(공백)을 바꾸면 "I l veoyou"입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- 문자열은 불변 객체이므로 직접 수정 불가 -> 리스트로 변환해서 수정
- 리스트는 가변 객체이므로, 인덱스 기반으로 직접 원소를 변경할 수 있다.

### 💻 접근법
인사이트 : `enumerate()`를 사용하여 if문으로 조건을 주어 문자를 바꾼 문자열을 반환하는 것으로 풀이

### 📝 슈도코드
```
def solution(문자열 my_string과 정수 num1와 num2를 매개변수로 받는다):
    answer 변수 선언
    for my_string를 인덱스와 함께 튜플 형태로 반환하여 각 요소를 반복:
        if 인덱스 i가 num2와 같다면:
            answer리스트에 my_string[num1] 값을 추가한다.
        elif 인덱스 i가 num1와 같다면:
            answer리스트에 my_string[num2] 값을 추가한다.
        else:
            answer리스트에 나머지 요소를 추가한다.
    return 배열을 문자열로 결합한 값을 반환
```
```python
# 풀이 코드
def solution(my_string, num1, num2):
    answer = []
    for i, v in enumerate(my_string):
        if i == num2:
            answer.append(my_string[num1])
        elif i == num1:
            answer.append(my_string[num2])
        else:
            answer.append(v)
    return ''.join(answer)
```

### 👍 다른 정답 코드
1.
```python
def solution(my_string, num1, num2):
    strList = list(my_string)
    strList[num1], strList[num2] = strList[num2], strList[num1]
    return ''.join(strList)
```
- 다중 할당을 사용하여 값 교환 : `strList[num1], strList[num2]`에 각각 `strList[num2], strList[num1]`의 값을 할당하여 **서로의 값을 교환**
