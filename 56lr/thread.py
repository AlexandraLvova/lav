import threading
from threading import Thread, BoundedSemaphore

#изменим программу , у нас доступно всего 5 самолетов на 100 шпионов,
# после возвращения одного самолета следующий шпион садится в самолет

from multiprocessing import Process
import random
import logging
from time import time,sleep
from threading import Thread,BoundedSemaphore
plain = BoundedSemaphore(value=4)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def walk_on_map(matrix ,matr ,procc_id, thread_id):
    lock = threading.Lock
    go = threading
    i = random.randrange(0,matr)
    j = random.randrange(0,matr)
    start_coord = [i,j]
    coord = []
    sum = 0
    with plain: #наш семафор
        sleep(2)
        while(True):
            if (procc_id == 0):
                if (i + 1 > matr):

                    print(f" Шпион {thread_id} ,начал странствия с {start_coord} нашел {sum} целей, их координаты {coord}")
                    break
                elif (i+1<=matr):
                    if matrix[i+1][j] == 1:
                        sum = sum + 1
                        coord.append([i+1 , j])
                        i = i + 1
                    else:
                        i = i + 1
            elif (procc_id == 1):
                if (j + 1 > matr):
                    print(f" Шпион {thread_id} ,начал странствия с {start_coord} нашел {sum} целей, их координаты {coord}")
                    break
                elif(j +1 <=matr):
                    if matrix[i][j+1] == 1:
                        sum = sum + 1
                        coord.append([i , j+1])
                        j = j + 1
                    else:
                        j = j + 1
            elif (procc_id == 2):
                if (i - 1 < 0):
                    print(f" Шпион {thread_id} ,начал странствия с {start_coord} нашел {sum} целей, их координаты {coord}")
                    break
                elif (i - 1 >= 0 ):
                    if matrix[i-1][j] == 1:
                        sum = sum + 1
                        coord.append([i-1 , j])
                        i = i - 1
                    else:
                        i = i - 1
            elif (procc_id == 3):
                if (j - 1 < 0):
                    print(f" Шпион {thread_id} ,начал странствия с {start_coord} нашел {sum} целей, их координаты {coord}")
                    break
                elif (j - 1 >= 0 ):
                    if matrix[i][j-1] == 1:
                        sum = sum + 1
                        coord.append([i , j-1])
                        j = j - 1
                    else:
                        j = j - 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == '__main__':
    matr = random.randrange(5,10)
    x = random.randrange(1,100)
    matrix = []*matr
    print(matr)
    A = []
    for i in range(matr):
        A.append([0] * matr)
    # print(A)
    for i in range(matr):
        for j in range(matr):
            tmp = random.randrange(1,100)
            A[i][j]= 1 if tmp>x else 0
    for item in range(matr):
        print(A[item])
    procs = []
    for item in range(20):
        # создание потока
        proc = Thread(target=walk_on_map, args=(A, matr-1, item%4,item+1))
        procs.append(proc)
        proc.start()

