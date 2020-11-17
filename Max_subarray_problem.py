# output is in the form of (i , j) when max sum is positive
# else its null(-1) for 0 or negative sum

l = int(input())
a = list(map(int , input().split()))
if(l > 0):
  b = max(a)
  c = a.index(b)
  maxsum = b
  maxsumnow = 0
  i = j = 0
  mid = 0
  # main function
  if(b > 0):
    for k in range(len(a)):
      maxsumnow += a[k]
      if(maxsumnow < 0):
        maxsumnow = 0
        mid = k +1
      if(maxsumnow > maxsum):
        maxsum = maxsumnow
        i = mid
        j = k
    if(maxsum == b):
      print("(" ,c ,"," , c,")")
    else:
      print("(" ,i ,"," , j,")")
  else:print(-1)
else:
  print(-1)
