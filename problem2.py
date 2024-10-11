i = 1
j = 2
res = 0
while True:
    fib = i + j
    i = j
    j = fib
    if fib > 4000000:
        break
    if fib % 2 == 0: res += fib

print(res+2)