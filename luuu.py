# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:29:01 2021

@author: Laptop Masstel
"""

# Các thư viện cần thiết
import os
import requests
import codecs


# Hàm Tạo thư mục và chuyển đến thư mục đó
# Cần truyền vào cho hàm Tên thư mục
def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)


# Hàm Lưu file
# Truyền vào url cần lưu và Số thứ tự để đặt tên file cần lưu
def luu_file(url, stt):
    file = codecs.open( str(stt) + 'web' + '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()


# Hàm lưu tất cả các url đã tim được
# Truyền vào một List, set, tuples,... các URL hợp lệ
def luu_het_file(history, so_luong_trang):
    for (stt, url_con) in enumerate(history):
        if stt >= so_luong_trang:
            break
        luu_file(url_con, stt)
        print(f'Trang {stt} : {url_con}')


if __name__ == "__main__":
    main()
    