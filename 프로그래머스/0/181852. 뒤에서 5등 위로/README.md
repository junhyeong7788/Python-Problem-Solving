# [level 0] 뒤에서 5등 위로 - 181852 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181852) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 05일 03:31:23

### 문제 설명

<p>정수로 이루어진 리스트 <code>num_list</code>가 주어집니다. <code>num_list</code>에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>6 ≤ <code>num_list</code>의 길이 ≤ 30</li>
<li>1 ≤ <code>num_list</code>의 원소 ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[12, 4, 15, 46, 38, 1, 14, 56, 32, 10]</td>
<td>[15, 32, 38, 46, 56]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[12, 4, 15, 46, 38, 1, 14, 56, 32, 10]를 정렬하면 [1, 4, 10, 12, 14, 15, 32, 38, 46, 56]이 되고, 앞에서 부터 6번째 이후의 수들을 고르면 [15, 32, 38, 46, 56]가 됩니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `sorted()` : 해당 함수는 새로운 리스트를 반환하기 때문에 리스트 슬라이싱을 사용할 수 있다.

### 💻 접근법
인사이트 : list sorting, list slicing

### 📝 슈도코드
```
def solution(정수로 이루어진 num_list를 매개변수로 받는다):
    return num_list를 정렬하고 새로운 리스트 반환 후 6번째이후의 수들을 슬라이싱하여 반환
```
```python
# 풀이 코드
def solution(num_list):
    return sorted(num_list)[5:]
```

