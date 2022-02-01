import time

timeout = time.time() + 3
while True:
    if time.time() > timeout:
        print("yeap")
        timeout = time.time() + 3
