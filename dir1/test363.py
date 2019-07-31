
# import sys
# for p in sys.path:
#     print(p)
# '''
# import sys
#
# # C:\\Users\\bangong\\PycharmProjects\\untitled\\venv\\dir2\\calculator.py
# sys.path.append("C:\\Users\\bangong\\PycharmProjects\\untitled\\venv\\dir2")
# from calculator import add
#
# print(add(2, 3))
# '''
import sys
from os.path import dirname,abspath

project_path = dirname(abspath('__path__'))
print(project_path)
sys.path.append(project_path+'\\dir2')

from calculator import add
print(add(2,3))

