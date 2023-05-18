import zmq

def start_router():
    context = zmq.Context(1)
    frontend = context.socket(zmq.ROUTER)
    backend = context.socket(zmq.DEALER)

    frontend.bind('tcp://*:5570')  # Client connects here
    backend.bind('tcp://*:5571')  # Workers connect here

    zmq.proxy(frontend, backend)

if __name__ == "__main__":
    start_router()
