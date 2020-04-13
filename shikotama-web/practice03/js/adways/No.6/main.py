import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    x = list(lines[0])
    new_list = sorted(x)
    idx = 0
    for n in range(len(new_list)):
      if new_list[n] != "0":
        idx = n
        break
    new_list[0], new_list[idx] = new_list[idx], new_list[0]
    print("".join(new_list))
    #for i, v in enumerate(lines):
        #print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
