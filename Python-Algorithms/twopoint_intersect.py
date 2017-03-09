def isPossiblePath(a,b,p,q,N):
    # (A,B) Horizontal end-to-end check
    if abs(a[1] - b[1]) == N-1:
        if p[0] < a[0] < q[0] or p[0] > a[0] > q[0] or p[0] < b[0] < q[0] or p[0] > b[0] > q[0]:
            return False
    # (A,B) Vertical end-to-end check
    elif abs(a[0] - b[0]) == N-1:
        if p[1] < a[1] < q[1] or p[1] > a[1] > q[1] or p[1] < b[1] < q[1] or p[1] > b[1] > q[1]:
            return False

    # (P,Q) Horizontal end-to-end check
    if abs(p[1] - q[1]) == N-1:
        if a[0] < p[0] < b[0] or a[0] > p[0] > b[0] or a[0] < q[0] < b[0] or a[0] > q[0] > b[0]:
            return False
    # (P,Q) Vertical end-to-end check
    elif abs(p[0] - q[0]) == N-1:
        if a[1] < p[1] < b[1] or a[1] > p[1] > b[1] or a[1] < q[1] < b[1] or a[1] > q[1] > b[1]:
            return False

    return True
def main():

    if __name__ == '_main_':
        a = (1,0)
        b = (1,4)
        q = (0,2)
        p = (4,2)
        N = 5
        print (isPossiblePath(a,b,p,q,N))
