import sys
import time
from multiprocessing import Pool, Manager
import os

def print_progress_bar(completion_ratio):
    """Prints the progress bar to the console."""
    total_width=os.get_terminal_size().columns - 50
    filled_length = int(total_width * completion_ratio)
    bar = '=' * filled_length + '>' + ' ' * (total_width - filled_length)
    sys.stdout.write(f"\r(vscode) $[{bar}] {completion_ratio * 100:.2f}% complete")
    sys.stdout.flush()

def task(dummy, progress_counter, lock, total_tasks):
    """A dummy task that simulates some work by sleeping for a short duration."""
    for _ in range(10):  # Reduced work simulation steps for faster debugging
        time.sleep(1)  # Sleep to simulate work
        with lock:
            progress_counter.value += 1
    return None

def main():
    num_tasks = 5
    num_processes = 3
    manager = Manager()

    # Setup shared counter for progress
    progress_counter = manager.Value('i', 0)  # 'i' is for integers
    lock = manager.Lock()
    total_tasks = num_tasks * 10  # total work units
    print('I am main')
    # Create a pool of workers
    with Pool() as pool:
        # Using starmap to pass the shared counter to each task
        tasks = [(i, progress_counter, lock, total_tasks) for i in range(num_tasks)]
        result = pool.starmap_async(task, tasks)
        while not result.ready():
            with lock:
                completed = progress_counter.value
            print_progress_bar(completed / total_tasks)
            time.sleep(0.1)  # Update interval for progress bar

        print_progress_bar(1)  # Ensure 100% is shown at the end
        sys.stdout.write('\n')  # Move to next line at the end of progress

if __name__ == "__main__":
    main()
