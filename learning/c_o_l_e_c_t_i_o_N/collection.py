import collections
from collections import Counter, deque, defaultdict, namedtuple, OrderedDict, ChainMap, UserList

a = ['7', '7', '9', '9', '9', 'hi']
b = Counter(a)
# print(b)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
r = deque(['hi', 'hey'])
r.append('hello')
r.appendleft('uh')
# print(r)
r.pop()
r.popleft()
# print(r)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
e = defaultdict(int)
e['number 1']
# print(e)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
w = OrderedDict()
w['1'] = 6
w['2'] = 5
w['3'] = 9
w['4'] = 1
w.move_to_end('4')
w.move_to_end('3')
w.move_to_end('2')
w.move_to_end('1')
# print(w.keys())

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Point = namedtuple('Point', ['x', 'y'])
o = Point(10, 22)
# print(o.y)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
y = {'hi': 9}
p = {'hey': 919}
t = ChainMap(y, p)


# print(t)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class My_List(UserList):
    def append(self, item):
        super().append(item * 5)


u = My_List([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
u.append('hey')
# print(u)
