def non_repeat_substr(s):
    win = set()
    i, j, n = 0, 0, len(s)
    best_i, best_j = 0, 0
    for j in range(n):
        print(f'j = {j}, s[j]={s[j]}, win={win}')
        if s[j] not in win:
            win.add(s[j])
            if j - i + 1 > best_j - best_i:
                best_i, best_j = i, j+1
            continue
        while i < j:
            print(f'i = {i}, s[i] = {s[i]}')
            win.remove(s[i])
            if s[i] == s[j]:
                i += 1
                break
            i += 1
        win.add(s[j])
    return s[i:j]

res = non_repeat_substr('sfsdf2sd3fqwertsm')
print(res)
assert res == 'd3fqwertsm'

