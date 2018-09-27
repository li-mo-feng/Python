class Teacher():#先定义一个类,叫做老师

     def __init__(self,teacher_name,teacher_password):#然后初始化对象
         self.__name=teacher_name#这个对象有名字这个属性
         self.__password=teacher_password#这个名字有密码这个属性

 #因为这三个值为用户输入,所以需要传递给对象,也就是teacher
     def teacher_nameSet(self,teacher_name):
         self.__name=teacher_name
     def teacher_nameGet(self):
         return self.__name

     def teacher_passwordSet(self,teacher_password):
         self.__password=teacher_password
     def teacher_passwordGet(self):
         return self.__password




