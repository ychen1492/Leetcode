def to_be_defined(s: bool):
    t=[]
    while s:
        t.append(2)
        if len(t) == 10:
            s = False
    print(t)


if __name__ == "__main__":
    to_be_defined(True)