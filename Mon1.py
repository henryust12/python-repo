
#Mon 1

#変数
bol = 0
jun = 0
count = 0
lst = [1,10,55,60,11,5,45,73,90,73,15,85]

#入力
y = 85

#ループ
for i in lst:
    if y == i:
        bol = 1
        jun = count
    count = count + 1
if bol == 1:
    print("検索キーあり")
    print(jun,"番目")
else:
    print("検索キーなし")

