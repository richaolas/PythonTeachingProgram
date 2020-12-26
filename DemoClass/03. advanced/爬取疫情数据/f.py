import requests
import json
class epidemic_data():
  def __init__(self, province):
    self.url = url
    self.header = header
    self.text = {}
    self.province = province
    # self.r=None
  def down_page(self):
    r = requests.get(url=url, headers=header)
    self.text = r.text
    # self.r = r
  def parse_page(self):
    data_str = json.loads(self.text)['data']
    data_json = json.loads(data_str)
    data_tree_dict = data_json['areaTree'][0]['children'] # 取中国的省列表
    prt_str = []
    prt_str.append("数据更新时间："+data_json['lastUpdateTime'])
    prt_str.append("全国" + ":" + "累计确诊病例：" + str(data_json['chinaTotal']['confirm']) + \
            "累计疑似病例：" + str(data_json['chinaTotal']['suspect']) + \
            "累计死亡病例：" + str(data_json['chinaTotal']['dead']) + \
            "累计出院病例：" + str(data_json['chinaTotal']['heal']) + \
            "今日新增确诊病例：" + str(data_json['chinaAdd']['confirm']) + \
            "今日新增疑似病例：" + str(data_json['chinaAdd']['suspect']) + \
            "今日新增死亡病例：" + str(data_json['chinaAdd']['dead']) + \
            "今日新增出院病例：" + str(data_json['chinaAdd']['heal']))
    for province_list in data_tree_dict:
      for provice_name in self.province:
        if provice_name in province_list['name']:
          city_list = province_list['children']
          prt_str.append(province_list['name'] + ":" + "累计确诊病例：" + str(province_list['total']['confirm']) + \
                    "累计死亡病例：" + str(province_list['total']['dead']) + \
                    "累计出院病例：" + str(province_list['total']['heal']))
          if provice_name == '湖北':
            for data_dict in city_list:
              prt_str.append(data_dict['name'] + ":" + "累计确诊病例：" + str(data_dict['total']['confirm']) + \
                      "累计死亡病例：" + str(data_dict['total']['dead']) + \
                      "累计出院病例：" + str(data_dict['total']['heal']) + \
                      "今日确诊病例：" + str(data_dict['today']['confirm']))
    for item in prt_str:
      print(item)
  def show(self):
    self.down_page()
    self.parse_page()
if __name__ == '__main__':
  url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
  header = {
    'user - agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
  }
  province = ['湖北','山东']
  wf = epidemic_data(province)
  wf.show()