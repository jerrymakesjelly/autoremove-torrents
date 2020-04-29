import time

def convert_timestamp(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
