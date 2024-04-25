import multiprocessing

def calculate_square(number, counter, lock):
    """Function to calculate and return the square of a given number.
    It also increments a shared counter using a lock for synchronization."""
    square = number * number
    with lock:  # Use the lock to ensure safe update to the shared counter
        counter.value += 1
    return square

def main():
    # List of numbers to calculate the square of
    numbers = [1, 2, 3, 4, 5]
    
    # Create a manager for managing shared data
    manager = multiprocessing.Manager()
    
    # Create a shared Value (integer) and a Lock using the manager
    counter = manager.Value('i', 0)
    lock = manager.Lock()
    
    # Create a pool of workers
    with multiprocessing.Pool() as pool:
        # Prepare arguments for each task, passing the shared counter and lock
        task_args = [(number, counter, lock) for number in numbers]
        
        # Use starmap_async to apply `calculate_square` to each set of arguments
        result_async = pool.starmap_async(calculate_square, task_args)
        
        # Wait for all results to be ready and retrieve them
        squares = result_async.get()  # This blocks until the result is ready
        
        print("Squares:", squares)
        print("Total calculations performed:", counter.value)

if __name__ == "__main__":
    main()
