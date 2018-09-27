i=1
while i<=3:
    zhanghao = input('请输入账号:')
    mima = input('请输入密码:')
    if zhanghao=='seven' and mima=='123':
        print('登陆成功')
        break
    else:
        print('账号或者密码错误')
        i+=1
else:
    print('账号被锁定')
