import math


def expectation(*args):
    mp1 = [i for i in args]
    res1 = sum(mp1) / len(mp1)
    res2 = sum(((i - res1) ** 2) for i in args)
    res3 = math.sqrt(res2)
    res4 = res3 / res1

    print('математическое ожидание:', round(res1, 2))
    print('дисперсия:', round(res2, 2))
    print('среднеквадратическое отклонение:', round(res3, 2))
    print('коэффициент вариации:', round(res4, 2))



expectation(2,8,7)
