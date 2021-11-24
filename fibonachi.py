def max_sequence():

    curr = 0
    highscore = 0

    arr = [5, 1, 3, -7, 3, -5]

    for number in arr:
        curr += number
        curr = max(curr, 0)
        highscore = max(highscore, curr)


cache = {}


def fib(n):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
        print(cache[n])
    return cache[n]


print(fib(50))
max_sequence()
