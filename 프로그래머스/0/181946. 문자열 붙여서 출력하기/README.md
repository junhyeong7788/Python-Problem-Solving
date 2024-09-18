# [level 0] 문자열 붙여서 출력하기 - 181946 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181946) 

### 성능 요약

메모리: 7.34 MB, 시간: 12.38 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 18일 23:18:06

### 문제 설명

<p>두 개의 문자열 <code>str1</code>, <code>str2</code>가 공백으로 구분되어 입력으로 주어집니다.<br>
입출력 예와 같이 <code>str1</code>과 <code>str2</code>을 이어서 출력하는 코드를 작성해 보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>str1</code>, <code>str2</code>의 길이 ≤ 10</li>
</ul>

<hr>

<h5>입출력 예</h5>

<p>입력 #1</p>
<div class="highlight"><pre class="codehilite"><code>apple pen
</code></pre></div>
<p>출력 #1</p>
<div class="highlight"><pre class="codehilite"><code>applepen
</code></pre></div>
<p>입력 #2</p>
<div class="highlight"><pre class="codehilite"><code>Hello World!
</code></pre></div>
<p>출력 #2</p>
<div class="highlight"><pre class="codehilite"><code>HelloWorld!
</code></pre></div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `input()` : 사용자가 콘솔(터미널)에서 입력한 문자열을 읽어온다. 입력된 모든 내용은 문자열(string) 형태로 저장
- `.strip()` : 입력된 문자열의 앞뒤에 있는 공백문자를 제거
- `.split(' ')` : 문자열을 공백(스페이스)을 기준으로 나누는 함수, 입력 문자열이 공백으로 구분된 여러 부분으로 나뉘게 된다.
- `str1, str2 =` : split()이 반환한 리스트에 두개의 값이 있다고 가정하고, 각각 할당

### 💻 접근법
인사이트 : 문자열을 받아왔으니 문자열의 합을 생각하게 되었다.

### 📝 슈도코드
```
str1변수와 str2변수 = 사용자가 입력한 문자열을 읽어온다.입력된 문자열의 앞뒤에 있는 공백 문자를 제거한다.입력된 문자열을 공백기준으로 나눈다.
str1와 str2문자열을 합한 결과를 출력한다.
```
```python
# 풀이 코드
str1, str2 = input().strip().split(' ')
print(str1 + str2)
```

### 👍 다른 정답 코드
1.
```python
print(input().strip().replace(' ', ''))
```
- 내가 풀이한 코드는 반드시 두 개의 단어가 있어야하고 두 개의 단어만 허용하는 코드이다.
- 다른 풀이 코드는 몇 개의 단어가 있어도 문제가 없고 입력에 상관없이 공백을 제거하여 출력된다.
