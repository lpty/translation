import random

def randomChose(lis):
    '''
    chose random item in list
    '''
    item = lis[random.randint(0, len(lis) - 1)]
    return item