# Bizenプロジェクト

いろんなクラウドに適当なデータを送ってみるテスト．
とりあえず，クラウド側のIDとかが正しく設定できてるかを確認するだけ．
ただのテストなので，実用的な要素は一切含まれない．

# ThingSpeak用設定

ThingSpeakに適当なデータを送信してみる，テスト用プログラム．

## 必要なもの

* ThingSpeakのアカウント
* ThingSpeak上でチャンネルを作っておくこと

## 準備

info.jsonの各項目に，ThingSpeakのAPIを使うための情報を記述する．

- Data
    - num
        - 作ったチャンネルに送信するデータの数．
    - res
        - 取得するデータの数．
- ThingSpeak
    - CH
        - Channel ID．URLとかページ内とかに書いてある．
    - api\_key
        - ThingSpeakにログインしてAPI Keysタブを見れば書いてある．

# Ambient用設定

## 必要なもの

* Ambientのアカウント
* Ambient上でチャンネルを作っておくこと
* Ambientのpythonライブラリをインストールしておくこと

## 準備

info.jsonの各項目に，AmbientのAPIを使うための情報を記述する．

- Data
    - ThingSpeakと同じ
- Ambient
    - CHID
        - チャンネルID
    - WRITE\_KEY
        - ライトキー
    - READ\_KEY
        - リードキー
    - USER\_KEY
        - ユーザーキー

チャンネルIDと各キーはいずれも，Myチャンネルを開けば書いてある．

# 適当な値を送信する

```
$ python3 main.py
```

送信されるデータはランダムな値．
すべてのサーバに同じデータが送信される．
使わないサービスがある場合は，main.pyを直接編集する．
次の2つを削除するか，コメントアウトするか，適当に．

- import文
- 関数呼出し

