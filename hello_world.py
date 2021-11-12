import time

lines = ['Hello World']
with open('test.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
        
time.sleep(30)
        
