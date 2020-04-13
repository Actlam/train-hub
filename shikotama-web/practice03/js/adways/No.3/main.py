


import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))

    idx = lines[0].split()
    idx = ["3:Fizz","5:Buzz","6"]

    a = []
    s = []
    b = 0
    c = 0


    for i in range(len(idx)-1):
      if b <= 1:
        a.append(idx[b].split(":")[0])
        b += 1
    a = list(map(int, a))



    for i in range(len(idx)-1):
      if c <= 1:
        s.append(idx[c].split(":")[1])
        c += 1



    m = int(idx[-1])


    # print(len(a))
    # print(type(a[0]))
    # print(type(s[0]))
    # print(type(m))
    # print(s)
    # print(m)


    res = []
    for i in range(len(a)):
      if m % a[i] == 0:
        res.append(s[i])
      else:
        pass
    
    if len(res) == 0:
      res.append(m)
    else:
      pass

    res = list(map(str, res))
    
    print(''.join(res))


    




if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
