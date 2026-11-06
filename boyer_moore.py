def boyer_moore(text, p):
    
    n = len(text)
    m = len(p) 
    last = {}
    for i in range(m):
        last[p[i]] = i
    s = 0
    
    while s <= n - m:
        j = m - 1
        while j >= 0 and p[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        c = text[s + j]
        s += max(1, j - last.get(c, -1))

    return -1
text = "ԳԱԶԱՆԱՆՈՑ"
p = "ԶԱՆ"
result = boyer_moore(text, p)
print(result)