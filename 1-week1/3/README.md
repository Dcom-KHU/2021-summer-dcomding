# 1주차 문제3 - 연산자 끼워넣기

|구분|값|
|---|---|
|난이도|3|
|점수|3|
|출처|https://www.acmicpc.net/problem/14888|

## 문제 설명
`N`개의 수로 이루어진 `수열` A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어집니다. 또, 수와 수 사이에 끼워넣을 수 있는 `N-1개의 연산자`가 주어집니다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있습니다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있습니다. 이 때, 주어진 수의 순서를 바꾸면 안 됩니다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있습니다. 예를 들어, 아래와 같은 식을 만들 수 있습니다.

- 1+2+3-4×5÷6
- 1÷2+3+4-5×6
- 1+2÷3×4-5+6
- 1÷2×3-4+5+6

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 합니다. 또, 나눗셈은 정수 나눗셈으로 몫만 취합니다. 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같습니다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같습니다.

- 1+2+3-4×5÷6 = 1
- 1÷2+3+4-5×6 = 12
- 1+2÷3×4-5+6 = 5
- 1÷2×3-4+5+6 = 7

N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 만들어주세요.

## 제한 사항
- 2 ≤ N ≤ 11
- 1 ≤ A<sub>i</sub> ≤ 100
- -10억 ≤ 각 연산의 결과(중간 결과 포함) ≤ 10억

## 입력
첫째 줄에 수의 개수 N이 주어집니다.

둘째 줄에는 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어집니다.

셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수입니다. 

## 출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다.

## 예시
### 예시1
**입력**

```
2
5 6
0 0 1 0
```

**출력**
```
30
30
```

**설명**

- 최댓값: 5×6
- 최솟값: 5×6

### 예시2
**입력**

```
3
3 4 5
1 0 1 0
```

**출력**
```
35
17
```

**설명**

- 최댓값: 3+4×5
- 최솟값: 3×4+5

### 예시3
**입력**

```
6
1 2 3 4 5 6
2 1 1 1
```

**출력**
```
54
-24
```

**설명**

- 최댓값: 1-2÷3+4+5×6
- 최솟값: 1+2+3÷4-5×6