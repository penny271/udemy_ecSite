# リスト
# list_a = [1,2,3,4]
# list_b = []

# print(list_a)
# print(list_a[-2])

# list_a = [1, [1,2,'apple'],3,'banana']

# print(list_a[1][2])
# print(list_a)
#-数の置き換え new - 20220628
# list_a[1][2] = 'lemon'
# print(list_a)
# list_a.reverse()
# print(list_a)

# リスト関数
#!!!

list_a = [1,2,3,4,5]
list_b = list_a[:3]
print(list_b)
print(list_a[0:5:2])

# append, extend, insert, clear
# #!
# list_a.append('apple')
# print(list_a)

# #- new リストを拡張 20220628 リストとリストを一つのリストとしてつなげる
# list_a.extend(['banana', 'lemon']) # [1, 2, 3, 4, 5, 'apple', 'banana', 'lemon']
# print(list_a)
# list_a.insert(1, 'grape')
# print(list_a)
# #- new
# list_a.clear() #[]
# print(list_a)

# # remove, pop, count
#!
# list_a.remove(3)
# print(list_a)
# #- new -20220628 最後の要素をリストから取り出す
# value = list_a.pop(1)
# print(list_a)
# print(list_a, value) #[1, 4, 5] 2
# print(list_a.count(1)) #1 エラーの場合、0を返す
# print(list_a.index('apple')) #ない場合はエラーを返す

# #copy
#!
# #- 参照渡ししている new 20220628
# # list_b = list_a
# # list_b[0]='AAAAA'
# # print(list_a) #['AAAAA', 2, 3, 4, 5]
# #- 20220628 new! 参照渡しを防ぐ
# list_b = list_a.copy()
# print(list_a)
# list_b[0]='AAAAA'
# print(list_a)

# # sort reverse
list_a = ['banana', 'lemon', 'apple', 'grape']
print(list_a)
list_a = sorted(list_a)
list_a.reverse()
print(list_a)
