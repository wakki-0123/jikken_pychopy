import pyautogui
import time
from psychopy import visual, core
import os
import glob
import csv


#################################

    

# クリックする関数(ただし，心拍系だけダブルクリックじゃないと動かない)
def click2(position,position1,position2):
    x, y = position
    x1,y1 = position1
    x2,y2 = position2
    pyautogui.click(x, y)
    time.sleep(0.001) #delayは0.001秒
    pyautogui.click(x1, y1)
    time.sleep(0.001) #delayは0.001秒
    pyautogui.doubleClick(x2, y2)
    


# 画像検索関数
def psychopy00():
    cwd = os.getcwd()  # 現在の作業ディレクトリ
    imageLists = glob.glob(cwd + "/image/*.jpg") # 任意のファイルがあるディレクトリ
    return imageLists

# 画像読み込み関数
def psychopy0(imageLists):
    imageData = {}
    for i in imageLists:
        imageData[i] = visual.ImageStim(win, image=i)
    return imageData

# 画像表示関数
def psychopy(imageLists, imageData, time3):
    print('画像提示開始タイミング:',time3)
    time4 = time.perf_counter()
    write_to_csv(time3)
    j = 0

    for i in imageLists:
        j = j + 1
       
        imageData[i].draw()
        win.flip()
        core.wait(6) # 画像の表示時間
        time5 = time.perf_counter()
        time6 = (time5 - time4) + time3
        print('画像提示終了タイミングその',j)  # 画像が終わった時間
        print(time6)
        write_to_csv(time6)

def write_to_csv(time_value):
    # ファイルは新規作成したものを入れよう(そのまま上書きされるので)
    with open('time_log1.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Timestamp']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # # 常にヘッダーを書き込む
        # writer.writeheader()
        # writer.writerow({'Timestamp': time_value})

        #ファイルが空ならヘッダーを書き込む
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Timestamp': time_value})

############################################################        
# 以下から実際に実行される
if __name__ == "__main__":
    # クリックしたい座標
    click_positions = [(657,585)] #アイトラッカー
    click_positions1 = [(1259,64)] # 脳波計
    click_positions2 = [(88,90)] # 心拍計


    
# 画像の表示のための準備
    win = visual.Window(size=(1000, 600), pos=(203,188), screen=1) # size 大きさ pos 座標
    imageLists = psychopy00()
    imageData = psychopy0(imageLists)

    
    # 画面上の複数の位置でクリックを実行
    click2(click_positions[0],click_positions1[0],click_positions2[0])
    i = 0
    while True:
        i += 1
        if i == 1:
            time1 = time.perf_counter() # 1回目のループのときに時間を取得
        else:
            time1 = time1

        time.sleep(1)
        time2 = time.perf_counter() # 1秒ごとに時間を取得
        print("経過時間:", time2 - time1) # 1秒ごとに経過時間を表示
        time3 = time2 - time1
        if int(time3) == 5: # 5秒後に画像提示
            psychopy(imageLists, imageData, time3)
