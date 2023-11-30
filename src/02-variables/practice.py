# 习题

### 运行下面的代码，思考为什么会这样？总结一下在哪些情况下两个不同的变量会有相同的id？

a = 256
b = 256
print(id(a), id(b))
print(a is b)

a = 257
b = 257
print(id(a), id(b))
print(a is b)