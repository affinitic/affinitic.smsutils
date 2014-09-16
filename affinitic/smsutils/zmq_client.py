#
#   Request-reply client in Python
#   Connects REQ socket to tcp://localhost:5559
#   Sends "Hello" to server, expects "World" back
#
import zmq
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    return parser.parse_args()


def main():
    args = get_args()

    # Prepare our context and sockets
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.99.115:5555")

    socket.send(args.message)
    message = socket.recv()
    print("Received reply %s" % message)