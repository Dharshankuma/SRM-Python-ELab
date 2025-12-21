# Laaslya is planning to go to the cinema theater to spend her weekend vacation. Her friends Tina, Caleb, and J
# ocelyn all knew about Laasya's plan. They say we are coming too, but she thinks to ignore them because only 
# Laasya has enough money to pay for the cinema ticket.
# Laasya is very good at programming, so she puts up a puzzle to avoid taking her friends to the cinema. 
# She also says that those who have finished this can come with me.
# The puzzle is Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 

# The objective of the puzzle is to move the entire stack to another rod. the number of the disk will be given as 
# input obeying the following simple rules:

# 1) Only one disk can be moved at a time.
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. 
# a disk can only be moved if it is the uppermost disk on a stack.
# 3) No disk may be placed on top of a smaller disk.


def tower_of_hanoi(n, source, destination, auxiliary):
    if n==1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        return
    
    tower_of_hanoi(n-1, source, auxiliary, destination)
    
    print(f"Move disk {n} from source {source} to destination {destination}")
    
    tower_of_hanoi(n-1, auxiliary, destination, source)

n = int(input())
tower_of_hanoi(n, 'A', 'B','C')