import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()

# squares的值作为y轴，x轴的数字默认从0开始的整数
ax.plot(squares)

plt.show()