from abc import ABC,abstractmethod
class absclass(ABC):

    def print(self, x):
        print(x)

    @abstractmethod
    def task(self):
        print("we are inside absclass")

class task_class(absclass):
    def task(self):
         print('we are inside task class ')

taskobj = task_class()
taskobj.task()
taskobj.print(100)