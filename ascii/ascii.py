# -*- coding: utf-8 -*-
__author__ = 'QB'

from PIL import Image  # 图像处理库
import argparse  # 命令行解析包

"""
图片转换成字符画，很好玩
终端运行：python ascii.py 图片名称 -o 文件输出路径(默认当前路径下) --width 字符画宽 --height 字符画高
示例：python ascii.py wm.png -o H:/out.txt --width 100 --height 100
实验楼教程链接：https://www.shiyanlou.com/courses/370
"""
# 命令行输入参数处理
parser = argparse.ArgumentParser()
# 调用 add_argument() 方法来添加参数的信息
parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 可选参数：输出文件
parser.add_argument('--width', type=int, default=50)  # 可选参数：输出字符画宽，默认 50
parser.add_argument('--height', type=int, default=50)  # 可选参数：输出字符画高，默认 50

# 获取参数
args = parser.parse_args()
IMG = args.file  # 获取图片文件路径及文件名
WIDTH = args.width  # 获取输入的字符画宽度
HEIGHT = args.height  # 获取输入的字符画高度
OUTPUT = args.output  # 获取输入的输出文件路径及文件名

# 字符画所使用的字符集,
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.  ")


# RGB值转换字符的函数，将256灰度映射到70个字符上
def rgb2char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    # 每个字符对应的gray值区间宽度
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    # gray值对应到char_string中的位置（索引值）
    idx = int(gray / unit)
    return ascii_char[idx]


if __name__ == '__main__':
    img = Image.open(IMG)
    img = img.resize((WIDTH, HEIGHT), Image.NEAREST)
    # 保存字符画的字符串
    txt = ""
    # 获取像素点的rgb元组值，如(254, 0, 0)，并将其转化为字符
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += rgb2char(*img.getpixel((j, i)))
        txt += '\n'
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        # 保存字符画
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        # 如果没有输入输出文件路径及文件名，则默认保存在当前目录
        with open("output.txt", 'w') as f:
            f.write(txt)
