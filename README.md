# beagleboneblack
BeagleBoneBlack Repository


BeagleBoneblackの練習用リポジトリです。
現在はraspberry pi 2 で練習中です。


実行方法
##single_thread ディレクトリ
モーションセンサーを動かすプログラム。
実行方法: $ sudo python manager.py

 - manager.py
camera, uploader, motion_sensorのインスタンスを生成
motion_sensorにイベントハンドラの追加
モーションセンサーの実行を行っている

##multi_thread ディレクトリ
モーションセンサーと超音波センサーを
それぞれスレッドを立て同時に動かすプログラム。
実行方法: $ sudo python thread_manager.py

 - thread_manager.py
 manager.pyと同じようにインスタンスを生成、イベントハンドラの追加を行う
 複数センサーを扱うことを目的としている為
 モーションセンサーと超音波センサーそれぞれのスレッドを立てメソッドを呼び出している


##課題点
 - それぞれ例外処理について記述できていない。
  thread_managerに関してはCtrl-cで終了できないので手間だがpsをkillしてあげる
 - インデントが空白2つになっているので4つに修正

###後々追加修正する必要あり。

##共通ファイルの説明

 - event.py
 各センサーにイベントハンドラを持たせる為のファイル

 - camera.py
 カメラモジュールで画像を撮影する為のファイル
 shutterメソッドの引数は
 senderは誰がこのメソッドを呼んだかを表す
 eargはモーションセンサーが反応した時刻をstr型として受け取っている

 - motion_sensor.py
 モーションセンサーを動かす為のファイル
 while文で無限ループを行うことで周期的に動作している
 現状では2秒間隔で動作するようにしている
 センサーが感知した場合、登録されているevent_handlersを呼び出す

 - sonic_sensor.py
 超音波センサーを動かす為のファイル
 while文で無限ループを行うことで周期的に動作している
 現状では1秒間隔で動作するようにしている
 測定距離が20cm以下となった場合、登録されているevent_handlersを呼び出す

  - uploader.py
  camera.pyで撮影された画像をアップロードするためのファイル
  現状ではcameraの撮影後すぐに呼び出されるようになっている。

##multi_process ディレクトリ
現状動作しないプログラム。
目的として、モーションセンサーと超音波センサー
それぞれを別々のプロセスで同時に動かす。
