# 02：Python变量

## Python变量

- Python可以自动推断变量的类型
- Python变量不是盒子，而是标签
- Python变量命名规则（P429关键字）

## 字符串

- 使用单引号或者双引号来创建字符串
  - 'This is a string.'
  - "This is also a string."
- title方法：将单词的首字母大写
- 将字符串改为全部大写或者小写: upper(), lower()
- f字符串: full_name = f'{first_name} {last_name}' # Python 3.6+
- 字符串中的转义字符：制表符'\t', 换行'\n'
- 删除空白: rstrip(), lstrip(), strip()

## 数

- 整数（int）： 没有区分长度（没有int32， int64，long），从Python 3.8开始没有最大值的限制
- 浮点数(float): 没有区分单精度和双精度
- int和float的实际长度会根据机器平台来决定，绝大多数情况下为64位，8个字节
- 基本运算： +， -， *,  /
- 乘方运算:  **
- 模运算（求余数）： %
- 除法求商： //
- 求商和余数: divmod函数
- round函数：对小数部分四舍五入
- 上面所有的运算都支持：正数、负数、小数、虚数
- 为什么.3+.1不等于.4？因为浮点数的精度位数有限，大部分浮点数使用2进制在内存中都是近似值。
- 数字中的下划线： universe_age = 14_000_000_000
- 科学计数法：universe_age = 1.4e10

## 变量的函数

- str()函数：将其他数据转化为字符串
- int()函数：将其他数据转化为整数
- float()函数：将其他数据转化为浮点数
- type函数: 返回该变量的类型
- id函数： 返回该变量的id，这是一个int类型的值，可以看作是变量的值保存的地址
- isinstance函数：如果该变量是某类型的实例，返回True，否则返回False
- 简单类型变量（str,int,float）都是不可变的，如果进行改变简单变量的操作，实际上是创建了新的变量
- 从-5到256的整数作为被常用的整数会被缓存起来，这些整数的id总是相同的
- 简单字符的字符串也会被缓存起来

## Python之禅

- 运行命令: `import this`
- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Programs must be written for people to read, and only incidentally for machines to execute.
- 使用 # 来编写python代码注释
