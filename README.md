# zmq-workers-boilerplate
A boilerplate for a client -> multiple workers tasks distribution. The client and workers threads and processes are dynamically launched based on a config.

How to use:

  1) Start the router by running python router.py.
  2) Start the worker by running python worker.py NUMBER_OF_WORKERS, where NUMBER_OF_WORKERS is the number of worker processes you want to start.
  3) Send a configurable number of requests from the client by running python client.py CLIENT_ID NUMBER_OF_REQUESTS, where CLIENT_ID is a unique identifier for the client and NUMBER_OF_REQUESTS is the number of requests you want the client to send.

Remember to install ZeroMQ and the Python bindings for ZeroMQ (pyzmq) before running the scripts. You can install these using pip:
pip install pyzmq
