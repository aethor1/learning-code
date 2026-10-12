
#easy way to solve problems that give you 2 diff numbers in an arithmetic sequence and ask you to find the equation (explicit rule) for it

# just to note its in the form --> a_n=a_1+(n-1)d  ---  but i'll be representing it more like y=mx+b

# Hope the names are straightforward but just in case-- value is for the actual number it's representing in the sequence, and term number is the position of the number in the sequence
firstValue=120 #y-val
firstTermNumber=14 #x-val

scndValue=370 #y-val
scndTermNumber=39 #x-val

answer=[]

#finding the common difference part

commonDifference=(scndValue-firstValue)/(scndTermNumber-firstTermNumber)


#finding the initial number finally

initialNumber=firstValue-(commonDifference*firstTermNumber)


# putting the actual answer together -- using "n" as the variable-- the problem might be asking for smth else who knows :/

answer.append(f"{commonDifference}n + {initialNumber}")

print(answer)
