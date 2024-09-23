# [level 0] 수 조작하기 1 - 181926 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181926) 

### 성능 요약

메모리: 10.4 MB, 시간: 13.26 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 23일 23:14:23

### 문제 설명

<p>정수 <code>n</code>과 문자열 <code>control</code>이 주어집니다. <code>control</code>은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, <code>control</code>의 앞에서부터 순서대로 문자에 따라 <code>n</code>의 값을 바꿉니다.</p>

<ul>
<li>"w" : <code>n</code>이 1 커집니다.</li>
<li>"s" : <code>n</code>이 1 작아집니다.</li>
<li>"d" : <code>n</code>이 10 커집니다.</li>
<li>"a" : <code>n</code>이 10 작아집니다.</li>
</ul>

<p>위 규칙에 따라 <code>n</code>을 바꿨을 때 가장 마지막에 나오는 <code>n</code>의 값을 return 하는 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>-100,000 ≤ <code>n</code> ≤ 100,000</li>
<li>1 ≤ <code>control</code>의 길이 ≤ 100,000

<ul>
<li><code>control</code>은 알파벳 소문자 "w", "a", "s", "d"로 이루어진 문자열입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>control</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>"wsdawsdassw"</td>
<td>-1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>수 <code>n</code>은 <code>control</code>에 따라 다음과 같은 순서로 변하게 됩니다.</li>
<li>0 → 1 → 0 → 10 → 0 → 1 → 0 → 10 → 0 → -1 → -2 → -1</li>
<li>따라서 -1을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- for loop
  

### 💻 접근법
인사이트 : for loop

### 📝 슈도코드
```
def solution(매개변수로 정수n과 문자열 control을 받는다):
    for 문자열 control을 순회한다:
        만약 x가 "w"와 일치한다면:
            n = n + 1
        만약 x가 "a"와 일치한다면:
            n = n - 10
        만약 x가 "s"와 일치한다면:
            n = n - 1
        만약 x가 "d"와 일치한다면:
            n = n + 10
    return n을 반환
```
```python
# 풀이 코드
def solution(n, control):
    for x in control:
        if x == "w":
            n += 1
        elif x == "a":
            n -= 10
        elif x == "s":
            n -= 1
        else:
            n += 10
    return n
```

### 👍 다른 정답 코드
1.
```python
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])
```
- `key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))` : 주어진 문자 각각을 숫자 1, -1, 10, -10과 연결하는 딕셔너리를 생성한다.
- `zip()`: 두 리스트의 각 요소를 튜플로 묶어준다. 이 튜플들을 dict()함수에 전달하여 키-값 상을 가진 딕셔너리를 만든다.
- `sum([key[c] for c in control])` : control 문자열의 각 문자c에 대해 딕셔너리 key에서 해당 문자에 대응하는 값을 가져온다. 이 값들은 주어진 컨트롤 문자에 따라 n을 더하거나 뺄 값들이다.
2.
```python
def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer
```
- dictionary로 각 문자에 따른 값 매핑
- for loop를 사용하여 control문자열을 순회, 각 만복에서 i는 control문자열의 각 문자를 나타냄, c[i]는 현재 문자 i에 해당하는 값을 딕셔너리 c에서 찾아내어 answer에 더한다.
3.
```python
def solution(n, control):
    return n + 10*(control.count('d')-control.count('a')) + (control.count('w')-control.count('s'))
```
- 각 문자열에 대해 발생횟수를 계산하여, 상쇄될 수 있는 값의 발생횟수를 빼준다.
