n = int(input())
words = []
for i in range(n):
    words.append(input())


# sort
dictionary = sorted(words)

start = 0
end = n-1
count = 0
skip = 0

for word in words:
    start = 0
    end = n-1
    i = 0
    while i < len(word):
        # update count
        count += 1

        # update scope
        started = False
        for j in range(start, end+1):
            if dictionary[j][:i+1] == word[:i+1]:
                if not started:
                    start = j
                    started = True
                end = j

        # get skip
        valid = True
        for j in range(i+1, len(word)):
            for w in dictionary[start:end+1]:
                if len(w) <= j or w[j] != word[j]:
                    valid = False
                    break

            if valid:
                skip += 1
            else:
                break

        # update i
        i += skip + 1
        skip = 0

    # print count
    print(count)
    count = 0
