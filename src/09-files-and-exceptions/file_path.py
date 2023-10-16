# 在.py文件中，'.'代表的当前路径是vscode打开的工程的根目录

# 如何获取当前路径下的所有文件名
import os

# 获取到当前路径
current_dir = os.getcwd()
print(current_dir)

# 列举并打印当前路径下的所有文件名
files = os.listdir(current_dir)
print(files)