# [level 0] 배열 자르기 - 120833 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120833) 

### 성능 요약

메모리: 10 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 11일 22:52:16

### 문제 설명

<p>정수 배열 <code>numbers</code>와 정수 <code>num1</code>, <code>num2</code>가 매개변수로 주어질 때, <code>numbers</code>의 <code>num1</code>번 째 인덱스부터 <code>num2</code>번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>numbers</code>의 길이 ≤ 30</li>
<li>0 ≤ <code>numbers</code>의 원소 ≤ 1,000</li>
<li>0 ≤<code>num1</code> &lt; <code>num2</code> &lt; <code>numbers</code>의 길이</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>num1</th>
<th>num2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5]</td>
<td>1</td>
<td>3</td>
<td>[2, 3, 4]</td>
</tr>
<tr>
<td>[1, 3, 5]</td>
<td>1</td>
<td>2</td>
<td>[3, 5]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 4, 5]의 1번째 인덱스 2부터 3번째 인덱스 4 까지 자른 [2, 3, 4]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[1, 3, 5]의 1번째 인덱스 3부터 2번째 인덱스 5까지 자른 [3, 5]를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- 리스트 슬라이싱

### 💻 접근법
인사이트 : 리스트 슬라이싱
- 처음에는 num1 = 1이고 num2 = 3일때 `numbers[num1:num2]` 로 생각했는데 이러면 결과값은 인덱스 1에서 인덱스 3까지의 배열을 슬라이싱 해온다.
- 이후 `numbers[num1:num2+1]`로 수정해줬다. (인덱스 1~4까지)

### 📝 슈도코드
```
def solution(numbers, num1, num2)함수를 정의한다:
    변수 answer에 numbers 리스트의 num1번째부터 num2번째까지의 부분 리스트를 저장한다.(인덱스 num2까지 포함)
    answer을 반환한다.
```
```python
# 풀이 코드
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
```
- 직접 계산된 결과나 표현식을 return문에 넣어 반환하는 기능
- 코드를 간결하게 만들고, 실행 효율을 개선하는 데 도움을 준다.
- 이런 방식을 사용함으로써 변수 할당을 줄일 수 있다.
