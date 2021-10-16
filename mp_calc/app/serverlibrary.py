def merge(array, p, q, r):
    
    start, middle, end = p,q,r
    aleft = array[start:middle+1]
    nleft = len(aleft)
    
    aright = array[middle+1 : end+1]
    nright = len(aright)
    
    left,right, dest = 0,0,start
    
    while (left < nleft and right < nright) :
        if (aleft[left] < aright[right]):
            array[dest] = aleft[left]
            left = left+1      
        else : 
            array[dest] = aright[right]
            right = right+1    
        dest = dest+1
        
    while left<nleft:
        array[dest]= aleft[left]
        left = left+1
        dest = dest+1
        
    while right<nright:
        array[dest]= aright[right]
        right = right+1
        dest = dest+1

def mergesort_recursive(array, p, r):
    
    start,end = p,r
    length = end - start + 1
    
    if (length > 1):
        middle = int((end+start)/2)
        mergesort_recursive(array, start,middle)
        mergesort_recursive (array, middle+1, end)
        merge(array,start,middle,end)

def mergesort(array, byfunc=mergesort_recursive()):
  array = list[get_smallest_three()]
                     
    
def mergesort(array):
    if (len(array)) <= 1:
        return (array)
      
    else : 
        mergesort_recursive(array,0, len(array)-1)
        return array

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