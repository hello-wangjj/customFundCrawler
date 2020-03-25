"""
@Time :    2020/3/21 0021 14:31
@Author:  wangjunjie
@File: OwnProvideTheListOfFund.py
@Software: PyCharm
"""

"""
开放式基金
"""
import requests
import re
import pandas as pd


class GetFundList(object):
    """
    调用get_fund_list来获得基金列表，需实现_set_fund_list_generator方法来设置_fund_list_generator的值
    """

    def __init__(self):
        self.sum_of_fud = None
        self._fund_list_generator = None
        self._set_fund_list_generator()

    def get_fund_list(self):
        return self._fund_list_generator

    def _set_fund_list_generator(self):
        raise NotImplementedError()


class GetFundListByWeb(GetFundList):
    def __init__(self, headers, params, urls):
        self.headers = headers
        self.params = params
        self.urls = urls
        self.fund_list = []
        super(GetFundListByWeb, self).__init__()

    def get_fund_list_from_web(self):
        print("获取基金列表中")
        page = requests.get(url=self.urls, headers=self.headers, params=self.params)
        text = page.text
        pattern = re.compile(r'\d{6}')  # 查找数字
        result1 = pattern.findall(text)
        self.fund_list = result1
        print('共发现' + str(self.sum_of_fund) + '个基金')

    def _set_fund_list_generator(self):
        # columns = ['code']
        # save_file = pd.DataFrame(columns=columns, data=result1)
        # save_file.to_csv('fundList.csv', index=False, encoding="utf-8")
        self.sum_of_fund = len(self.fund_list)
        self._fund_list_generator = (i for i in self.fund_list)

    def write_to_csv(self):
        columns = ['code']
        save_file = pd.DataFrame(columns=columns, data=self.fund_list)
        save_file.to_csv('fundList.csv', index=False, encoding="utf-8")
        print("write to csv success")


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.79"}
    # urls = "http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2019-03-19&ed=2020-03-19&qdii=&tabSubtype=,,,,,&pi=1&pn=5778&dx=1&v=0.4290949550138723"
    urls = "http://fund.eastmoney.com/data/rankhandler.aspx"
    # sc=1nzf 近一年   sc=zzf 近一周  sc=1yzf 近一月  sc=3yzf 近3月  sc=6yzf 近6月  sc=2nzf 近2年  sc=3nzf 近三年 sc=jnzf 今年来  sc=lnzf 成立来
    params = {"op": "ph", "dt": "kf", "ft": "all", "gs": "0", "sc": "zzf", "st": "desc", "sd": "2019-03-21",
              "ed": "2020-03-21", "pi": "1", "pn": "6000", "dx": "1", "v": "0.4290949550138723"}
    test = GetFundListByWeb(headers=headers, params=params, urls=urls)
    test.get_fund_list_from_web()
    ls = test.fund_list
    test.write_to_csv()
    print("success")

