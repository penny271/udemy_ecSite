for i in range(10):
    if i == 3:
        continue
    print(i)
#* else: ループの外に出た際に実行されます(breakでループを抜けた場合には実行されません)
else:
    print('ループ処理終了') #-#ループ終了後実行されます new 20220628

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print('whileループ終了')
