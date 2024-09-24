# [level 0] 홀짝에 따라 다른 값 반환하기 - 181935 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181935) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 24일 23:45:35

### 문제 설명

<p>양의 정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>이 홀수라면 <code>n</code> 이하의 홀수인 모든 양의 정수의 합을 return 하고 <code>n</code>이 짝수라면 <code>n</code> 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>7</td>
<td>16</td>
</tr>
<tr>
<td>10</td>
<td>220</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>n</code>은 7로 홀수입니다. 7 이하의 모든 양의 홀수는 1, 3, 5, 7이고 이들의 합인 1 + 3 + 5 + 7 = 16을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>n</code>은 10으로 짝수입니다. 10 이하의 모든 양의 짝수는 2, 4, 6, 8, 10이고 이들의 제곱의 합인 2<sup>2</sup> + 4<sup>2</sup> + 6<sup>2</sup> + 8<sup>2</sup> + 10<sup>2</sup> = 4 + 16 + 36 + 64 + 100 = 220을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- list comprehension, odd_num과 even_num

### 💻 접근법
인사이트 : for loop와 if문 사용, 리스트 컴프리헨션으로 해결
- `range(start, end, step)` : 지정된 범위의 숫자 시퀀스를 생성하는 데 사용, 일반적으로 for루프에서 반복을 수행할 때 숫자리스트를 생성하는 데 유용하다.

### 📝 슈도코드
```
def solution(매개변수로 정수 n을 받는다):
    홀수를 담을 리스트 변수 선언
    짝수를 담을 리스트 변수 선언
    if n이 홀수이면:
        for 0~n+1까지 순회한다:
            0~n+1중에 홀수숫자이면:
                홀수 리스트 변수에 홀수 숫자를 추가한다.
        return 홀수 리스트 요소를 모두 더해 반환
    else n이 짝수이면:
        for 0~n+1까지 순회한다:
            0~n+1중에 짝수숫자이면:
                짝수 숫자의 제곱을 짝수 리스트 변수에 추가한다.
        return 짝수 리스트 요소를 모두 더해 반환
```
```python
# 풀이 코드 1
def solution(n):
    odd_answer = [] 
    even_answer = []
    
    if n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                odd_answer.append(i)
        return sum(odd_answer)
    else : 
        for i in range(n+1):
            if i % 2 == 0:
                even_answer.append(i**2)
        return sum(even_answer)
```
```python
#풀이코드 2
def solution(n):
    if n % 2 == 1:
        return sum([i for i in range(n+1) if i%2 == 1])
    else : 
        return sum([i**2 for i in range(n+1) if i%2 == 0])
```

### 👍 다른 정답 코드
1.
```python
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])
```
- `range(start, end, step)` : **시작점**에 따라 **홀수와 짝수를 구별**하여 리스트를 만들고 해당 요소들을 모두 더하여 풀이할 수 있다.
