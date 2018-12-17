# Bizenプロジェクト

# ThingSpeakに適当なデータを送信

ThingSpeakに適当なデータを送信してみる，テスト用プログラム．
ただのテストなので，実用的な要素は一切含まれない．

## 必要なもの

* ThingSpeakのアカウント
* ThingSpeak上でチャンネルを作っておくこと

## 準備

info.jsonの各項目に，ThingSpeakのAPIを使うための情報を記述する．

CH Channel ID．URLとかページ内とかに書いてある．
api\_key ThingSpeakにログインしてAPI Keysタブを見れば書いてある．
num 作ったチャンネルに送信するデータの数．
res 取得するデータの数．

## 実行

'''
$ python3 main.py
'''

