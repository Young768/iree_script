
def process():
    f = open("4layer-nosharding.mlir", "r")
    lines = f.readline()
    lines = f.readline()
    lines = f.readline()
    line = lines.split()
    for idx, val in enumerate(line):
        if "%arg" in val:
            sub1 = "<"
            sub2 = ">"
            test_str = line[idx+1]
            # getting index of substrings
            idx1 = test_str.index(sub1)
            idx2 = test_str.index(sub2)
            res = ''
            # getting elements in between
            for idx in range(idx1+1, idx2):
                res = res + test_str[idx]
            res = "--input=" + res + "=1"
            print(res)



process()