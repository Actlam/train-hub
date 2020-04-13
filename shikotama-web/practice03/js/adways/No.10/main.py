import sys
import numpy as np

def main(lines):
  # このコードは標準入力と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use stdin and stdout.
  # Edit and remove this code as you like.

  n, m, x, y = list(map(int, lines[0].split(" ")))
  a = list(reversed(list(map(int, lines[1].split(" ")))))
  b = list(reversed(list(map(int, lines[2].split(" ")))))

  #occ_list = np.zeros(n, dtype=np.int)

  count = 0
  unb = []
  for i in range(len(b)):
    if a[count] < b[i] or count < len(a):
      count+=1
    else:
      unb.append(i)

  loss = 0
  for u in unb:
    if x < y or count >= len(a):
      loss += b[u] * x
    else:
      k = 0
      num_b = b[u]
      while(num_b > 0):
        num_b -= a[count]
        count+=1
        k+=1
      loss += (k-1) * y
    
  print(loss)
  

    #for i, v in enumerate(lines):
    #    print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
      lines.append(l.rstrip('\r\n'))
  main(lines)