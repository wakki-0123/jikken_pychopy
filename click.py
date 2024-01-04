import pyautogui
import time

# 画面上の座標を指定してクリック
def click_at_position(position):
    x, y = position
    pyautogui.click(x, y)
    print(f"Clicked at position: ({x}, {y})")
    


def click2(position,position1,position2):
    x, y = position
    x1,y1 = position1
    x2,y2 = position2
    pyautogui.click(x, y)
    time.sleep(0.001) #delayは0.001秒
    pyautogui.click(x1, y1)
    time.sleep(0.001) #delayは0.001秒
    pyautogui.doubleClick(x2, y2)
    


    #2つ目の座標をクリックしてからの時間経過を表示する
    i=0
    while(1):
     i+=1
     if(i==1):
        time1 = time.perf_counter()
     else:
        time1 = time1

     time.sleep(1) #1秒間ごと
     time2 = time.perf_counter()
     print("経過時間:", time2 - time1)




if __name__ == "__main__":
    
    # クリックしたい座標
    
    click_positions = [(646,586)] #アイトラッカー
    click_positions1 = [(1259,64)] # 脳波計
    click_positions2 = [(88,90)] # 心拍計


    # 画面上の複数の位置でクリックを実行
    click2(click_positions[0],click_positions1[0],click_positions2[0])



