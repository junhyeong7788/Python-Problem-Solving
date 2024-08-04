# [Bronze IV] 숫자의 합 - 11720

[문제 링크](https://www.acmicpc.net/problem/11720)

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현, 수학, 문자열

### 제출 일자

2024년 8월 5일 03:16:46

### 문제 설명

<p>N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.</p>

### 출력

 <p>입력으로 주어진 숫자 N개의 합을 출력한다.</p>

---

### 💻접근법

- 인사이트 : 예제 입력 2번 참고

### 📝슈도코드

```
n값 받기
numbers 변수에 list함수를 이용하여 숫자를 한 자리씩 나누어 받기
sum변수 선언하기

for numbers 탐색 :
    **sum변수에 numbers에 있는 각 자릿수를 가져와 더하기**

sum 출력
```

### 👍다른 정답 코드

```python
num = input()
numbers = list(map(int,input()))

print(sum(numbers))
```

### 🔗레퍼런스

- [백준 11720번: 숫자의 합 파이썬](https://bambbang00.tistory.com/21)
- [Do it! 알고리즘 코딩테스트 with Python - 배열과 리스트 실전문제](https://youtu.be/m2KpGo_-sGI)
