# [level 0] 옷가게 할인 받기 - 120818 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120818) 

### 성능 요약

메모리: 9.91 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 09일 11:20:57

### 문제 설명

<p>머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.<br>
구매한 옷의 가격&nbsp;<code>price</code>가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>10 ≤ <code>price</code> ≤ 1,000,000

<ul>
<li><code>price</code>는 10원 단위로(1의 자리가 0) 주어집니다.</li>
</ul></li>
<li>소수점 이하를 버린 정수를 return합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>price</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>150,000</td>
<td>142,500</td>
</tr>
<tr>
<td>580,000</td>
<td>464,000</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>150,000원에서 5%를 할인한 142,500원을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>580,000원에서 20%를 할인한 464,000원을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- dictionary, for loop

### 💻 접근법
인사이트 : 조건문을 사용하여 해당 가격 지정 후 리턴값을 준다.

### 📝 슈도코드
```
def solution함수 (가격):
    if 가격이 50만원 이상이면
        return 정수(가격 - (할인률 20%))
    elif 가격이 30만원이상이고 50만원 미만이면:
        return 정수(가격 - (할인률 10%))
    elif 가격이 10만원이상이고 30만원 미만이면:
        return 정수(가격 -(할인률 5%))
    else :
        return 정수(가격)
```

```python
# 풀이 코드
def solution(price):
    if price >= 500000:
        return int(price - (price*0.2))
    elif price >= 300000 and price < 500000:
        return int(price - (price*0.1))
    elif price >= 100000 and price < 300000:
        return int(price - (price*0.05))
    else : 
        return int(price)
```

### 👍 다른 정답 코드
```python
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
```
- dictionary로 정의 / 특정 가격 기준을 key로 저정, 각 가격에 적용할 할인율을 value로 저장
- for 반복문을 사용하여 discount_rates사전의 각 항목을 순회 / 할인 적용 기준 가격과 적용 할인율을 추출
- 할인된 가격을 구하고, 이를 정수로 변환하여 반환 / 사전은 내림차순 정렬이므로, 더 높은 할인율이 적용할 경우 먼저 검사하고 조건에 맞으면 바로 반환
