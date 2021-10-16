def mergesort(array, byfunc= None):
  pass

class Stack:

  def __init__(self):
    self.__items = []

  def queue(self,item):
    self.__items.append(item)
    
  def dequeue(self):
    if (len(self.__items) >= 1):
      return self.__items.pop()

  def peek(self):
    if (len(self.__items) >= 1):
      return self.__items[-1]
    
  @property
  def is_empty(self):
    return len(self.__items) == 0
  
  @property
  def size(self):
    return len(self.__items)
    
class EvaluateExpression:
  
    operands = "0123456789"
    operators = "+-*/"

    def __init__(self):
        self.expression = []
        self.stack = Stack()

    def input(self, item):
        self.expression.append(item)

    def evaluate(self):
        while len(self.expression) != 0:
            item = self.expression.pop()
            if item.isdigit():
                self.stack.push(int(item))
            elif len(item) == 1 and item in EvaluateExpression.operators:

                op1 = self.stack.pop() 
                op2 = self.stack.pop() 

                result = self.process_operator(op1, op2, item) 
                self.stack.push(result)

        return self.stack.pop()

    def process_operator(self, op1, op2, op):
        if op == "+":
            return op2 + op1
        elif op == "-":
            return op2 - op1
        elif op == "*":
            return op2 * op1
        elif op == "/":
            return op2 / op1
        else:
            return 0

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]