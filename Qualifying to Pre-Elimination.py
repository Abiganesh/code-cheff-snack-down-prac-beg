t=int(input())
for i in range(t):
    input1=input()
    vals=input1.split(' ')
    input2=input()
    scores=[]
    s=input2.split(' ')
    for i in s:
        scores.append(int(i))
    scores.sort(reverse=True)
    k=int(vals[1])
    k=k-1
    thresold=scores[k]
    count=0
    for m in scores:
        if(m>=thresold):
            count=count+1
    print(count)
    