def findMedianSortedArrays(nums1, nums2) -> float:
    if len(nums1) > 1:
        med1 = nums1[len(nums1) // 2 - 1]
    else:
        med1 = nums1[0]
    if len(nums2) > 1:
        med2 = nums2[len(nums2) // 2 - 1]
    else:
        med2 = nums2[0]

    if len(nums1) == 1 and len(nums2) == 1:
        return (med1 + med2) / 2

    if med1 < med2:
        return findMedianSortedArrays(nums1[len(nums1) // 2:], nums2[:len(nums1) // 2])
    else:
        return findMedianSortedArrays(nums1[:len(nums1) // 2], nums2[len(nums1) // 2 - 1:])


array1 = [1, 2]
array2 = [3]
print(findMedianSortedArrays(array1, array2))
