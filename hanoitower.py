def hanoi(n,fr,by,to,c):

    if n == 1:
        move(fr, to, n)
        print(c)
    else:
        hanoi(n-1, fr, to, by, c+1)
        move(fr, to, n)
        hanoi(n-1, by, fr, to, c+1)
        

def move(a, b, n):

    print(n, '이동', a, '->', b)

c = 0
hanoi(12,'A','B','C', c)

