import zmq
import sys
import time
import threading

def client_thread(id, request):
    context = zmq.Context.instance()
    client = context.socket(zmq.REQ)
    client.identity = u"Client-{}-{}".format(id, request).encode("ascii")
    client.connect('tcp://localhost:5570')

    print(f"Client-{id}-{request} is sending request {request}")
    start_time = time.time()  # Time before sending the request
    client.send_string(str(request))
    response = client.recv()
    end_time = time.time()  # Time after receiving the response
    request_time = end_time - start_time  # Time taken for this request
    print(f"Client-{id}-{request} received reply {response.decode('utf-8')} in {request_time} seconds")

def client(id, n_requests):
    start_time = time.time()

    threads = []
    for i in range(n_requests):
        t = threading.Thread(target=client_thread, args=(id, i))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Client-{id} total send and receive time: {total_time} seconds")

if __name__ == "__main__":
    id = sys.argv[1]  # Client ID
    n_requests = int(sys.argv[2])  # Number of requests
    client(id, n_requests)
