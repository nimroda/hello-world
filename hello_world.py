import time

outFileName="/data/test.txt"
outFile=open(outFileName, "w")
outFile.write("Hello World!")
outFile.close()

time.sleep(60)
