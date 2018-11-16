def fibonacci_generator(n):
    a = 0
    b = 1
    i = 1
    isOtr = False
    if n < 0:
        n = -n
        isOtr = True
    elif n == 0:
        yield 0

    while i < n:
        b = b + a
        a = b - a
        i += 1
        if (i % 2 != 0):
            if (isOtr == True):
                yield -a;
            else:
                yield a;
        else:
            yield a;


print(list(fibonacci_generator(10)))
print(list(fibonacci_generator(-10)))
