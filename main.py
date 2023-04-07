import os.path
from PIL import Image
import pyheif

user_path = os.path.expanduser('~')
#ファイル名を宣言
readPath = user_path + '/Desktop/Gazo/original/'
savePath = user_path + '/Desktop/Gazo/resize/'

def heic_chenge(image_path, save_path):
    # HEICファイルpyheifで読み込み
    heif_file = pyheif.read(image_path)
    # 読み込んだファイルの中身をdata変数へ
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    # JPEGで保存
    data.save(str(save_path), "JPEG")

# アスペクト比を固定して、高さが指定した値になるようリサイズする。
def scale_to_height(img, height):
    width = round(img.width * height / img.height)
    return img.resize((width, height))

# アスペクト比を固定して、幅が指定した値になるようリサイズする。
def scale_to_width(img, width):
    height = round(img.height * width / img.width)
    return img.resize((width, height))


def resize_image(file):
    img = Image.open(file) # 画像のパスを生成し、imgへ画像を格納
    if img.width < img.height:
        img = img.rotate(90, expand=True)
    # サイズを幅と高さにアンパック
    # img.thumbnail(size=(800, 800))     # 画像を800×800サイズ変更
    img = scale_to_width(img, 1200)
    img.save(file)  #resizeフォルダへ保存

def save(before, after):
    img = Image.open(before) # 画像のパスを生成し、imgへ画像を格納
    img.save(after)  #re

if __name__ == "__main__":
    #imgフォルダ内の画像名をまとめて取得
    files = os.listdir(readPath)

    #for文で画像サイズを一括変更
    for file in files:
        if file == ".DS_Store":
            # DS_STOREは無視する
            continue
        root, ext = os.path.splitext(file)
        file_name = savePath + root + ".jpeg"
        if ext == ".HEIC" or ext == ".heic":
        # nowtime = datetime.now().strftime('%Y%m%d%H%M%S%f')))
            heic_chenge(os.path.join(readPath, file), file_name)
        else:
            save(os.path.join(readPath, file), file_name)

        resize_image(file_name)
