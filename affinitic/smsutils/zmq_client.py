#
#   Request-reply client in Python
#   Connects REQ socket to tcp://localhost:5559
#   Sends "Hello" to server, expects "World" back
#
import zmq


def main():
    #  Prepare our context and sockets
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.1.1:5555")

    # TRAC lance ce script en asynchrone du trac, il ne se finira pas tant que le
    # raspberry n'aura pas repondu

    #  Do 10 requests, waiting each time for a response
    for request in range(1, 11):
        socket.send("Hello")
        message = socket.recv()
        print("Received reply %s [%s]" % (request, message))
