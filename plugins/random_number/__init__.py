import random
def get_coc_random_number(b, a=1, c=0,):
    result = 0
    for i in range(a):
        result += random.randint(1, b+1)
    return result +c