import zmq
from constCS import * #-
context = zmq.Context()

p1 = "tcp://"+ HOST +":"+ PORT1 # how and where to connect
s  = context.socket(zmq.REQ)    # create request socket

s.connect(p1)                   # block until connected
s.send("Hello world")           # send message
message = s.recv()              # block until response
s.send("STOP")                  # tell server to stop
print message                   # print result
