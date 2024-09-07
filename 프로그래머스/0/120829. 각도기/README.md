# [level 0] 각도기 - 120829 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120829?language=python3) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 07일 21:16:03

### 문제 설명

<p>각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 각 <code>angle</code>이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.</p>

<ul>
<li>예각 : 0 &lt; <code>angle</code> &lt; 90</li>
<li>직각 : <code>angle</code> = 90</li>
<li>둔각 : 90 &lt; <code>angle</code> &lt; 180</li>
<li>평각 : <code>angle</code> = 180</li>
</ul>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>angle</code> ≤ 180</li>
<li><code>angle</code>은 정수입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>angle</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>70</td>
<td>1</td>
</tr>
<tr>
<td>91</td>
<td>3</td>
</tr>
<tr>
<td>180</td>
<td>4</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>angle</code>이 70이므로 예각입니다. 따라서 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>angle</code>이 91이므로 둔각입니다. 따라서 3을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>angle</code>이 180이므로 평각입니다. 따라서 4를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
### 다른 풀이
1.
```python
def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
```
- 조건문 방식 : 각도 범위를 조건문으로 직접 정의하였기 때문에 angle의 값을 직관적으로 확인 가능
- 장점 : 코드가 명확하고 직관적으로 각 구간이 어떻게 분류되는지 알 수 있다.
2.
```python
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
```
- 단순화된 연산 : 나머지 연산(%)과 몫 연산(//)을 사용해 90도 단위로 각을 나누고, 나머지가 있는 경우 추가 값을 더하는 방식
-  코드가 간결하고 수학적 연산을 활용해 각도를 구분함
- ex : `angle = 100일 경우` : `( 100 // 90 ) * 2 + ( 100 % 90 > 0 ) * 1 = 2 + 1 = 3`
