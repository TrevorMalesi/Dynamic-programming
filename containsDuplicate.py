class Solution:
    def isDuplicate(self,array):
        a=set()
        for i in range (len(array)):
            if array[i] not in a:
                a.add(array[i])
            else:
                return True
        return False
solution=Solution()
array=[1,2,3]
arr=[1,1,2]
print(solution.isDuplicate(array))
print(solution.isDuplicate(arr))