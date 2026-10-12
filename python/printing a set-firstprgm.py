
#givenSet:[1, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]

highestPeak=50
startingTerm=2
sequence=[]
for mainSequence in range(highestPeak-1):
    for risingTerm in range(startingTerm): #range(6) = [0,1,2,3,4,5] -- rising terms
        sequence.append(risingTerm+1)

    for fallingTerm in range(startingTerm-2): #range (5)=[0,1,2,3,4] -- falling terms
        sequence.append(startingTerm-fallingTerm-1) 

    startingTerm=startingTerm+1
sequence.append(1)
print(sequence)
print("                                               ")
print(len(sequence))
print(sequence[2025])
