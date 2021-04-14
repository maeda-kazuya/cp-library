import math
# The method to return True or False
def solve(self, n):
    return True

# The method to fix border
def fixBorder(self, m):
    if not self.solve(m) and self.solve(m+1):
        return m+1
    elif not self.solve(m) and self.solve(m-1):
        return m-1
    else:
        return m

# Main method
def main(self):
    l = 0
    r = 10**9
    m = math.ceil((l+r)/2)

    while l <= r:
        m = math.ceil((l+r)/2)
        # print('\n', l, r, m)

        if self.solve(m):
            # print('Too big!')
            r = m - 1
        else:
            # print('Too small!')
            l = m + 1

    return self.fixBorder(m)