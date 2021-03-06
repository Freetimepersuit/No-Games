
import time
import psutil

last_recevied = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_recevied + last_sent

while True:
    bytes_recevied = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_recevied + bytes_sent

    new_received = bytes_recevied - last_recevied
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total /1024 / 1024

    print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")

    last_recevied = bytes_recevied
    last_sent = bytes_sent
    last_total = bytes_total

    time.sleep(1)


