
num_list = [10, 22, 12, 13, 23, 44, 33]



while True:
    ans = input("数字を入力してね:")
    if ans == "q":
        break
    else:
        try:
            int_ans = int(ans)
            if int_ans in num_list:
                print("正解")
            else:
                print("不正解")
               
        except:
            print("数字を入力するかqで終了してね")
