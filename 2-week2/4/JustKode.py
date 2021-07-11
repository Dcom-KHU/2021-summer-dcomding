n = int(input())
list_var = []
dict_var = {}

for i in range(n):
    string = input()
    list_var.append(string)
    dict_var[string] = 0

start = 0
end = 0
current = 1
dict_len = len(dict_var)
r_s, r_e = 0, n - 1
dict_var[list_var[0]] = 1

if r_e - r_s > end - start and current == dict_len:
    r_s, r_e = start, end

while end < n:
    if current < dict_len:  # end 이동
        if end == n - 1:
            break
        end += 1
        if dict_var[list_var[end]] == 0:
            current += 1
        dict_var[list_var[end]] += 1
    elif end == n - 1 or current == dict_len:
        dict_var[list_var[start]] -= 1
        if dict_var[list_var[start]] == 0:
            current -= 1
        start += 1
    
    if r_e - r_s > end - start and current == dict_len:
        r_s, r_e = start, end

print(r_s + 1)
print(r_e + 1)