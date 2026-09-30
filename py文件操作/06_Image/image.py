from PIL import Image

# 获取 Image 对象
image = Image.open('test.jpg')
# 图像格式
print(image.format)
# 图像尺寸
print(image.size)
# 图像模式
print(image.mode)
# 显示图像
# image.show()

# 剪裁图像（左上，右下）
# image.crop((500, 0, 800, 200)).show()

# 缩略图
# image.thumbnail((128, 128))
# image.show()

# 旋转图像
# image.rotate(45).show()

# 翻转图像
# Image.FLIP_LEFT_RIGHT - 水平翻转
# Image.FLIP_TOP_BOTTOM - 垂直翻转
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 操作像素
# for x in range(630, 730):
#     for y in range(50, 140):
#         image.putpixel((x, y), (255, 0, 0)) # RGB值
# image.show()

# 滤镜
from PIL import ImageFilter
image.filter(ImageFilter.CONTOUR).show()



