import zmq
import time
import sys
from multiprocessing import Process
import random

def worker_process(id):
    context = zmq.Context(1)
    worker = context.socket(zmq.REP)
    worker.connect('tcp://localhost:5571')

    while True:
        request = worker.recv_string()
        print(f"Worker-{id} received request {request}")
        #sleep_time = random.randint(1, 10)  # Random sleep time between 1 and 10 seconds
        sleep_time = 1
        time.sleep(sleep_time)
        worker.send_string(request)

def start_workers(n_workers):
    for i in range(n_workers):
        Process(target=worker_process, args=(i,)).start()

if __name__ == "__main__":
    n_workers = int(sys.argv[1])  # Number of worker processes
    start_workers(n_workers)
