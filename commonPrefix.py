# Question2_SuglabaiTambolkar
def commonPrefix(A):
    size=len(A)
    if(size==0):
        return ""
    if(size==1):
        return A[0]
    A.sort()
    end=min(len(A[0]),len(A[size-1]))
    i=0
    while(i<end and A[0][i]==A[size-1][i]):
        i+=1
    prefix=A[0][0:i]
    return prefix

A=["VLiNKEDTECH","VLiSer","VLiedTevices"]
print(commonPrefix(A))
