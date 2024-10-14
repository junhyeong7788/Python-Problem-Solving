# [level 0] 숫자 찾기 - 120904 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120904?language=python3) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 14일 18:55:05

### 문제 설명

<p>정수 <code>num</code>과 <code>k</code>가 매개변수로 주어질 때, <code>num</code>을 이루는 숫자 중에 <code>k</code>가 있으면 <code>num</code>의  그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>num</code> &lt; 1,000,000</li>
<li>0 ≤ <code>k</code> &lt; 10</li>
<li><code>num</code>에 <code>k</code>가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>29183</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td>232443</td>
<td>4</td>
<td>4</td>
</tr>
<tr>
<td>123456</td>
<td>7</td>
<td>-1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>29183에서 1은 3번째에 있습니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>232443에서 4는 4번째에 처음 등장합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>123456에 7은 없으므로 -1을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `enumerate()` : (index, value) 형태의 튜플을 반환하는 이터레이터를 생성
    - 리스트, 튜플등에서 요소의 인덱스가 필요할 때 유용하게 사용

### 💻 접근법
인사이트 : 주어진 숫자는 정수이기 때문에 정수를 문자형으로 변환 후 비교하는 것으로 풀이

### 📝 슈도코드
```
def solution(정수 num과 k를 매개변수로 받는다):
    for str(num)을 인덱스와 값으로 반복:
        if str(k)와 v가 같으면:
            return i + 1값을 반환
    return -1을 반환
```
```python
# 풀이 코드
def solution(num, k):
    for i, v in enumerate(str(num)):
        if str(k) == v:
            return i + 1
    return -1
```

### 👍 다른 정답 코드
1.
```python
def solution(num, k):
    k_str = str(k) 
    num_str = str(num)  
    index = num_str.find(k_str) # k가 num_str에서 처음 등장하는 인덱스를 찾기
    return index + 1 if index != -1 else -1 # find 메서드는 -1을 반환할 수 있으므로, 인덱스를 1-based로 조정
```
- `find() 메서드` : find() 메서드가 -1이 아닌 경우, 즉 k가 num에 존재하는 경우 index+1을 반환하여 1-based인덱스를 제공
    - 반면 index가 -1인 경우, 즉 k가 num에 존재하지 않으면 -1을 반환
