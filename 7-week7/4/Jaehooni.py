import sys
input = sys.stdin.readline
n = int(input())
string = input().rstrip()
str_len = len(string)
words = [input().rstrip() for i in range(n)]
word_tuple = []
matches = [[0 for i in range(str_len)] for i in range(str_len)]

for word in words:
    i = 0
    length = len(word)
    while True:
        i = string.find(word, i)
        if (i == -1):
            break

        if not (matches[i][i+length-1]):
            matches[i][i+length-1] = 1
            word_tuple.append((i, i+length-1))

        i += 1

word_tuple.sort(key=lambda x: (x[0], x[1]))
len_word_tuple = len(word_tuple)


def solve(start, end, index):
    if index >= len_word_tuple:
        pass

    elif start == 0 and end == str_len - 1:
        pass

    elif word_tuple[index][0] != end + 1:
        solve(start, end, index + 1)

    else:
        ns = word_tuple[index][0]
        ne = word_tuple[index][1]

        if (start == -1):
            solve(ns, ne, index + 1)
            solve(start, end, index + 1)

        else:
            if (matches[start][ne] == 1):
                pass

            elif (matches[start][ne] > 1):
                matches[start][ne] = min(matches[start][ne], matches[start][end] + 1)

            else:
                matches[start][ne] = matches[start][end] + 1

            solve(start, end, index + 1)
            solve(start, ne, index + 1)


solve(-1, -1, 0)

#print(word_tuple)
print(matches[0][str_len-1] if matches[0][str_len-1] else -1)