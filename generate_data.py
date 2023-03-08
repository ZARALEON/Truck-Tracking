import time
import os

def data(num):
    with open('./data.txt', 'a+') as file:
        file.write(str(num) + ',' + time.strftime('%H:%M:%S') + '\n')
        count = len(open('./data.txt','rU').readlines())
        if count>=30:
            file.truncate(0)
    file.close()
      
