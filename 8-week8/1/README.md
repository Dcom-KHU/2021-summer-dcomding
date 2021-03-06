# 8주차 문제1 - 유사회문

|구분|값|
|---|---|
|난이도|2|
|점수|2|
|출처|https://www.acmicpc.net/problem/17609|

## 문제 설명
`회문(palindrom)`은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말합니다. 예를 들어, `abba`, `kayak`, `reviver`, `madam`은 모두 회문입니다. 마찬가지로 `apple`, `dcom`은 앞 뒤 방향으로 볼 때 같은 순서로 구성되지 않았으므로 회문이 아닙니다.

만약 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 이 문자열을 `유사회문`이라고 부릅니다. 예를 들어, `summuus`는 5번째나 6번째 문자 `u`를 삭제하여 `summus`라는 회문을 만들 수 있으므로 유사회문입니다.

문자열 `word`가 주어질 때, 이 문자열이 회문인지, 유사회문인지, 아무 것도 아닌지 판단하는 프로그램을 만들어주세요.


## 제한 사항
- 1 ≤ word의 길이 ≤ 100,000
- word는 알파벳 소문자로만 이루어져 있습니다.

## 입력
첫째 줄에 word가 주어집니다.

## 출력
첫째 줄에 회문인 경우 `0`을, 유사회문인 경우 `1`을, 아무 것도 아닌 경우 `2`을 출력합니다.

## 예시
### 예시1
**입력**
```
abba
```

**출력**
```
0
```

**설명**

문제의 예시와 같습니다.


### 예시2
**입력**
```
summuus
```

**출력**
```
1
```

**설명**

문제의 예시와 같습니다.


### 예시3
**입력**
```
xabba
```

**출력**
```
1
```

**설명**

맨 앞의 `x`를 삭제하면 회문이 되는 유사회문입니다.


### 예시4
**입력**
```
xabbay
```

**출력**
```
2
```

**설명**

한 문자를 삭제해서 회문으로 만들 수 없습니다.


### 예시5
**입력**
```
comcom
```

**출력**
```
2
```

**설명**

한 문자를 삭제해서 회문으로 만들 수 없습니다.


### 예시6
**입력**
```
comwwmoc
```

**출력**
```
0
```

**설명**

회문입니다.


### 예시7
**입력**
```
comwwtmoc
```

**출력**
```
1
```

**설명**

`t`를 삭제하면 회문이 되는 유사회문입니다.
