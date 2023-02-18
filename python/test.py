def main(arr1, arr2):
    index1 = 0
    index2 = 0

    result = []

    while index1 < len(arr1) or index2 < len(arr2):
        print ("i1 = %d i2 = %d" % (index1, index2))
        if index1 == len(arr1):
            toadd = arr2[index2]
            index2 = index2 + 1
        elif index2 == len(arr2):
            toadd = arr1[index1]
            index1 = index1 + 1
        elif arr1[index1] < arr2[index2]:
            toadd = arr1[index1]
            index1 = index1 + 1
        else:
            toadd = arr2[index2]
            index2 = index2 + 1
        
        if len(result) == 0:
            result.append(toadd)
        elif result[-1] != toadd:
            result.append(toadd)

    print (result)

if __name__ == "__main__":
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    main(arr1, arr2)
