# Fibonacci Even Numbers Problem
# x = odd numbers [1,3,4,8,13]
# y = even numbers that end in a multiple of 2 [2,8,34]
# z = even numbers that end in 0 edge cases
limit = 4000000
count = 0
x = 1
y = 2
z = 0
total = 2

while total < limit:
    count = x + y
    z = x
    x = y
    y = count
    if count % 2 == 0:
        total += count

if count > limit:
    count -= z
    total -= count

print(total)

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s = sorted(s)
    t = sorted(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True