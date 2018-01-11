# -*- coding: utf-8 -*-

import os
import sys
import glob
import hashlib
from PIL import Image


def empty_temp(path):
    if os.path.isdir(path):
        os.system('del /Q ' + path)
    else:
        os.mkdir(path)


def rename(path):
    file_list = glob.glob(path + '\\*')
    for file_name in file_list:
        if os.path.isdir(file_name):
            continue
        os.rename(file_name, file_name + '.png')


def copy(src, dst):
    if not os.path.isdir(dst):
        os.mkdir(dst)
    COMMAND = 'copy ' + src + '\\* ' + dst
    os.system(COMMAND)


def check_size(path):
    flag = False
    with Image.open(path) as img:
        flag = (img.size != (1920, 1080))
    if flag:
        os.remove(path)


def batch_check_size(path):
    file_list = glob.glob(path + '\\*.png')
    for file_name in file_list:
        if os.path.isfile(file_name):
            check_size(file_name)


def read_md5(path):
    ans = list()
    with open(path, 'r') as f:
        for line in f.readlines():
            if line[-1] == '\n' and len(line) == 33:
                ans.append(line[:-1])
            elif len(line) == 32 and line[-1] != '\n':
                ans.append(line)
    return ans


def get_md5(path):
    ans = ''
    with open(path, 'rb') as f:
        ans = hashlib.md5(f.read()).hexdigest()
    return ans


def batch_check_md5(md5_path, dst):
    md5_list = read_md5(md5_path)
    n = len(md5_list)
    file_list = glob.glob(dst + '\\*.png')
    for file_name in file_list:
        m = get_md5(file_name)
        if m in md5_list:
            os.remove(file_name)
        else:
            md5_list.append(m)
    return (md5_list, n)


def update_md5(md5_list, last_num, md5_path):
    with open(md5_path, 'a') as f:
        for i in range(last_num, len(md5_list)):
            f.write(md5_list[i] + '\n')

def rename_md5(dir):
    file_list = glob.glob(dir + "\\*.png")
    for file_name in file_list:
        m = get_md5(file_name)
        os.rename(file_name, dir + '\\' + m + '.png')


def main(argv):
    if len(argv) > 3:
        md5_path = sys.argv[3]
    else:
        md5_path = 'D:\\Users\\Eswai\\Pictures\\Wallpaper\\win_focus\\md5.txt'

    if len(argv) > 2:
        dst_path = sys.argv[2]
    else:
        dst_path = 'D:\\Users\\Eswai\\Pictures\\Wallpaper\\win_focus'
    dst_temp = dst_path + '\\temp'

    if len(argv) > 1:
        src_path = sys.argv[1]
    else:
        src_path = 'C:\\Users\\Eswai\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'

    # 0. EMPTY temp dir
    empty_temp(dst_temp)
    # 1. COPY & RENAME images
    copy(src_path, dst_temp)
    rename(dst_temp)
    # 2. JUDGE image size
    batch_check_size(dst_temp)
    # 3. CHECK repetition by MD5
    rename_md5(dst_temp)

    # (md5_list, last_num) = batch_check_md5(md5_path, dst_temp)
    # update_md5(md5_list, last_num, md5_path)
    # 4. COPY temp to dst
    copy(dst_temp, dst_path)


if __name__ == '__main__':
    main(sys.argv)
