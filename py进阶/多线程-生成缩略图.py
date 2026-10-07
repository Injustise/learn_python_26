import glob # 用于查找符合特定规则的文件路径名
import os # 提供与操作系统交互的接口，在代码中主要用于路径判断、目录创建和路径字符串处理
import threading # 用于在程序中创建和管理线程，实现并发执行

from PIL import Image

PREFIX = 'thumbnails'

def generate_thumbnail(infile, size, format = 'JPEG'):
    file, ext = os.path.splitext(infile) # 将路径拆分为文件名和扩展名（带.）两部分
    # file = file[file.rfind('/') + 1:]
    file = os.path.basename(file)
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.Resampling.LANCZOS) # Image.Resampling.LANCZOS（抗锯齿）
    img.save(outfile, format)

def main():
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX) # 创建一个单层目录。如果目录已经存在，会抛出 FileExistsError 异常，故先用 if not exists 进行判断

    for infile in glob.glob('image/*.jpg'): # 默认是指当前工作目录下的路径
        for size in (32, 64, 128):
            threading.Thread( # 多线程
                target = generate_thumbnail,
                args = (infile, (size, size))
            ).start()
            '''
            创建一个线程对象。
            target：指定线程要执行的目标函数
            args：传递给目标函数的参数，必须是元组
            '''
''' 一些问题
1.线程爆炸：创建线程本身就需要消耗内存和CPU时间。瞬间创建大量线程，会导致操作系统频繁切换上下文，反而比单线程还要慢，甚至直接导致电脑卡死崩溃。
2.主线程提前结束：如果主线程启动完所有线程后直接退出，而子线程还没执行完，程序可能会直接中断，导致部分缩略图损坏或根本没生成。
'''

if __name__ == '__main__':
	main()         