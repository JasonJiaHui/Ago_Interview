
'''
MinStack and MinQueue have same idea !!!
'''

class MinStack:
    def __init__(self):
        self.stack1 = []
        self.minStack2 = []

    def mypush(self, val):
        self.stack1.append(val)
        if not self.minStack2:
            self.minStack2.append(val)
        else:
            tail = self.minStack2[-1]
            if tail < val:
                self.minStack2.append(tail)
            else:
                self.minStack2.append(val)

    def mypop(self):
        if self.stack1:
            self.stack1.pop()
            self.minStack2.pop()

    def getMin(self):
        if self.minStack2:
            return self.minStack2[-1]

