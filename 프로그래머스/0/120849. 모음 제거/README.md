# [level 0] 모음 제거 - 120849 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120849) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 06일 22:01:57

### 문제 설명

<p>영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 <code>my_string</code>이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>my_string</code>은 소문자와 공백으로 이루어져 있습니다.</li>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"bus"</td>
<td>"bs"</td>
</tr>
<tr>
<td>"nice to meet you"</td>
<td>"nc t mt y"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"bus"에서 모음 u를 제거한 "bs"를 return합니다.</li>
</ul>

<p>입출력 예 #1</p>

<ul>
<li>"nice to meet you"에서 모음 i, o, e, u를 모두 제거한 "nc t mt y"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### REMIND
- List Comprehension
- not in 연산자
- [.join()](https://github.com/junhyeong7788/TIL/blob/15dfe1b4caa27a8f6c4d8610d1a78d367ecaa133/Python/join().md)

### 다른 풀이
```python
def solution(my_string):
    word = ("a", "e", "i", "o", "u")
    return ''.join([i for i in my_string if i not in word])
```
- `i for i in my_sting`: my_string의 각 문자를 i로 하나씩 순회
- `if i not in word`: 현재 순회 중인 문자 i가 word(모음 리스트)안에 포함 되어 있지 않은 경우에만 그 문자를 결과 리스트에 추가
- `''.join()` : 리스트 안의 문자열 요소들을 하나의 문자열로 합쳐주는 매서드 (여기서는 빈 문자열 사용)
  
```python
def solution(my_string):
    words = ['a', 'e', 'i', 'o', 'u']
    for i in words:
        my_string = my_string.replace(i, '')
    return my_string
```
- for 루프는 words 리스트에 있는 각 모음을 하나씩 변수 i에 저장하며 순차적으로 실행
- `replace()` : 문자열 내에서 특정 문자를 다른 문자로 대체하는 함수 / 여기서는 i로 나타나는 각 모음을 빈 문자열 ('')로 대체하고, 그 결과를 my_string에 할당
