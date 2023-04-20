import time
import timeit


def create_list_using_for_loop(number):
    return [str(num) for num in range(number)]


def create_list_using_map(number):
    return list(map(str, range(number)))


def timing_code_using_time():
    print("ELAPSED USING FOR LOOP")
    start_time = time.time()
    result = create_list_using_for_loop(1000000)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

    print("ELAPSED USING MAP")
    start_time = time.time()
    result = create_list_using_map(1000000)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)


def timing_code_using_time_it():
    print("ELAPSED USING FOR LOOP")
    statement = '''create_list_using_for_loop(100)'''
    setup = '''def create_list_using_for_loop(number):
        return [str(num) for num in range(number)]'''

    execution_time = timeit.timeit(statement, setup, number=1000000)
    print("Execution time:", execution_time)

    print("ELAPSED USING MAP")
    statement = '''create_list_using_map(100)'''
    setup = '''def create_list_using_map(number):
        return list(map(str, range(number)))'''

    execution_time = timeit.timeit(statement, setup, number=1000000)
    print("Execution time:", execution_time)


def divider(title):
    print(f"=========={title.upper()}==========")


if __name__ == '__main__':
    divider("timing code using time")
    timing_code_using_time()

    divider("timing code using time-it")
    timing_code_using_time_it()
