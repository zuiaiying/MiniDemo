#简单工厂模式
#简单工厂模式（simple factory pattern）：是通过专门定义一个类来负责创建其他类的实例，
# 被创建的实例通常具有共同的父类

class Operation(object):
    """
    四则运算的父类，接受用户输入的数值
    """
    def __init__(self,number1=0,number2=0):
        self.number1=number1
        self.number2=number2


    def GetResult(self):
        pass
    pass

class OperationAdd(Operation):
    def GetResult(self):
        return self.number1+self.number2



class OpreationSub(Operation):
    def GetResult(self):
        return self.number1- self.number2


class OperationMul(Operation):
    def GetResult(self):
        return self.number1 * self.number2

class OperationDiv(Operation):
    def GetResult(self):
        if self.num2 == 0:
            return '除数不能够为零'
        return 1.0*self.number1/self.number2

class OperationUndef(Operation):
    def GetResult(self):
        return '操作符错误'


#简单工厂类
class OpreationFactory(object):
    def choose_oper(self,ch):
        if ch == '+':
            return OperationAdd()
