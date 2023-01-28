


def judge():
        

    S,T,X = map(int,input().split())

    if S<T:
        if S<=X<T:
            return True
        else:
            return False
    else:
        if T<=X<S:
            return False
        else:
            return True

print("Yes" if judge() else "No")
