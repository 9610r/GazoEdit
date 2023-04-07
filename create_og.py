import os.path
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np

import pyheif

user_path = os.path.expanduser('~')
#ファイル名を宣言
readPath = user_path + '/Desktop/Gazo/original/'
savePath = user_path + '/Desktop/Gazo/og/'
rectPath = user_path + '/Desktop/Gazo/rect/'
font = user_path + '/Desktop/Gazo/NotoSansJP-Bold.otf'

def get_font(size: int):
    return ImageFont.truetype(font, size)

def read_image(file):
    base = Image.open(file).convert('RGBA')
    size = base.size
    rect = Image.new('RGBA', size)
    draw_rect = ImageDraw.Draw(rect)
    rect_margin = 50
    draw_rect.rectangle((rect_margin, rect_margin, size[0] - rect_margin, size[1] - rect_margin), fill=(255, 255, 255,70))
    base = Image.alpha_composite(base, rect)
    path = base.save(rectPath+'ret.png')
    # cv2で画像を3次元配列として読み込み
    # PIL.ImageDraw形式に変換
    img = cv2.imread(rectPath+'ret.png')
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)

    # 書き込むタイトル文字列を表示する行ごとに区切ったもの
    text_lines = ['TEST TITLE', 'BBBBBBBBBBBBBBB']
    # 文字書き込みの初期位置のy座標
    y_offset = 100
    # 上記プロセスで用意したフォントttfファイルパス
    font_size = 62

    font_info = get_font(font_size)

    # 行ごとに書き込み処理
    for text_line in text_lines:
        draw.text((80, y_offset), text_line, font=font_info, fill=(0, 0, 0, 0))
        # Y位置を移動（下方向にずらして改行を表現する）
        y_offset += 77

    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    Image.fromarray(img).save(savePath + 'result.png')

if __name__ == "__main__":
    #imgフォルダ内の画像名をまとめて取得
    files = os.listdir(readPath)

    #for文で画像サイズを一括変更
    for file in files:
        if file == ".DS_Store":
            # DS_STOREは無視する
            continue
        draw = read_image(readPath+file)
