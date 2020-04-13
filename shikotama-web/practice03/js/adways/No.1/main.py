
import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    n, K = list(map(int,lines[0].split(" ")))
    a = list(map(int,lines[1].split(" ")))
    count = 0
    for i in range(n):
      for j in range(n-i-1):
        for k in range(n-i-j-2):
          res = a[i] + a[i+j+1] + a[i+j+k+2]
          if res == K:
            count+=1
    print(count)
    #for i, v in enumerate(lines):
        #print("line[{0}]: {1}".format(i, v))

    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

print()
