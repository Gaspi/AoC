
with open('./input.txt', 'r') as file:
    data = [int(n) for n in file.read().split(' ')]

_memo = {}
def blink(stone, n):
    if (stone, n) in _memo:
        return _memo[(stone, n)]
    res = None
    if n == 0:
        res = 1
    else:
        sstone = str(stone)
        if stone == 0:
            res = blink(1, n-1)
        elif len(sstone) %2 == 0:
            stone1 = int( sstone[:len(sstone)//2] )
            stone2 = int( sstone[len(sstone)//2:] )
            res = blink(stone1, n-1) + blink(stone2,n-1)
        else:
            res = blink(stone * 2024, n-1)
    _memo[(stone, n)] = res
    return res

print(sum(blink(c, 25) for c in data))

print(sum(blink(c, 75) for c in data))
