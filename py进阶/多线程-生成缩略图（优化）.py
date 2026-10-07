import glob, os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

PREFIX = 'thumbnails'
os.makedirs(PREFIX, exist_ok = True) # exist_ok=True：如果目录已经存在，直接跳过，无论单线程还是多线程环境下，都是绝对安全且极简的

def generate_thumbnail(infile, size, format = 'JPEG'):
    try:
        file, ext = os.path.splitext(infile)
        file = os.path.basename(file)
        outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}{ext}'

        img = Image.open(infile)
        img.thumbnail(size, Image.Resampling.LANCZOS) # Image.Resampling.LANCZOS（抗锯齿）
        img.save(outfile, format)
    except Exception as err:
        print(f"Error processing {infile}: {err}")

def main():
    # max_workers：限制并发数
    # with 语句：当 with 里面的代码块执行完时，主线程会自动等待所有提交的任务执行完毕
    with ThreadPoolExecutor(max_workers = 10) as executor: # 多线程
        for infile in glob.glob('image/*.jpg'):
            for size in (32, 64, 128):
                executor.submit(
                    generate_thumbnail, 
                    infile, (size, size))
                '''
                .start() 创建一个全新的线程并执行任务
                .submit() 先将任务扔进队列，线程池内谁空闲谁执行队列中任务
                '''


if __name__ == '__main__':
    main()