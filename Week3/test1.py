a = int(input())
a = str(format(pow(a, 0.5),'.3f'))
if len(a) > 30:
    print(a)
else:
    print(a.rjust(30, "+"))
