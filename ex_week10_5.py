'''5. Using a context manager and a 'ProcessPoolExecutor', complete the same task as Exercise 4.'''

from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from my_devices10 import network_devices
from my_functions10 import ssh_conn2

def main():

    start_time = datetime.now()
    max_threads = 8

    # Loop through every device in imported device_list
    with ThreadPoolExecutor(max_threads) as pool:
        future_list = []
        for a_device in network_devices:
            future = pool.submit(ssh_conn2, a_device)
            future_list.append(future)
        
        for future in as_completed(future_list):
            print("Result: " + future.result())
            end_time = datetime.now()
            print(end_time - start_time)

if __name__ == "__main__":
    main()
