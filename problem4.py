res = 9009

def is_palindrome(mul):
    return str(mul) == str(mul)[::-1]

for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        mul = i*j
        if is_palindrome(mul):
            res = max(res, mul)
            break

print(res)
