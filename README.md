# GazoEdit

画像を比率を維持したまま横1200pxまで圧縮するスクリプト。
iPhone撮影時のフォーマット(.HEIC)であった場合はJPEG形式に圧縮する。


# Requirement

Python 3.9.16

```requirements.txt
cffi==1.15.1
numpy==1.24.2
opencv-contrib-python==4.7.0.72
Pillow==9.2.0
pycparser==2.21
pyheif @ git+https://github.com/david-poirier-csn/pyheif.git@721ef2c17347ccde7700d35e7d3b088d14fbae23

```


# Installation

Requirementで列挙したライブラリなどのインストール方法を説明する

```bash
cd GazoEdit
pip install -r requirements.txt
```

# Usage

リサイズ・変換スクリプト
```bash
git clone https://github.com/9610r/GazoEdit.git
cd GazoEdit
python main.py
```

# Note

注意点などがあれば書く

# Author

作成情報を列挙する

* tiger

# License

Under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
