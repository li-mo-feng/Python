import pymysql
class EmployeeCURD:
    def __init__(self):
        pass


    @classmethod#直接使用类名调用函数
    def conn(cre):
        conn = pymysql.connect("localhost", "root", "root", "test", charset="utf8")
        cur = conn.cursor()
        return cur,conn
    @classmethod#直接使用类名调用函数
    def insert(cre,employee):
        # num, Name1, addr, Zip, Tel, Email, Depno, SEX, Birth

        num = employee.getnum()
        Name1=employee.setName1()
        addr=employee.setaddr()
        Zip=employee.getZip()
        Tel=employee.getTel()
        Email=employee.getEmail()
        Depno=employee.getDepno()
        SEX=employee.getSEX()
        Birth=Employee.getBirth()



        sql1="insert into employee values(%d,%s,%s,%s,%d,%s,%d,%s,%s)"%\
             (num, Name1, addr, Zip, Tel, Email, Depno, SEX, Birth)






























class employee():
    def __init__(self,num,Name1,addr,Zip,Tel,Email,Depno,SEX,Birth):#私有化属性
        self.__num=num
        self.__Name1=Name1
        self.__addr = addr
        self.__Zip = Zip
        self.__Tel = Tel
        self.__Email = Email
        self.__Depno = Depno
        self.__SEX = SEX
        self.__Birth = Birth

    def getnum(self):#定义一个获得num的值的方法
        return self.__num#返回私有化属性num的函数
    def setnum(self,num):#定义赋值方法
        self.__num=num#给返回的私有化属性的属性赋值

    def getName1(self):
        return self.__Name1
    def setName1(self,Name1):
        self.__Name1=Name1

    def addr(self):
        return self.__addr
    def setaddr(self,addr):
        self.__addr =addr

    def getZip(self):
        return self.__Zip
    def setZip(self,Zip):
        self.__Zip =Zip

    def getTel(self):
        return self.__Tel
    def setTel(self, Tel):
        self.__Tel =Tel
     # self, num, Name1, addr, Zip, Tel, Email, Depno, SEX, Birth
    def getEmail(self):
        return self.__Email
    def setEmail(self, Email):
        self.__Email =Email

    def getDepno(self):
        return self.__Depno
    def setDepno(self,Depno):
        self.__Depno=Depno

    def getSEX(self,SEX):
        return self.__SEX
    def setSEX(self,SEX):
        self.__SEX=SEX


    def getBirth(self):
        return self.__Birth
    def setBirth(self,Birth):
        self.__Birth=Birth









