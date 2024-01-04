

#################################################

import pyautogui
import time
from psychopy import visual, core, sound
import os
import glob
import csv
from threading import Thread
import pyglet


# クリックする関数(ただし，心拍系だけダブルクリックじゃないと動かない)
def click2(position, position1, position2):
    x, y = position # アイトラッカーの座標
    x1, y1 = position1 # 脳波計
    x2, y2 = position2 # 心拍計
    pyautogui.click(x, y) # アイトラッカー
    time.sleep(0.001)  # delayは0.001秒
    pyautogui.click(x1, y1)
    time.sleep(0.001)  # delayは0.001秒
    pyautogui.doubleClick(x2, y2)

# 音声ファイルの検索
def sound_load():
    # 音声ファイルのパスを指定
    cwd = os.getcwd()  # 現在の作業ディレクトリ
    sound_list = glob.glob(cwd + "/voice/*.wav") # ファイルのパスを取得
    return sound_list


# 音声ファイルの読み込み
def sound_search(sound_list):
    sound_Data = {}
    for i in sound_list:
        sound_obj = pyglet.media.load(i)
        sound_Data[i] = sound_obj
    return sound_Data

# 音声ファイルの再生
def sound_play(sound_Data, time3):

    print('音声再生開始タイミング:', time3)
    time4 = time.perf_counter()
    write_to_csv(time3)

    for i in sound_Data.values():
        player = i.play()
        player.eos_action = pyglet.media.Player
        core.wait(6)
        player.pause()
        print('音声再生終了タイミング:', time3)
        time5 = time.perf_counter()
        time6 = (time5 - time4) + time3
        print('音声再生終了タイミング:', i)  # 音の再生が終わった時間
        print(time6)
        write_to_csv(time6)






def write_to_csv(time_value):
    # ファイルは新規作成したものを入れよう(そのまま上書きされるので)
    with open('time_log_voice.csv', 'a', newline='', encoding='utf-8') as csvfile: # time_log_voice.csvは任意に変えてよい　ただし，拡張子は.csvにすること
        fieldnames = ['Timestamp']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # ファイルが空ならヘッダーを書き込む
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Timestamp': time_value})
# ...（前略）

if __name__ == "__main__":
    # クリックしたい座標
    click_positions = [(657, 585)]  # アイトラッカー
    click_positions1 = [(1259, 64)]  # 脳波計
    click_positions2 = [(88, 90)]  # 心拍計

   
    sound_list = sound_load()

    # 使用したいサウンドデバイスを選択
    # selected_device = {
    #     'DeviceIndex': 7.0,
    #     'HostAudioAPIId': 13.0,
    #     'HostAudioAPIName': 'Windows WASAPI',
    #     'DeviceName': 'ヘッドホン (AVIOT TE-D01gv)',
    #     'NrInputChannels': 0.0,
    #     'NrOutputChannels': 2.0,
    #     'LowInputLatency': 0.0,
    #     'HighInputLatency': 0.0,
    #     'LowOutputLatency': 0.003,
    #     'HighOutputLatency': 0.01,
    #     'DefaultSampleRate': 44100.0,
    #     'id': 1
    # }
    #　使用したいサウンドデバイスを指定
    selected_device = {'DeviceIndex': 6.0,
                        'HostAudioAPIId': 13.0, 
                        'HostAudioAPIName': 'Windows WASAPI', 
                        'DeviceName': 'スピーカー (Realtek High Definition Audio)',
                          'NrInputChannels': 0.0,
                            'NrOutputChannels': 8.0,
                              'LowInputLatency': 0.0, 
                              'HighInputLatency': 0.0, 
                              'LowOutputLatency': 0.003, 
                              'HighOutputLatency': 0.0106667,
                                'DefaultSampleRate': 48000.0, 
                                'id': 1}
    sound_Data = sound_search(sound_list)
    click2(click_positions[0],click_positions1[0],click_positions2[0]) # 実際にクリックする 

    i = 0 # 経過時間のカウントのための変数
    # 経過時間の表示と音声の再生
    while True:
        i += 1
        if i == 1:#最初のループのみ time1に現在時刻を代入
            time1 = time.perf_counter()
        else: #2回目以降はtime1は固定する
            time1 = time1

        time.sleep(1) #1秒待つ
        time2 = time.perf_counter()
        print("経過時間:", time2 - time1) # 経過時間を表示
        time3 = time2 - time1 # 経過時間をtime3に代入

        if int(time3) == 3: # 3秒経過したら音を鳴らすようにする
            sound_thread = Thread(target=sound_play, args=(sound_Data,time3))
            

            sound_thread.start()
            

            sound_thread.join()
            
