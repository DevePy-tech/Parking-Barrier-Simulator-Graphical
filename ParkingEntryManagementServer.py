import ParkingBarrierGate as parking
from time import sleep
from datetime import datetime
from multiprocessing.connection import Listener


def control_gate():
    print('Opening the gate...')
    parking.control_gate_arm("up")
    print('Waiting for the car passing...')
    sleep(5)
    print("Closing the gate...")
    parking.control_gate_arm("down")

def start_server():
    # Server
    listener = Listener(('localhost', 8080), authkey=b'PY C-2024')
    running = True
    while running:
        print(datetime.now())
        conn = listener.accept()
        print('Connection accepted from', listener.last_accepted)
        while True:
            msg = conn.recv()
            print(msg)
            if msg == 'close connection':
                conn.close()
                break
            if msg == 'close server':
                conn.close()
                running = False
                break
            if msg == 'ready to open':
                control_gate()      


parking.init()
start_server()

# Keep Turtle window open
parking.t.getscreen().mainloop()