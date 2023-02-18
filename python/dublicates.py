def containsNearbyDuplicate(nums, k):
    nums_witn_index = [(nums[i], i) for i in range(0, len(nums))]
    nums_witn_index.sort(key = lambda i: i[0])

    print(str(nums_witn_index))

    starter = nums_witn_index.pop()
    while len(nums_witn_index) > 0:
        next = nums_witn_index.pop()
        if starter[0] == next[0] and abs(starter[1] - next[1]) <= k:
            print (str(starter), str(next))
            return True
        else:
            starter = next

    return False


if __name__ == "__main__":
    #nums = [1,2,3,1,2,3]
    nums = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
    k = 1
    #nums = [1,2,3,1]
    #k = 3
    print(str(containsNearbyDuplicate(nums, k)))
