from PIL import Image
import pytesseract
import cv2
import numpy as np

# # 读取图像
# image = Image.open('./images/yefeng001.png')
#
# # 将图像转换为灰度
# gray_image = image.convert('L')
#
# # 使用OpenCV进行二值化处理
# _, binary_image = cv2.threshold(np.array(gray_image), 130, 255, cv2.THRESH_BINARY)
#
# # 使用Tesseract OCR进行识别
# text = pytesseract.image_to_string(binary_image)
#
# # 打印识别结果
# print("识别结果:", text)
#
# # 显示原始图像
# image.show()
#
# # 显示处理后的图像
# Image.fromarray(binary_image).show()

data_split = "PG35ybn5A40B324VY6H5424490gOK05E15uU7IM#12133311132213322131".split("#")
scode = data_split[0]
sxh = data_split[1]
code = "202013030313" + "%%%" + "Zsh-1234"
encoded = ""

for i in range(len(code)):
    if i < 20:
        encoded += code[i:i + 1] + scode[0:int(sxh[i:i + 1])]
        scode = scode[int(sxh[i:i + 1]):len(scode)]
    else:
        encoded += code[i:len(code)]
        i = len(code)
        break
print(encoded)
