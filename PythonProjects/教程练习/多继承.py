class Father:
    def __init__(self):
        self.x=x
    money=100
    def play(self):
        print("先把作业作完")
class Mother:
    face="很好看"
    def play(self):
        print("随便玩")
class Son(Father,Mother):
    pass
s=Son()
print(s.face)
print(s.money)