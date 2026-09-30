import re

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
# ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡', '']
sentences_list = re.split(r'[，。]', poem)
# 过滤掉列表里的空字符串（空字符串 '' 会被视为 False）
sentneces_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)