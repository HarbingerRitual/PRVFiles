def SubSequence(array, sequence):
    index = 0

    for i in array:
        if index < len(sequence) and i == sequence[index]:
            index += 1
    return index == len(sequence)

array = []
sequence = []
try:
    N = int(input("Enter the numbers of elements of the main array: "))
    for i in range(N):
        array.append(int(input("enter a value: ")))
        print(array)

    N1 = int(input("Enter the numbers of elements of the sequence array: "))
    for i in range(N1):
        sequence.append(int(input("enter a value: ")))
        print(sequence)

    if len(sequence) == 0:
        print("you need at least one element in the sequence")

    elif len(array) == 0:
        print("you need at least one element in the array")

    else:
        print("Is the sequence array a subSequence of the main array?")
        print(SubSequence(array, sequence))
except:
    print("Please enter a valid input (numbers)")

'''
array1 = [5,1,22,25,6,-1,9,10]
array2 = [1, 6, -1, 10]
'''