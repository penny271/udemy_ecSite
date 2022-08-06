# セイウチ演算子
#- python(セイウチ演算子(3.8以降)) new 20220628
# := イコールの前に:コロンとつけた演算子
#^ 変数の代入と変数の使用を同時に実行できるという特徴を持っている

if (n := 10) > 5:
    print('5より大きい: {}'.format(n))

n = 0
while (n := n + 1) < 10:
    print(n)

# n =1
# while n < 10:
#     print(n)
#     n += 1

n = 1
while (n := n+1) < 5:
    print(f'{n=}')