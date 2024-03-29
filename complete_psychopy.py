import pyautogui
import time
from psychopy import visual, core
import os
import glob
import csv

#######################################################################################################
# 実験する際の注意点

# 2台のモニターを使えるようになった
# 計測用パソコンのモニターには、vscodeを表示させておく
# 被験者の目の前のモニターには、画像を表示させる(本プログラムにおいて指定する)
# 計測者の目の前のモニターには、実際にプログラムでクリックできるよう脳波計、アイトラッカー、心拍計の画面を表示させておく(ドラック操作等で移動させておくこと)
# また、画像提示のタイミングをcsvファイルに記録するようにしている


#######################################################################################################
# 変更するべき箇所
# imageLists = glob.glob(cwd + "/image/*.jpg") # 任意のファイルがあるディレクトリ

#core.wait(6) # 画像の表示時間(この書き方だと，基本的にすべての画像は6秒間表示される)

## ファイルは新規作成したものを入れよう(そのまま上書きされるので)  EX) time_log1.csv##
#with open('time_log1.csv', 'a', newline='', encoding='utf-8') as csvfile:

# クリックしたい座標(この部分は適宜変更すること)
    # click_positions = [(657,585)] #アイトラッカー
    # click_positions1 = [(1259,64)] # 脳波計
    # click_positions2 = [(88,90)] # 心拍計

#win = visual.Window(size=(1919,1076), pos=(0,0), screen=1) # size: 画面の大きさ(信川Labのモニターの大きさと同じにしている) pos: 画面の座標 screen = ( 0 OR 1 OR 2 ) 画像を表示させるスクリーンの指定

# if int(time3) == 20: # クリックしてから20秒後に画像提示をするようになっている

# 以上に挙げた箇所以外の部分は変更しないでください(デバックが大変になります...)

#######################################################################################################

# クリックする関数(ただし，心拍計だけダブルクリックじゃないとクリックされない)
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
    print('画像提示開始時刻:',time3)
    time4 = time.perf_counter()
    write_to_csv(time3)
    j = 0

    for i in imageLists:
        j = j + 1
       
        imageData[i].draw()
        win.flip()
        core.wait(6) # 画像の表示時間　(この書き方だと，基本的にすべての画像は6秒間表示される)
        time5 = time.perf_counter()
        time6 = (time5 - time4) + time3
        print('画像提示終了時刻その',j)  # 画像が終わった時間
        print(time6)
        write_to_csv(time6)

def write_to_csv(time_value):
    # ファイルは新規作成したものを入れよう(そのまま上書きされるので)  EX) time_log1.csv
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
    # クリックしたい座標(この部分は適宜変更すること)
    click_positions = [(657,585)] #アイトラッカー
    click_positions1 = [(1259,64)] # 脳波計
    click_positions2 = [(88,90)] # 心拍計


    # 画面上の複数の位置でクリックを実行
    click2(click_positions[0],click_positions1[0],click_positions2[0])
    time0 =  time.perf_counter()  # クリックした時の時間を取得   

    # 画像の表示のための準備
    win = visual.Window(size=(1919,1076), pos=(0,0), screen=1) # size: 画面の大きさ(信川Labのモニターの大きさと同じにしている) pos: 画面の座標 screen = ( 0 OR 1 OR 2 ) 画像を表示させるスクリーンの指定
    imageLists = psychopy00()
    imageData = psychopy0(imageLists)

    # 画像，経過時間の表示　また，画像提示時刻をcsvファイルに記録する
    i = 0
    while True:
        i += 1
        if i == 1:
            time1 = time0
        else:
            time1 = time1

        time.sleep(1)
        time2 = time.perf_counter() # 1秒ごとに時間を取得
        print("経過時間:", time2 - time1) # 1秒ごとに経過時間を表示
        time3 = time2 - time1
        if int(time3) == 20: # クリックしてから20秒後に画像提示をするようになっている
            psychopy(imageLists, imageData, time3)
