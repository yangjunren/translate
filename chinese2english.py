# -*- coding: utf-8 -*-
# flake8: noqa
import os
from translate import Translator


def chinese2english(folder_path):
    file_list = os.listdir(folder_path)
    os.chdir(folder_path)
    for old_name in file_list:
        # 中文翻译成英文
        translator = Translator(from_lang="chinese", to_lang="english")
        new_name = translator.translate(old_name)
        os.rename(old_name, new_name)


if __name__ == '__main__':
    path = os.getcwd() + "/document/06_flask frame"
    filelist1 = os.listdir(path)
    for old_path in filelist1:
        folder_path1 = path + "/" + old_path
        chinese2english(folder_path1)
    print("翻译完成")
    
# import os
# # 获取指定目录下的所有子目录和文件名
# os.listdir(文件夹路径)
# # 对文件或目录改名
# os.rename(原文件名，新文件名）
# # 切换到当前目录下
# os.chdir(文件夹路径）
