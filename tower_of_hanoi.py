#Author:- Nikhil Balwani Parshwa Shah

class Stack:                                             # Substitute class for stack
     def __init__(self):
         self.items = []
     
     def is_empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
     def __getitem__(self, i):
         return self.items[i]

beg = Stack()                                           # Begginging Stack
aux = Stack()                                           # Auxiliary Stack
des = Stack()                                           # Destination Stack

# Prints the stacks
def print_stacks():
    print "Beg",
    for i in range(0, beg.size()):
        print beg[i], " ",
    print ""
    
    print "Aux",
    for i in range(0, aux.size()):
        print aux[i], " ",
    print ""
    
    print "Des",
    for i in range(0, des.size()):
        print des[i], " ",
    print ""

n = int(raw_input("Enter number of disks\n>> "))        # Input: Number of disks
temp = n

while temp > 0:                                         # Adding the values of disks to the beggining Stack
    beg.push(temp)
    temp -= 1                                           # Decrementing by 1 unit on each iteration

def tower_of_hanoi(n, beg, aux, des):                   # Recursive Function to solve Tower Of Hanoi Problem
    if n == 1:
        des.push(beg.pop())                             # Pushing the top disk from beg peg to des peg
        print_stacks()
        print ""
        return None
        
    tower_of_hanoi(n - 2, beg, des, aux)                # Moving n - 1 disks to auxiliary peg using recursive call
    save1 = beg.pop()                                   # Pushing the top disk from beg peg to des peg
    save2 = beg.pop()
    
    des.push(save2)
    des.push(save1)
    
    print_stacks()
    print ""
    tower_of_hanoi(n - 2, aux, beg, des)                # Moving n - 1 disks to destination peg using recursive call
    return None

print "The tower of hanoi problem can be solved as below:- \n"

tower_of_hanoi(n, beg, aux, des)                        # Function call
