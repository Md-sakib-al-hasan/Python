def is_palindrome(arr):
    n=len(arr)
    for i in range(n//2):
        if arr[i] != arr[n-1-i]:
            return "NO"
    return "YES"
n=int(input())
arr=list(map(int,input().split()))
result = is_palindrome(arr)
print(result)