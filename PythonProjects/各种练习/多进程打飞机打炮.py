from multiprocessing import Process
def feiji():
    while True:
     print("打飞机")

def pao():
    while True:
     print("打炮")

if __name__=="__main__":
    p1=Process(target=feiji)
    p1.start()
    p2=Process(target=pao)
    p2.start()

