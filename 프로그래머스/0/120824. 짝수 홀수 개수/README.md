# [level 0] 짝수 홀수 개수 - 120824 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120824) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 10일 22:50:58

### 문제 설명

<p>정수가 담긴 리스트&nbsp;<code>num_list</code>가 주어질 때, <code>num_list</code>의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>num_list</code>의 길이 ≤ 100</li>
<li>0 ≤ <code>num_list</code>의 원소 ≤ 1,000</li>
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
<td>[1, 2, 3, 4, 5]</td>
<td>[2, 3]</td>
</tr>
<tr>
<td>[1, 3, 5, 7]</td>
<td>[0, 4]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 4, 5]에는 짝수가 2, 4로 두 개, 홀수가 1, 3, 5로 세 개 있습니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[1, 3, 5, 7]에는 짝수가 없고 홀수가 네 개 있습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- 짝수 : num % 2 == 0
- 홀수 : num % 2 == 1

### 💻 접근법
인사이트 : for loop와 if문 사용, answer배열에 짝수와 홀수 개수를 추가

### 📝 슈도코드
```
def solution함수 (정수가 담긴 리스트):
    정답 리스트

    짝수리스트, 홀수리스트
    for num in 정수가 담긴 리스트:
        if num을 2로 나눴을 때 나머지가 0이면:
            짝수 리스트에 1 추가
        else :
            홀수 리스트에 1 추가
    정답 리스트 = [짝수 리스트, 홀수 리스트]
    return 정답 리스트
```

```python
# 풀이 코드
def solution(num_list):
    answer = []
    
    odd_num, even_num = 0, 0
    
    for num in num_list:
        if num % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    
    answer = [even_num, odd_num]
    
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
```
- `answer[n%2]`: answer리스트에서 인덱스를 `n % 2`로 접근하여 해당 인덱스의 값을 1씩 증가시킨다.
- n이 홀수일 경우 n%2=1, 짝수일 경우 무조건 0이 나온다.
- 그렇기 떄문에 n이 존재하는 한 `answer[0]`, `answer[1]`에 1씩 계속 더해진다.
2.
```python
def solution(num_list):
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]
```
- 람다함수와 map함수 사용하여 각 숫자가 짝수인지 홀수인지를 판별한 값을 새로운 리스트로 만든 뒤, 해당 리스트에서 짝수(0)의 개수와 홀수(1)의 개수를 카운트하여 반환
- `map() 함수` : 리스트 num_list의 각 요소에 대해 지정한 함수를 적용하여 새로운 리스트를 생성하는 함수
- `lambda v: v % 2` : 리스트의 각요소 v에 대해 2로 나눈 나머지를 반환 (0이면 짝수, 1이면 홀수)
- `dic_num_list.count(0)`: 짝수의 개수를 세고 (1)은 홀수의 개수를 센다.
