def mergesort(A):
    if(len(A)>1):
        left_A=A[:len(A)//2]
        right_A=A[len(A)//2:]




        mergesort(left_A)
        mergesort(right_A)

        i=0
        j=0
        k=0
        while(i<(len(left_A))) and (j<(len(right_A))):
            if(left_A[i]<right_A[j]):
                A[k]=left_A[i]
                i+=1
            else:
                A[k]=right_A[j]
                j+=1
            k+=1


        while(i<(len(left_A))):
             A[k]=left_A[i]
             i+=1
             k+=1


        while(j<(len(right_A))):
            A[k]=right_A[j]
            j+=1
            k+=1



A=[2,9,16,23,46,6,1,3]
mergesort(A)
print(A)
