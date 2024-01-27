# image_time_count.py の使い方

## 注意書き

今回行う画像呈示の実験において，使うプログラムに関しては今から説明する，**image_time_count.py**のみである．ただし，画像については変更がある可能性が高いので，**画像が入っているディレクトリ**に関してはよく確認しておくこと．また今回渡すプログラム集の中には使わないものも入っているので，注意して使用すること．

## 0. 実験の準備

3つの測定機器(心拍計，アイトラッカー，脳波計)を接続し，**モニター上にレコーディングボタンを表示させておくこと**．(このプログラムでは，レコーディングボタンを押す作業を自動化したものであることからこの準備が必須である．)

さらに，この実験で使用するモニターの数はパソコンの画面も含めると**3つ**である．1つ目に**被験者に表示する画像を見せる**ためのモニター，2つ目に**レコーディングボタンを表示させる**ためのモニター，そして3つ目に**このプログラム**を表示させておくためのパソコンの画面，以上の3つである．


## 1. 座標の指定

メインプログラム以降の**click_positions**と記載しているところの座標を変えてあげればよい．またその座標に関しては，**click_demo.py**を使用して確認すること．

**click_demo.py**の使用方法については当日に説明します．


## 2. 画像の指定

各関数**psuchopy??**(??には数字が入る)において，**現在のディレクトリからのパスを指定**することで，画像の参照が可能になっている．
EX) **"/jikken_0120_3/*.jpg"**　これだと現在のディレクトリから考えると，**jikken_0120_3**のディレクトリの中の全ての**jpgファイル**を参照していることになっている．また，このプログラムにおいて画像データの情報は，それぞれの**imageLists**，**imageData**に格納されている．よって画像の変更等はこれらの変数に注意してデバックすること．

## 3. 画像表示について

### 関数psychopyについて
　
この関数は，読み込んだ刺激の強い画像と時間間隔の短いグレースケール画像を表示させるための関数である．このプログラムでは，**刺激の強い画像**をcore.wait(10)に設定しているように**10秒間**表示させ，psychopy1関数を使い**グレースケール画像**をcore.wait(2)，すなわち**2秒間**表示させる関数である．

### 関数psychopy1について

この関数は，時間間隔の長いグレースケール画像を表示させるための関数である．このプログラムでは，**グレースケール画像**をcore.wait(120)，すなわち**120秒間**表示させる関数である．


## 4. csvファイルへの書き込みについて

関数**write_to_csv**において，音刺激を開始した時刻をcsvファイルに記録するようにしている．
ここでcsvファイルに関しては元のプログラムだと，**time_log1.csv**というファイル名で作成される。また，ファイル名は任意に変更してよい。ただし，拡張子は.csvにすること．

**csvファイルは記録したら逐次，保存 OR 削除**すること(保存した場合はプログラムの中でcsvファイルの名前を変えておくこと)．そうしないと元のcsvファイルに新たに書き込みされてしまう.


## 5. スクリーン指定などの詳細設定

プログラムを実行する上での詳細設定は以下のように記載している．
**win = visual.Window(size=(1919,1076), pos=(0,0), screen=1)**
ここで，変数**size**は画像提示の外枠の大きさ(ウインドウ)でありディスプレイの大きさによって変更することが望ましい．**pos**はウインドウを配置する箇所であり，基本的に(0,0)にしておくこと．さらに**screen**は本実験では，**0 OR 1 OR 2**の値が存在し，画像を表示させるスクリーンによって値を変更すること．

わかんなくなった場合は，全パターン試して最適なスクリーンを選ぶこと．

## 6. プログラムの終了方法

**コントロールキー + c**を押すことで，プログラムの終了が可能である．
