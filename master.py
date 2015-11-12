import os
import time
start = input("Enter Staring number : ")
end = input("Enter ending number : ")
count = start
for x in range(start,end):
    os.system("scrapy crawl gre -o issue_"+str(count)+" -t csv")
    count = count + 1
   # time.sleep(2)
