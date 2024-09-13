# [level 0] 배열 만들기 1 - 181901 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181901) 

### 성능 요약

메모리: 10.4 MB, 시간: 44.91 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 13일 20:00:52

### 문제 설명

<p>정수 <code>n</code>과 <code>k</code>가 주어졌을 때, 1 이상 <code>n</code>이하의 정수 중에서 <code>k</code>의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 1,000,000</li>
<li>1 ≤ <code>k</code> ≤ min(1,000, n)</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>3</td>
<td>[3, 6, 9]</td>
</tr>
<tr>
<td>15</td>
<td>5</td>
<td>[5, 10, 15]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>1 이상 10 이하의 3의 배수는 3, 6, 9 이므로 [3, 6, 9]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>1 이상 15 이하의 5의 배수는 5, 10, 15 이므로 [5, 10, 15]를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- list comprehension, append()

### 💻 접근법
인사이트 : n개를 k로 나눴을 때 나머지가 0인 것을 리스트에 추가
- [[level 0] n의 배수 - 181937](https://github.com/junhyeong7788/Python-Problem-Solving/tree/8182ed529cfacbf3700c39a5c34961cd3a609a56/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/0/181937.%E2%80%85n%EC%9D%98%E2%80%85%EB%B0%B0%EC%88%98) : 해당 문제에서 정수 num이 n의 배수인지 확인하는 부분에서 인사이트를 얻었다.

### 📝 슈도코드
```
def solution함수(정수 n, 배수 지정 k):
    정답 리스트
    for i in range(1부터 n+1까지):
        if i를 k로 나눴을 때 나머지가 0과 동일하다면:
            answer(정답)리스트에 i를 추가
    return 정답 리스트
```
```python
# 풀이 코드 1
def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)
    return answer
```
```python
# 풀이 코드 2 
def solution(n, k):
    return [i for i in range(1, n+1) if i % k == 0]
```
- 리스트 컴프리헨션 사용
### 👍 다른 정답 코드
```python
def solution(n, k):
    return [i for i in range(k, n+1, k)]
```
- K부터 시작한 코드, 굳이 1부터 시작 안해도 된다.
    
