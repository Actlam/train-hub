import sys
import numpy as np

def main(lines):

  # This is a sample code to use stdin and stdout.
  # Edit and remove this code as you like.

  n, m, x, y = list(map(int,  lines[0].split(" ")))
  a = list(map(int, lines[1].split(" ")))
  b = list(map(int, lines[2].split(" ")))
  a.sort()
  b.sort()
  a.reverse()
  b.reverse()
  occ_list = np.zeros(n, dtype=np.int)
  asum = np.array(a).sum()

  unb = []
  for i in range(len(b)):
    min_v = np.inf
    min_idx = -1
    for idx in range(len(occ_list)):
      if occ_list[idx] == 0 and a[idx] >= b[i]:
        min_v = a[idx] - b[i]
        min_idx = idx

    if min_v != np.inf:
      occ_list[min_idx] = 1
      asum -= a[min_idx]
    else:
      unb.append(i)

  loss = 0
  for u in unb:
    if x < y or b[u] > asum:
      loss += b[u] * x
    else:
      k = 0
      num_b = b[u]
      for idx in range(len(occ_list)):
        if occ_list[idx] == 0:
          num_b -= a[idx]
          asum -= a[idx]
          k+=1
          if num_b <= 0:
            break
      loss += (k-1) * y

  print(loss)
  

    #for i, v in enumerate(lines):
    #    print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
  lines = []
  #for l in sys.stdin:
  #    lines.append(l.rstrip('\r\n'))
  main(lines)
