import os.path
import time

save_path = '/data'
completeName = os.path.join(save_path, "test.txt")         
file1 = open(completeName, "w")
toFile = raw_input("Hello World!")
file1.write(toFile)
file1.close()
        
time.sleep(300)
