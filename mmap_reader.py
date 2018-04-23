import mmap, os, time
mx = mmap.mmap(os.open('test_mmap',os.O_RDWR), 1)
last = None

while True:
    mx.resize(mx.size(  ))
    data = mx[:]
    if data != last:
        print(data)
        last = data
    time.sleep(1)
    if (data == b'q'):
        print("Shut'n me-self down")
        mx.close()
        os._exit(0)
