# [level 0] 홀짝 구분하기 - 181944 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181944) 

### 성능 요약

메모리: 7.48 MB, 시간: 13.06 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 26일 01:18:31

### 문제 설명

<p>자연수 <code>n</code>이 입력으로 주어졌을 때 만약 <code>n</code>이 짝수이면 "<code>n</code> is even"을, 홀수이면 "<code>n</code> is odd"를 출력하는 코드를 작성해 보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>

<p>입력 #1</p>
<div class="highlight"><pre class="codehilite"><code>100
</code></pre></div>
<p>출력 #1</p>
<div class="highlight"><pre class="codehilite"><code>100 is even
</code></pre></div>
<p>입력 #2</p>
<div class="highlight"><pre class="codehilite"><code>1
</code></pre></div>
<p>출력 #2</p>
<div class="highlight"><pre class="codehilite"><code>1 is odd
</code></pre></div>
<p>※ 2023년 05월 15일 지문이 수정되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `f-string` : 문자열 포매팅 방식
- `input()` : 사용자로부터 입력을 받는 함수
    -  `input(prompt)`: 함수는 prompt라는 매개변수를 사용할 수 있다.

### 💻 접근법
인사이트 : print로 출력

### 📝 슈도코드
```
a = 사용자한테 받은 입력을 int형으로 a변수에 저장한다.

if a가 짝수이면:
    print( a is even를 출력 )
else a가 홀수이면:
    print( a is odd를 출력)
```
```python
# 풀이 코드
a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else :
    print(f'{a} is odd')
```
- `f-string` : 문자열 포매팅 방식, 간결하고 가독성 좋은 방식으로 문자열 안에 변수나 표현식을 삽입할 수 있게 해준다.

### 👍 다른 정답 코드
1.
```python
N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")
```
- if문으로 한줄 쓰기 가능
2.
```python
a = int(input())

if a % 2 == 0:
    print('{} is even'.format(a))
else :
    print('{} is odd'.format(a))
```
- `str.format()` 방식을 사용
