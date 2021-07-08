#Mon 2
'''
def nibunn(arr,x):
   l=0
   r=len(arr)-1
   while(l<=r):
      mid=(l+r)//2
      if(arr[mid]==x):
         return mid
      elif(x<arr[mid]):
         r=mid-1
      elif(x>arr[mid]):
         l=mid+1
   return -1

array=[20,55,60,10,5,73,90,7,30,84]
a=int(input("入力："))
if(nibunn(array,a) == -1):
    print("検索キーなし")
else:
    print("検索キーあり")
    print(str(nibunn(array,a))+"番目です。")
'''


TBL = [20,55,60,10,5,73,90,7,30,84]
Y = int(input("Yを入力："))
head = 0
mid = 0
tail = len(TBL)-1
sw = 0
j = 0

while (sw == 0 and head <= tail):
    mid = (head+tail) / 2
    TBL[mid] = Y