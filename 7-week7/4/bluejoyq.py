import sys 
from heapq import *
input = sys.stdin.readline

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
        # 0개 골랐고, 0번째 글자부터
        findings = []
        heappush(findings, (0,0))
        while findings:
            selected, start = heappop(findings)
            if start == len(target):
                return selected

            cur = self.root
            try:
                for i in range(start, len(target)):
                    char = target[i]
                    cur = cur[char]
                    try:
                        # 여기서 끝나는 애가 있으면.
                        cur[0]
                        heappush(findings, (selected + 1, i + 1))
                    except:
                        pass
            except:
                pass
        return -1

def solve():
    N = int(input())
    target = input().rstrip() 
    trie = Trie()
    for i in range(N):
        trie.add(input().rstrip())

    return trie.find(target)
print(solve())