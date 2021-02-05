def fibonacci_series(num):
    x=0;y=1
    print(x,y,end=' ')
    i=2
    for i in range(2,10):
        c=x+y
        x=y
        y=c
        print(c,end=' ')

num=int(input("Enter the number: "))
fibonacci_series(num)