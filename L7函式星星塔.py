def star(x):
    for i in range(x+1):
        print('*'*(x-i))
def star2(x):
    for i in range(x+1):
        print('*'*i)
star2(int(input('星星塔')))
star(int(input('星星塔')))