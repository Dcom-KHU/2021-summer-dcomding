groups = dict()

def search(f):
    global groups
    if sum(map(bool, groups.values())):
        if f in groups.keys():
            for t in sorted(sorted(groups[f]), key=lambda x: len(x)):
                groups[f].remove(t)
                result = search(t)
                if result:
                    return [f] + result
                else:
                    groups[f].append(t)
        return False
    else:
        return [f]

n = int(input())
tickets = [list(map(int, input().split()))for i in range(n)]

for t in tickets:
    if t[0] in groups.keys():
        groups[t[0]].append(t[1])
    else:
        groups[t[0]] = [t[1]]

print(' '.join(search('ICN')))
