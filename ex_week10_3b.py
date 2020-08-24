from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from my_devices10 import network_devices
from my_functions10 import ssh_conn2

def main():

    start_time = datetime.now()
    #cmd = "show version"
    max_threads = 8
    
    # instantiate an object from the concurrent.futures library we imported
    pool = ThreadPoolExecutor(max_threads)
    # 'submit' and action to the newly defined pool, which starts 2nd thread
    #future = pool.submit(ssh_conn2, network_devices[0])
    
    # Add new list
    future_list = []

    # Loop through every device in imported device_list
    for a_device in network_devices:
        # start a thread for each device, bound by 'max_threads'. As they complete,
        # next will start (ThreadPool handles waiting and enforcing how many threads
        # are running, and when to start a new one. Results put in list
        future = pool.submit(ssh_conn2, a_device)
        future_list.append(future)

    # wait for all pending threads to finish
    wait(future_list)

    # This is the spot where the results of the child threads are passed back
    # to the main thread
    for future in as_completed(future_list):
        print("\n\n\n\n\n", "=" * 50)
        print("Result: " + future.result())

    end_time = datetime.now()
    print("Elapsed time was:", (end_time - start_time))

if __name__ == "__main__":
    main()
