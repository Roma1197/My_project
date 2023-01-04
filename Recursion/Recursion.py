import os

path = 'C:/Users/Рома/PycharmProjects/pythonProject/Recursion/1/'
def list_recursive(path, level=1):
    for item in os.listdir(path):
        print(item)
    for item in os.listdir(path):
        if os.path.isdir(path+'\\'+item):
            print(' ' + item)
            list_recursive(path+'\\'+item, level+1)


list_recursive(path)