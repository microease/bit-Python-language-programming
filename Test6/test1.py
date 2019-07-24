# 第一题 数字不同数之和
# 描述‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬
# 获得用户输入的一个整数N，输出N中所出现不同数字的和。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬
#
# 例如：用户输入 123123123，其中所出现的不同数字为：1、2、3，这几个数字和为6。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫
#
# 输入输出示例
# 输入	输出
# 123123123	6
# 解答代码
# 思路：用N接收输入的数字字符串，接着利用set()转为集合去重，最后迭代集合求和。这里要注意要把字符串类型转化为数字类型，不然会报错。

# 数字不同数之和
N = input()
st = set(N)
sum = 0
for i in st:
    sum += int(i)
print(sum)

d= {'a': 1, 'b': 2, 'b': '3'}
print(d['b'])