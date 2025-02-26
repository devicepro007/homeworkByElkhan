import time

def timeFunction(func, *args):
    start_time = time.time()
    func(*args)
    execution_time = time.time() - start_time
    return execution_time

amount_of_functions = 1

def example(example_text):
    print(example_text)
    time.sleep(0.0001)

while True:
    try:
        for i in range(amount_of_functions):
            execution_time = timeFunction(example, "This is an example")
            print(f"\nExecution Time: {execution_time:.5f}s")
        break

    except:
        print("Oops! Something went wrong...\n\n")