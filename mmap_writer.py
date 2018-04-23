from time import sleep
import os, mmap


mx = mmap.mmap(os.open('test_mmap',os.O_RDWR), 1)
while True:
    data = input('Enter some text:')
    if (data != 'q'):
        try:
            fileob.seek(0)
            fileob.write(data)
            fileob.truncate(  )
            fileob.flush(  )
        except:
            sleep(.025)
    else:
        fileob.seek(0)
        fileob.write(data)
        fileob.truncate(  )
        fileob.flush(  )
        sleep(1)

        fileob.seek(0)
        fileob.write("")
        fileob.close()
        sleep(1)

        os.remove('test_mmap')
        os._exit(0)
    
    
