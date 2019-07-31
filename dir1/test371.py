# open("test.txt",'r')

# try:
#     open("test.txt",'r')
# except FileNotFoundError:
#     print("没有找到文件")

try:
    print(a)
    open("test.txt",'r')
except BaseException as msg:
    print(msg)