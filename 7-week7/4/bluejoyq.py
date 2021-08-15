import sys 
input = sys.stdin.readline
MAX = sys.maxsize
class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            try:
                cur = cur[char]
            except:
                cur[char] = {}
                cur = cur[char]
        cur[0] = 0
     
    def find(self, target):
        T =  len(target)
        cache = [MAX] * (T + 1)
        cache[0] = 0

        for i in range(T):
            if cache[i] == MAX:
                continue
            cur = self.root
            for j in range(i, T):
                char = target[j]
                try:
                    cur = cur[char]
                except:
                    break
                try:
                    # 여기서 끝나는 애가 있으면.
                    tmp = cur[0]
                    cache[j + 1] = min(cache[j + 1], cache[i] + 1)
                except:
                    continue
        if cache[-1] == MAX:
            return -1
        return cache[-1]

def solve():
    N = int(input())
    target = input().rstrip() 
    trie = Trie()
    for i in range(N):
        trie.add(input().rstrip())

    return trie.find(target)
print(solve())