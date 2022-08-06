# タプル

fruit = ('apple', 'banana', 'lemon')

print(fruit)
print(type(fruit))
print(fruit[0])
# fruit[1] = 'grape'
#- tupleに要素を追加 - 20220628
fruit = fruit + ('grape',)
print(fruit)

list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit)
print(fruit.count('apple'))
print(fruit.index('apple'))

#- ★★new タプル型で辞書型のキーの設定ができる!!
pos = (135, 35)
pos =[ 135, 35)]

countries = {pos: 'Japan'}

#! 辞書.get(タプル)
print(countries.get((135,35)))
#! 下記不可
# TypeError: 'dict' object is not callable
print(countries((135,35)))
