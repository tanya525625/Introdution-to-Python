#Пример взят из http://easydan.com/arts/2016/pyfloats-comp/.
#При использовании разного количества разрядов для вещественных чисел

from mpmath import mp, mpf

def f(a, b):
    return (333.75 - a * a) * b ** 6 + a * a * (11 * a * a * b * b - 121 * b ** 4 - 2) + 5.5 * b ** 8 + a / (2.0 * b)


def f_true():
    for j in range(6, 50):
        mp.dps = j
        acc = 10 ** (-1)
        eps = 10 ** (-j + 5)
        a = mpf(77617)
        b = mpf(33096)
        ans = f(a, b)
        print(mp.dps, ans)
        if abs(f(a + eps, b + eps) - f(a - eps, b - eps)) < acc:
            break
    return ans
pass

f_true()