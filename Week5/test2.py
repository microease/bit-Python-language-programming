# 连续质数计算
# 描述
# 补充编程模板中代码，完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
#
# 获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
#
# 注意：用户输入的数字N可能是浮点数，都是正数；最后一个输出后不用逗号。


def prime(m):
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_ + 1 if n_ < n else n_
count = 5
while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count = count - 1
    n_ = n_ + 1
