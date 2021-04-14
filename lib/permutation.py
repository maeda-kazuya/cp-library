from copy import *

class Permutation(object):
    def __init__(self):
        self.ans = set()

    def permutation(self, cur, arr):
        if len(arr) == 1:
            self.ans.add(cur + arr[0])

        for i in range(len(arr)):
            a = deepcopy(arr)
            c = a[i]
            del a[i]
            self.permutation(cur + c, a)

test = 'ABC'
# test = 'AAB'
p = Permutation()
p.permutation('', list(test))
print(p.ans)

