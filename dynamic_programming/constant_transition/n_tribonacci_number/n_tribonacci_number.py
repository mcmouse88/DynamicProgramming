def tribonacci(n: int) -> int:
    if n < 3:
        return n if n < 2 else 1

    first, second, third = 0, 1, 1
    for i in range(3, n + 1):
        first, second, third = second, third, first + second + third
    return third
