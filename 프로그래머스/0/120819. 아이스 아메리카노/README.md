# [level 0] 아이스 아메리카노 - 120819 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120819) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 10일 22:35:18

### 문제 설명

<p>머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 <code>money</code>가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return&nbsp;하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>money</code> ≤ 1,000,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>money</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>5,500</td>
<td>[1, 0]</td>
</tr>
<tr>
<td>15,000</td>
<td>[2, 4000]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>5,500원은 아이스 아메리카노 한 잔을 살 수 있고 잔돈은 0원입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>15,000원은 아이스 아메리카노 두 잔을 살 수 있고 잔돈은 4,000원입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
### 🤔 REMIND
- 배열에 추가해야해서 꼭 append함수를 써야한다고만 생각하였다.
- 배열에 추가해주려고 하지 않아도 된다.

### 💻 접근법
인사이트 
- 커피 개수 구하는 방법 : 가지고 있는 돈 // 커피가격
- 잔돈 구하는 방법 : 가지고 있는 돈 % 커피 가격

### 📝 슈도코드
```
def solution함수(돈):
    정답 변수 [ 가지고 있는 돈 // 커피가격, 가지고 있는 돈 % 커피 가격]
    return 정답
```

```python
# 풀이 코드
def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer
```

### 👍 다른 정답 코드
```python
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer
```
```python
def solution(money):
    return [money // 5500, money % 5500]
```
```python
def solution(money):
    return divmod(money, 5500)
```
- `divmod(a, b)`: 두 개의 숫자를 입력받아 그 숫자들의 몫과 나머지를 한 번에 계산해 반환하는 함수
    - a : 나누어 지는 숫자(피제수)
    - b : 나누는 숫자(제수
    - `(몫, 나머지)`를 튜플 형태로 반환/ 즉, `(a // b, a % b)` 와 동일한 결과를 제공한다.
