def triangleQuest():
    """You are given a positive integer N . Print a numerical triangle of height N-1  like the one below:
    
        1
        22
        333
        4444
        55555
    """
    size = int(input('Enter your size: \t'))
    for num in range(size):
        for n in range(num):
            print(num, end=' ')
        print()


triangleQuest()