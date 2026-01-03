import time


def jiance(jc_time):
    def wrapper(*args):
        start = time.time()
        result = jc_time(*args)
        time.sleep(2)
        end = time.time()
        print("所耗时间：", end - start, "秒")
        return result

    return wrapper


@jiance
def number_sum2(a, b):
    sum = a + b
    print(sum)
    return sum


@jiance
def number_sum3(a, b, c):
    sum = a + b + c
    print(sum)
    return sum


ss = number_sum2(4, 5)
ss = number_sum3(4, 5, 6)

# number_sum(4,5)
