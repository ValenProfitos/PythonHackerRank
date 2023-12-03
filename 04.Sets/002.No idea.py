N, M = input().split(), input().split()

A, B = set(input().split()), set(input().split())

HAPINESS = 0

for i in M:
    if i in A:
        HAPINESS += 1
    elif i in B:
        HAPINESS -= 1
    
print(HAPINESS)