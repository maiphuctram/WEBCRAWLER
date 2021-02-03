# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:57:01 2021

@author: Laptop Masstel
"""
"""
import requests
from bs4 import BeautifulSoup

page = requests.get(input("tên link:"))
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find('div', class_='s-result-list')"""
# Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import re

# Hàm tìm kiếm các URL liên quan để tải xuống
# Truyền vào URL cần được quét, và URL xuất phát
# Kết quả trả về là tập hợp các URL tìm được
def tim_url_lien_quan(url, url_goc):
    url_tim_duoc = set()
    link = requests.get(url)
    soup = BeautifulSoup(link.text, 'html.parser')
    results = soup('a', attrs={'href': True})
    for i in results:
        a = i['href']
        mau1 = f'^{url_goc}[^?#]*$'
        mau2 = '^/[^?#]*$'
        if re.match(mau1, a):
            url_tim_duoc.add(a)
        else:
            if re.match(mau2, a):
                url_lien_quan = f'{url_goc}{a}'
                url_tim_duoc.add(url_lien_quan)
    return url_tim_duoc


# Tăng số lượng URL trong tập hợp lên
# Cần truyền vào một set gồm các phần tử cần được duyệt, và URL xuất phát
# Kết quả trả về tập hợp các URL có số phần tử đạt yêu cầu
def them_va_duyet(hang_cho, url_goc, so_luong_trang):
    history = hang_cho
    while (len(hang_cho) > 0) and (len(history) < so_luong_trang):
        url_tim_duoc = tim_url_lien_quan(hang_cho.pop(), url_goc)
        hang_cho = hang_cho | (url_tim_duoc - history)
        history = history | url_tim_duoc
    return history


def main():
    
    history = them_va_duyet(url_tim_duoc)
    for i in history:
        print(i)


if __name__ == '__main__':
    main()