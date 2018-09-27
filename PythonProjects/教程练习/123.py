import os

path = 'F:\音乐'
list = [path]  # 列表值为路径
while len(list) == 0:  # 判断列表是否为空
    print("该路径下没有文件")
else:  # 如果列表不是空,那么选取列表内的值
    for i in list:  # 再列表内遍历,赋予i的值为列表内的地址
        if os.path.isfile(i):  # 用os内的方法isfile判断该地址下是否是文档
            # 如果是文档那么输出文档名字
            # print(list)
            file1 = i.split("\\")[-1]
            # print(file1)
            file2=file1.split(".")[-1]
            # print(file2)
            if "wav" and "mp3" and "flac" in file2:
                f = open("F:\音乐\车目录.txt", "a+", encoding="UTF-8")
                f.write(file2 + '\n')
                f.flush()
                print("名字是:" + i)

        else:  # 如果不是文档
            name = os.listdir(i)  # 那么查出该路径下次级目录的文件名,因为name的类型是列表
            for s in name:  # 从新的列表中遍历次级目录的名字
                newpath = os.path.join(i, s)  # 那么用上级目录地址i和次级目录进行组合,形成新的地址
                # 将新的地址放入列表,进行上一级的遍历....返回值是一个列表
                list.append(newpath)