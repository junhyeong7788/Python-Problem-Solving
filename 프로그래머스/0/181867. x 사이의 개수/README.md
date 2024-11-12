# [level 0] x 사이의 개수 - 181867 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181867) 

### 성능 요약

메모리: 11.7 MB, 시간: 3.19 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 11월 12일 22:06:35

### 문제 설명

<p>문자열 <code>myString</code>이 주어집니다. <code>myString</code>을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>myString</code>의 길이 ≤ 100,000

<ul>
<li><code>myString</code>은 알파벳 소문자로 이루어진 문자열입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>myString</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"oxooxoxxox"</td>
<td>[1, 2, 1, 0, 1, 0]</td>
</tr>
<tr>
<td>"xabcxdefxghi"</td>
<td>[0, 3, 3, 3]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"x"를 기준으로 문자열을 나누면 ["o", "oo", "o", "", "o", ""]가 됩니다. 각각의 길이로 배열을 만들면 [1, 2, 1, 0, 1, 0]입니다. 따라서 [1, 2, 1, 0, 1, 0]을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"x"를 기준으로 문자열을 나누면 ["", "abc", "def", "ghi"]가 됩니다. 각각의 길이로 배열을 만들면 [0, 3, 3, 3]입니다. 따라서 [0, 3, 3, 3]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 💻 접근법
인사이트 : cnt 변수를 선언하여 차례로 카운트를 증가시키면서 풀이

### 📝 슈도코드
```
def solution(문자열 myString을 매개변수로 받는다):
    answer = []
    cnt = 0
    for myString의 길이 만큼의 리스트 요소 반복:
        if myString[i] 가 'x'일치한다면:
            answer리스트에 cnt를 추가
            추가한 후 cnt를 0으로 초기화
        else: (myString[i]가 다른 값이라면)
            cnt 변수 1 증가
    answer리스트에 cnt 추가 # 루프가 끝난 후 남아있는 cnt 값을 추가
    return answer 리스트 반환
```
```python
# 풀이 코드
def solution(myString):
    answer = []
    cnt = 0
    for i in range(len(myString)):
        if myString[i] == 'x':
            answer.append(cnt)
            cnt = 0
        else:
            cnt += 1

    answer.append(cnt)
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(myString):
    split_strings = myString.split("x")
    result = [len(part) for part in split_strings]
    return result
```
- 'x' 를 기준으로 문자열을 나누고, 나눠진 문자열 조각들을 리스트에 저장
- 리스트 내 각 요소의 길이를 계산하고, 그 길이 값을 새로운 리스트에 저장
2.
```python
def solution(myString):
    return [len(w) for w in myString.split('x')]
```
- `1.` 코드에서 `.split('x')` 을 리스트 컴프리헨션 안에 집어넣어 한줄 코딩
