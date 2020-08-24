import threading
from datetime import datetime
from my_devices10 import network_devices
from my_functions10 import ssh_conn
from my_functions10 import print_show
from my_functions10 import print_show_no_loop

def main():

    total_start_time = datetime.now()


    
    cmd = "show version"
#    print_show(cmd) 

    threads = []

    for a_device in network_devices:
        # This line calls the threading library and spawns a new thread
        # Target = function defined above, no (), it's not calling the function
        # it's just referencing it
        # my_thread = threading.Thread(target=print_show, args=(a_device))
        t = threading.Thread(target=print_show_no_loop, args=(a_device, "show version"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_end_time = datetime.now()
    print("Elapsed time was:", (total_end_time - total_start_time))

if __name__ == "__main__":
    main()
