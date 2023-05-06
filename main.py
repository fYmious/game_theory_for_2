def f(s1, s, c, m):
    if 60 <= s + s1 <= 79: return c % 2 == m % 2
    if s + s1 > 79: return c % 2 != m % 2
    if c == m: return 0
    h = [f(s1 + 1, s, c + 1, m), f(s1 * 3, s, c + 1, m), f(s1, s + 1, c + 1, m), f(s1, s * 3, c + 1, m)]
    if (c + 1) % 2 == m % 2:
        return any(h)
    else:
        return all(h)


for s in range(1, 52):
    for m in range(1, 10):
        if f(8, s, 0, m) == 1:
            print(s, m)
            break
