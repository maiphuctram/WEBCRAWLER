# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:29:02 2021

@author: Laptop Masstel
"""

import cao
import luuu


def main():
    url_goc = input('Nhập link: ')
    so_luong_trang = int(input('nhập số lượng trang: '))
    hang = cao.tim_url_lien_quan(url_goc, url_goc)
    history = cao.them_va_duyet(hang, url_goc, so_luong_trang)
    luuu.tao_thu_muc(input('Nhập tên thư mục lưu file: '))
    luuu.luu_het_file(history, so_luong_trang)


if __name__ == '__main__':
    main()