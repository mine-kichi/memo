'''
Created on 2017/07/09

@author: mine
'''
class Dog(object):
    def __init__(self, name):
       self.name = name

class UltraDog(Dog):
    def __init__(self, name, type):
        super(UltraDog, self).__init__(name)
        self.type = type


if __name__ == '__main__':
    ud1 = UltraDog("taro", "akita")
    print(ud1.type)
