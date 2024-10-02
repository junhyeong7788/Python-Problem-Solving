# [level 1] 정수 내림차순으로 배치하기 - 12933 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12933) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 03일 00:49:26

### 문제 설명

<p>함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.</p>

<h5>제한 조건</h5>

<ul>
<li><code>n</code>은 1이상 8000000000 이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>118372</td>
<td style="text-align: center">873211</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `sort(reverse=True)` = `sorted(answer_list, reverse=True)`

### 💻 접근법
인사이트 : 정수 -> 문자열 -> 리스트 -> 정렬 -> 문자열 -> 정수
- 리스트 정렬을 사용하여 풀이 하였는데 올바른 풀이였다.

### 📝 슈도코드
```
def solution( 정수 n을 매개변수로 받는다 ):
    변수 answer 선언 = 정수n을 문자열로 변환 후 list로 만든다.
    answer리스트를 내림차순 정렬
    return answer리스트를 문자열로 join하고 이를 int형으로 변환한 값을 반환
```
```python
# 풀이 코드
def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    return int(''.join(answer))
```
```python
# 한줄 코드
def solution(n):
    return int("".join(sorted(str(n), reverse=True)))
```

### 👍 다른 정답 코드
1.
```python
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def solution(n):
    arr = list(str(n))
    n = int(''.join(mergeSort(arr)))
    return n
```
- 내가 풀이한 코드와 동일하게 n을 문자열로 변환하여 리스트로 변환하여 풀이하는 방법
- 병합정렬 : 분할 정복 알고리즘으로, 배열을 반으로 나누어 각각을 정렬한 후 다시 병합한다.
    - `O(nlogn)`: 시간복잡도를 가지며, 최악의 경우에도 성능이 일정하다.
    - 커스터마이징 가능성 : mergeSort()는 커스터마이징이 가능, 다른 형태의 정렬 요구 사항을 처리할 수 있다.
- 파이썬 내장 정렬 `sort()` 함수는 이미 매우 최적화되어 있으므로, 병합정렬을 직접 구현하는 것은 불필요하게 복잡하다. (병합 정렬은 추가적인 메모리 사용 발생)
