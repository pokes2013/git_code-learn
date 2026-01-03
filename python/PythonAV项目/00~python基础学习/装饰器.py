import time

def number_sum(a, b):
    sum = a + b
    # print(sum)
    return sum


# sum(2, 3)


def time_js(a, b):
    start = time.time()
    r = number_sum(a, b)
    time.sleep(2)
    print("结果为：",r)
    end = time.time()
    print("所耗时间：", end - start)

time_js(5,6)
