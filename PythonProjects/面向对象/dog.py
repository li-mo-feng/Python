class Dog:
    def __init__(self,name):
        self.name=name


    def bulk(self):
        print("%s:汪汪汪"% self.name)


d1= Dog("老师")
d1.bulk()