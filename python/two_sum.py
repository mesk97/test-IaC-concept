def main2(nums, target):
    print ("for1: ", range(0, len(nums)-1))
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            print ("for2: ", range(i+1, len(nums)))
            print (i, j, target)
            if (nums[i] + nums[j]) == target: 
                print ("waw")
                return [nums[i], nums[j]]
    return [0, 0]


def main(nums, target):
    nums1 = sorted([(nums[i], i) for i in range(0, len(nums))], key = lambda i: i[0])
    nums2 = []

    for e in nums1:
        r = target - e[0]
        if r <= 0:
#        if r <= 0 or e*2 == target:
            continue
        nums2.append((r, e[1]))
    nums2 = sorted(nums2, key = lambda i: i[0])
    
    i1 = 0
    i2 = 0
    len1 = len(nums1)
    len2 = len(nums2)

    while i1 < len1 and i2 < len2:
        print ("i1=%d i2=%d" % (i1, i2))
        if nums1[i1][0] == nums2[i2][0] and nums1[i1][1] != nums2[i2][1]:
            return [nums1[i1][1], nums2[i2][1]]
        elif nums1[i1][0] < nums2[i2][0]:
            i1 = i1 + 1
        else:
            i2 = i2 + 1

    return [-1, -1]


if __name__ == "__main__":
    nums = [3,2,4, 1, 9, 4, 11, 8]
    target = 8
    print (str(main(nums, target)))
