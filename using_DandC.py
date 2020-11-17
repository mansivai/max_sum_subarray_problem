# output(i , j , maxsum)
p = int(input())
a = list(map(int , input().split()))
def middle( a , l , m , h):
  sum = 0  
  leftsum = -10000
  rightsum = -10000
  maxleft = 0
  maxright = 0
  for i in range(m , l-1 , -1):
    sum = sum + a[i]
    if( sum > leftsum):
      leftsum = sum
      maxleft = i
  sum = 0
  for i in range(m + 1, h + 1):
    sum = sum + a[i]
    if( sum > rightsum):
      rightsum = sum
      maxright = i
   
  return maxleft, maxright,max(leftsum, rightsum , leftsum+rightsum)

def maxsum(a , l , h):
  # base case
  if (l == h) : 
    return(l , h ,a[l])
  else:
  # divide
    m =(l+ h) // 2
    # combine
    
    leftlow, lefthigh, leftsum = maxsum(a,l,m)
    rightlow, righthigh, rightsum = maxsum(a,m+1,h)
    xlow, xhigh, xsum = middle(a,l,m,h)

    if(leftsum >= max(rightsum , xsum)):
      return leftlow,lefthigh,leftsum
    elif(rightsum >= max(leftsum,xsum)):    
      return rightlow, righthigh, rightsum
    else:
      return xlow,xhigh,xsum


h = len(a)-1
if(len(a) >0):
 print(maxsum(a , 0 , h ))
else: print("null")
