# put your python code here
def parent(i):
    if i % 2 == 0:
        return (i - 2) // 2
    else:
        return (i - 1) // 2
    
def lch(i):
    return 2*i + 1

def rch(i):
    return 2*i + 2


def siftdown(i, res):
    size = len(h)
    mx_ind = i
    l = lch(i)
    r = rch(i)
    if l < size and h[l] < h[mx_ind]:
        mx_ind = l
    if r < size and h[r] < h[mx_ind]:
        mx_ind = r
    if i != mx_ind:
        h[i], h[mx_ind] = h[mx_ind], h[i]
        res.append((i, mx_ind))
        siftdown(mx_ind, res)

def builtheap(h):
    res = []
    size = len(h)
    start = (size - 2) // 2
    for i in range(start, -1, -1):
        siftdown(i, res)
    
    if res:
        print(len(res))
        for elem in res:
            s = ' '.join(list(map(str, elem)))
            print(s)
            
    else:
        print(0)
