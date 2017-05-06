# -*- coding: UTF-8 -*-


from __future__ import print_function

import requests
from bs4 import BeautifulSoup
import json
import pandas


def get_detail_news(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    new_detail = {'title': soup.select('h2')[0].text,
                  'time': soup.select('.tc')[0].text,
                  'source': soup.select('.linkRed02')[0].text,
                  'author': soup.select('.col_4')[0].text[3:],
                  'content': '\n'.join([item.text.strip() for item in soup.select('#show_txt p')])}
    return new_detail


def get_news_links(url):
    response_page = requests.get(url)
    response_page.encoding = 'utf-8'
    news_pages_detail = []

    # 去除所有开头的'_requestBelowNewsFunc(('和结尾的')'
    # json.loads 形式读出字典结构
    json_date = json.loads(response_page.text.lstrip('_requestBelowNewsFunc(').rstrip(')'))
    for i in json_date['data']:
        news_pages_detail.append(get_detail_news(i['url']))
    return news_pages_detail


def write_news_to_excel(lines):
    new_list = pandas.DataFrame(lines)
    new_list.head(50)
    new_list.to_excel('test.xlsx')


def main():
    # a = get_detail_news('http://dl.leju.com/news/2017-04-02/13096254167782330783780.shtml')
    # print(a)
    url = 'http://info.leju.com/search/default/index?type=new_news&appid=2015082628&ver=2.0&page=@@@@@&pcount=18&count=0&order={createtime}desc&filter1={deleted@eq}0&format=jsonp&abstract=content@180&filter2={createtime@elt}1491108466&filter4={city@eq}dl&filter5={topcolumn@eq}%E5%9C%B0%E4%BA%A7%E6%96%B0%E9%97%BB&callback=_requestBelowNewsFunc&sign=8fd1418eb597ab8b45be68e2bf5f1d06'
    news_total_detail = []
    for i in range(4, 5):
        news_url = url.replace('@@@@@', str(i))
        # news_url = url.format(i)
        news_list = get_news_links(news_url)
        # 结果追加到news_total 中
        news_total_detail.extend(news_list)
    return news_total_detail
    # len(news_total_links)
    write_news_to_excel(news_total_detail)


if __name__ == '__main__':
    main()
