def linearsearch(arr,n,key):
  for i in range(n):
    if arr[i]==key:
      return i
  return -1
arr=[20,21,19,18,17]
key=19
n=len(arr)
print("linear search:",linearsearch(arr,n,key))
