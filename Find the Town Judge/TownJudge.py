def townJudge(A,N):
  a0 = {x[0] for x in A}
  candidate=-1
  trustedby=0
  for i in range(N):
    if (i+1 not in a0): can=i+1
  for a in A:
    if (a[1]==candidate): trustedby+=1
  if(trustedby==N-1): return candidate
    else : return -1
