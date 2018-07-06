def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num


def get_multiples(mod=1, length=10):
    count = 1
    while count < length+1:
        yield count * mod
        count += 1


def get_multiples2(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num
