# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(len(d))
# TODO: deques can be iterated over
for i in d:
    print(i.upper())
# TODO: manipulate items from either end
d.pop()
d.popleft()
d.append(6)
d.appendleft(10)
print(d)
# TODO: use an index to get a particular item
d.rotate(1)
print(d)