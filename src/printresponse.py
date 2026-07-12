import time
import sys

def printresponse(response, stream_speed):
    for char in response:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(stream_speed)
