# # Binary search
# def binarySearch( arr, k):
#         # code here
        
#         left=0
#         right=len(arr)-1
#         while left<=right:
#             mid=(left+right)//2
#             if mid==k:
#                 return True
                
#             elif mid<k:
#                 left=mid+1
#             else:
#                 right=mid-1
#         return False
# arr=[2,3,4,6]
# k=6
# print(binarySearch(arr,k))




# 647. Palindromic Substrings
def countSubstrings( s):

        
    count=0
        
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring=s[i:j+1]
            left=0
            right=len(substring)-1
            ispalindrome=True
            while left<right:
                if substring[left]!=substring[right]:
                    ispalindrome=False
                    break
                left+=1
                right-=1

            if ispalindrome:
                count+=1
    return count
print(countSubstrings("abc"))
