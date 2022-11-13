import time


# def typical_generator(number):
#     print('Starting pur generator')
#     for i in range(number):
#         time.sleep(1)
#         yield i
#
#
# print(typical_generator(10))
# generator = typical_generator(10)
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())

def print_name(prefix):
    print(f'searching prefix {prefix}')
    while True:
        name = yield
        if prefix in name:
            print(name)


if __name__ == '__main__':
    coroutine = print_name('Dear')
    coroutine.send(None)
    # coroutine.__next__()
    coroutine.send('James')
    coroutine.send('Jacks')
    coroutine.send('Oleg')
    coroutine.send('Vasyl')
    coroutine.send('Dear James')
    coroutine.send('Dear Oleg')
    coroutine.send('Dear James')
    coroutine.close()