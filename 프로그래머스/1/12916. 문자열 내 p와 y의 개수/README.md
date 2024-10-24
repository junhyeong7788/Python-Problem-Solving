# [level 1] 문자열 내 p와 y의 개수 - 12916 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12916) 

### 성능 요약

메모리: 9.96 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 24일 18:48:37

### 문제 설명

<p>대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.</p>

<p>예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.</p>

<h5>제한사항</h5>

<ul>
<li>문자열 s의 길이 : 50 이하의 자연수</li>
<li>문자열 s는 알파벳으로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>"pPoooyY"</td>
<td>true</td>
</tr>
<tr>
<td>"Pyy"</td>
<td>false</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.</p>

<p>입출력 예 #2<br>
'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.</p>

<p>※ 공지 - 2021년 8월 23일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND & 💻 접근법
인사이트 : 처음에 문자열을 모두 소문자로 변환하지 않고 풀이해서 오답발생
- 문자열 내 특정 문자 개수 세기 : `count()`
- 문자열 모든 요소 소문자로 변환 : `lower()`

### 📝 슈도코드
```
def solution( 문자열 s를 매개변수로 받는다):
    p_count 변수 = 문자열 s를 모두 소문자로 변환 후 'p'의 개수를 카운트
    y_count 변수 = 문자열 s를 모두 소문자로 변환 후 'y'의 개수를 카운트
    if p_count 가 y_count와 같지 않다면:
        return False
    else : (같거나 없으면)
        return True
```
```python
# 풀이 코드 1
def solution(s):
    p_count = s.lower().count('p')
    s_count = s.lower().count('y')
    if p_count != s_count:
        return False
    else:
        return True
```
```python
# 풀이 코드 2
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
```
- 변수 선언 없이 조건에 만족하면 True값을 반환
