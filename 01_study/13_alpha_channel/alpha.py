# -*- coding: utf-8 -*-
import numpy as np
import cv2

# 参考(http://blanktar.jp/blog/2015/02/python-opencv-overlay.html)

src = cv2.imread('tinder.png', -1)  # -1を付けることでアルファチャンネルも読んでくれるらしい。
dst = cv2.imread('lena.jpg')

width, height = src.shape[:2]

# alphaチャンネルだけ抜き出す
mask = src[:,:,3]  # アルファチャンネルだけ抜き出す。
# ↑こいつがpython初心者には意味不明だったんだけど
#️ 多次元配列の中の要素全て抽出してくれる感じ　この場合だと2次元目の3番目の要素を配列にして抽出
# tin[0][0][3]
# tin[0][1][3]
# tin[0][2][3]
#       ↓
# tin[1][0][3]
# tin[2][1][3]
# tin[3][2][3]
#       ↓
# tin[t][n][3]
# で抜き出して配列を返してくれる。
#️ ちなみにpythonは配列ではなくてリストというらしい。


mask = cv2.cvtColor(mask, cv2.cv.CV_GRAY2BGR)  # 3色分に増やす。
mask = mask / 255.0  # 0-255だと使い勝手が悪いので、0.0-1.0に変更。
# mask = np.array(mask,np.uint8)

# cv2.imshow('mask',mask)
# cv2.waitKey(0)

# src = src[:,:,:3]  # アルファチャンネルは取り出しちゃったのでもういらない。

# dst[0:height:, 0:width] += np.  # 透過率に応じて元の画像を暗くする。
# dst[0:height:, 0:width] += src * mask  # 貼り付ける方の画像に透過率をかけて加算。

# cv2.imshow('mask',dst)
# cv2.imwrite('out.jpg', dst)
# cv2.waitKey(0)