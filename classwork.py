def search(x,nums):
    low=0
    high=len(nums)-1
    while nums[low]<=x<=nums[high]:
        mid=(low+high)/2
        if x==nums[mid]:
            return mid
            break
        elif x<nums[mid]:
            high=mid-1
            return search(x,nums[:mid])
        else:
            low=mid+1
            return search(x,nums[mid+1:])+mid
def main():
    ll=[1,4,8,9,10,11,13,19]
    search(4,ll)
main()

