import math
import random

if __name__ == '__main__':
    result = math.log(88, 10)
    print(result)
    check_result = 10 ** result
    print(check_result)

    print("GETTING RANDOM IN A LIST")
    array_list = list(range(1, 20))
    print(array_list)
    print(random.choice(array_list))

    print("SAMPLE WITH REPLACEMENT")
    result = random.choices(population=array_list, k=10)
    print(result)
    print("SAMPLE WITHOUT REPLACEMENT")
    result = random.sample(population=array_list, k=10)
    print(result)
