optimize two pointers:
https://leetcode.cn/problems/largest-merge-of-two-strings/description/

```python
    cur = start
    i = j = 0
    while cur <= end:
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            lst[cur] = left[i]
            cur += 1
            i += 1
        else:
            lst[cur] = right[j]
            cur += 1
            j += 1



```

basic:
https://leetcode.cn/problems/maximize-greatness-of-an-array/description/
https://leetcode.cn/problems/append-characters-to-string-to-make-subsequence/description/
https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/description/
https://leetcode.cn/problems/watering-plants-ii/description/
https://leetcode.cn/problems/count-binary-substrings/description/

compare to the hash-count, if the problem care about the order
then, we can't use hash-count, but two pointers

three numbers:
https://leetcode.cn/problems/3sum-closest/description/
https://leetcode.cn/problems/1fGaJU/description/


medium two pointers:
https://leetcode.cn/problems/expressive-words/description/

skip the part:
https://leetcode.cn/problems/move-pieces-to-obtain-a-string/description/

valid interval:
https://leetcode.cn/problems/4xy4Wx/description/
https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-ii/description/  -- (hard)
https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/description/


ready to be filled:
https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/

extreme inplace space:
https://leetcode.cn/problems/merge-sorted-array/description/

two pointers of interval to make array sorted :
https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/

merge interval:
https://leetcode.cn/problems/interval-list-intersections/description/

adaptive interval:
https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/description/

basic inplace:
https://leetcode.cn/problems/separate-black-and-white-balls/description/
