q = []

def push(val):
    q.insert(0,val)
def pop():
    return q.pop()
def isEmpty():
    if len(q)==0:
        return True;
    return False
