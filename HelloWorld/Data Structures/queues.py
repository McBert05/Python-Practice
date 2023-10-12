# queues resemble a waiting line or a queue in the real world
# the first person in the queue is the first person that will receive service
# this behavior is referred to as First In First Out (FIFO)
# queues work like so:
# [1, 2, 3] (preorganized queue)
# [2, 3]
# [3]
# []
# as you can see elements need to be shifted to the left once a element has been served
# this can be problematic when many items are present in the queue
# in these situation it is more efficient to use a 'deque' object
# first we need to import 'deque' from the collections module the syntax for this is:
from collections import deque
# instead of defining a variable an setting it to an empty list, we should wrap this list with a dequeu object 
queue = deque([])
# the deque object has many similar methods that we have in the list object like 'append'
queue.append(1)
queue.append(2)
queue.append(3)
# to remove an item from the beginning of the queue we call the 'popleft' method
queue.popleft()
print(queue)

# we can also check for an empty queue by using the 'not' operator
if not queue:
    print("empty")
