# [level 0] 제곱수 판별하기 - 120909 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120909) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 05일 10:21:22

### 문제 설명

<p>어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 1,000,000</li>
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
<td>144</td>
<td>1</td>
</tr>
<tr>
<td>976</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>144는 12의 제곱이므로 제곱수입니다. 따라서 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>976은 제곱수가 아닙니다. 따라서 2를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
### REMIND
- 제곱수 : `sqrt = n ** (1/2)` , `sqrt = n ** 0.5`
    - $\sqrt{n} = n^{1/2}$
- `float.is_integer()` : 부동 소수점(float) 객체에서 사용되는 메서드
    - float 인스턴스가 정숫값을 가진 유한이면, True(1)를 , 그렇지 않으면 False(0)를 돌려준다.
    - 공식문서 
    ```python
    >>>(-2.0).is_integer()
    True
    >>>(3.2).is_integer()
    False
    ```
    - 두 가지 메서드가 16진수 문자열과의 변환을 지원합니다. 파이썬의 float는 내부적으로 이진수로 저장되기 때문에 float를 십진수 문자열로 또는 그 반대로 변환하는 것은 보통 반올림 오류를 수반합니다. 이에 반해, 16진수 문자열은 부동 소수점 숫자의 정확한 표현과 지정을 가능하게 합니다. 이것은 디버깅 및 수치 작업에 유용할 수 있습니다.  


### 다른 풀이
```python
# 내가 푼 풀이
def solution(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return 1
    else :
        return 2
```
```python
# 코드 간결화
def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2
```
```python
# is_integer 사용
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
```
