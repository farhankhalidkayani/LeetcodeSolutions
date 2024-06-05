class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr,s,e):
            if e-s+1<=1:
                return arr
        
            mid=(s+e)//2
            mergeSort(arr,s,mid)
            mergeSort(arr,mid+1,e)
            merge(arr,s,mid,e)

            return arr
        def merge(arr,s,mid,e):
            left=arr[s:mid+1]
            right=arr[mid+1:e+1]
            i=0
            j=0
            k=s
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    arr[k]=left[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=right[j]
                    j+=1
                    k+=1
            while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
        return mergeSort(nums,0,len(nums)-1)
        
    
        