# [level 0] 문자열 바꿔서 찾기 - 181864 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181864) 

### 성능 요약

메모리: 9.96 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 10일 14:36:45

### 문제 설명

<p>문자 "A"와 "B"로 이루어진 문자열 <code>myString</code>과 <code>pat</code>가 주어집니다. <code>myString</code>의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중  <code>pat</code>이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>myString</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>pat</code>의 길이 ≤ 10

<ul>
<li><code>myString</code>과 <code>pat</code>는 문자 "A"와 "B"로만 이루어진 문자열입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>myString</th>
<th>pat</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"ABBAA"</td>
<td>"AABB"</td>
<td>1</td>
</tr>
<tr>
<td>"ABAB"</td>
<td>"ABAB"</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"ABBAA"에서 "A"와 "B"를 서로 바꾸면 "BAABB"입니다. 여기에는 부분문자열 "AABB"가 있기 때문에 1을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"ABAB"에서 "A"와 "B"를 서로 바꾸면 "BABA"입니다. 여기에는 부분문자열 "BABA"가 없기 때문에 0을 return 합니다.</li>
</ul>

<p>※ 2023년 05월 15일 제한사항 및 테스트 케이스가 수정되었습니다. 기존에 제출한 코드가 통과하지 못할 수 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `int(불리안 연산자)`, if문내에서 비교연산자로 문자열 비교도 가능

### 💻 접근법
인사이트 : 리스트로 만들어서 문자열로 결합하는 것으로 풀이

### 📝 슈도코드
```
def solution(문자열 myString과 pat을 매개변수로 받는다):
    answer 변수 선언
    for myString의 요소를 반복:
        if i == "A"이면:
            answer리스트에 "B" 추가
        else:
            answer리스트에 "A" 추가
    answer리스트를 문자열로 결합
    return myString문자열 안에 pat 문자열이 존재하면 1 반환, 없으면 0 반환
```
```python
# 풀이 코드
def solution(myString, pat):
    answer = "".join("B" if i == "A" else "A" for i in myString)
    return int(pat in answer)
```
```python
# 풀어 쓰기
def solution(myString, pat):
    answer = []
    for i in myString:
        if i == "A":
            answer.append("B")
        else:
            answer.append("A")
    answer = "".join(answer)
    
    return 1 if pat in answer else 0
```
