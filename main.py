import random
import threading
import time

def importUserNumbers(a, b):
    value = []
    for _ in range(11):
        value.append(random.randint(a, b))
    return value

startTime = time.time()
def maxNum(zoznam):
    num_max = max(zoznam)
    print(f"najvyssie cislo: {num_max}")
def minNum(zoznam):
    num_min = min(zoznam)
    print(f"najnizssie cislo: {num_min}")
def evenElements(zoznam):
    even = []
    for i in zoznam:
        if i % 2 == 0:
            even.append(i)
    print(f"Parne cisla zo zoznamu{even}")


zoznam = importUserNumbers(1, 999)



thread1 = threading.Thread(target=maxNum, args=(zoznam,))
thread2 = threading.Thread(target=minNum, args=(zoznam,))
thread3 = threading.Thread(target=evenElements, args=(zoznam,))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

trvanie = time.time() - startTime
print(f"trvanie pri 3ch vlaknach je {trvanie}")