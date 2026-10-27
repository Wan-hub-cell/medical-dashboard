#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

import json


class SourceDataDemo:

    def __init__(self):
        self.title = '智慧医院医疗运营数据监控大屏'
        self.counter = {'name': '年度总门诊接诊人数', 'value': 12581189}
        self.counter2 = {'name': '年度医保结算金额(元)', 'value': 3912410}
        self.echart1_data = {
            'title': '行业分布',
            'data': [
                {"name": "商超门店", "value": 47},
                {"name": "教育培训", "value": 52},
                {"name": "房地产", "value": 90},
                {"name": "生活服务", "value": 84},
                {"name": "汽车销售", "value": 99},
                {"name": "旅游酒店", "value": 37},
                {"name": "五金建材", "value": 2},
            ]
        }
        self.echart2_data = {
            'title': '省份分布',
            'data': [
                {"name": "浙江", "value": 47},
                {"name": "上海", "value": 52},
                {"name": "江苏", "value": 90},
                {"name": "广东", "value": 84},
                {"name": "北京", "value": 99},
                {"name": "深圳", "value": 37},
                {"name": "安徽", "value": 150},
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "0岁以下", "value": 47},
                {"name": "20-29岁", "value": 52},
                {"name": "30-39岁", "value": 90},
                {"name": "40-49岁", "value": 84},
                {"name": "50岁以上", "value": 99},
            ]
        }
        self.echarts3_2_data = {
            'title': '职业分布',
            'data': [
                {"name": "电子商务", "value": 10},
                {"name": "教育", "value": 20},
                {"name": "IT/互联网", "value": 20},
                {"name": "金融", "value": 30},
                {"name": "学生", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '兴趣分布',
            'data': [
                {"name": "汽车", "value": 4},
                {"name": "旅游", "value": 5},
                {"name": "财经", "value": 9},
                {"name": "教育", "value": 8},
                {"name": "软件", "value": 9},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "安卓", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "IOS", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': '省份TOP',
            'data': [
                {"name": "浙江", "value": 2},
                {"name": "上海", "value": 3},
                {"name": "江苏", "value": 3},
                {"name": "广东", "value": 9},
                {"name": "北京", "value": 15},
                {"name": "深圳", "value": 18},
                {"name": "安徽", "value": 20},
                {"name": "四川", "value": 13},
            ]
        }
        self.echart6_data = {
            'title': '一线城市情况',
            'data': [
                {"name": "浙江", "value": 80, "value2": 20, "color": "01", "radius": ['59%', '70%']},
                {"name": "上海", "value": 70, "value2": 30, "color": "02", "radius": ['49%', '60%']},
                {"name": "广东", "value": 65, "value2": 35, "color": "03", "radius": ['39%', '50%']},
                {"name": "北京", "value": 60, "value2": 40, "color": "04", "radius": ['29%', '40%']},
                {"name": "深圳", "value": 50, "value2": 50, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '北京', 'value': 320},
                {'name': '上海', 'value': 320},
                {'name': '广州', 'value': 520},
                {'name': '深圳', 'value': 700},
                {'name': '成都', 'value': 380},
                {'name': '重庆', 'value': 350},
                {'name': '杭州', 'value': 420},
                {'name': '武汉', 'value': 360},
                {'name': '南京', 'value': 400},
                {'name': '天津', 'value': 320},
                {'name': '西安', 'value': 340},
                {'name': '郑州', 'value': 310},
                {'name': '长沙', 'value': 290},
                {'name': '青岛', 'value': 280},
                {'name': '沈阳', 'value': 270},
                {'name': '大连', 'value': 260},
                {'name': '济南', 'value': 250},
                {'name': '哈尔滨', 'value': 240},
                {'name': '福州', 'value': 230},
                {'name': '厦门', 'value': 320},
                {'name': '昆明', 'value': 210},
                {'name': '合肥', 'value': 200},
                {'name': '南昌', 'value': 195},
                {'name': '石家庄', 'value': 190},
                {'name': '太原', 'value': 185},
                {'name': '南宁', 'value': 180},
                {'name': '长春', 'value': 175},
                {'name': '温州', 'value': 170},
                {'name': '宁波', 'value': 165},
                {'name': '苏州', 'value': 160},
                {'name': '无锡', 'value': 155},
                {'name': '贵阳', 'value': 150},
                {'name': '珠海', 'value': 145},
                {'name': '兰州', 'value': 140},
                {'name': '洛阳', 'value': 135},
                {'name': '海口', 'value': 130},
                {'name': '乌鲁木齐', 'value': 320},
                {'name': '扬州', 'value': 120},
                {'name': '南通', 'value': 115},
                {'name': '烟台', 'value': 110},
                {'name': '海门', 'value': 105},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        sym = data.get('symbolSize')
        if sym is None or (isinstance(sym, (int, float)) and not (sym > 0)):
            sym = 100
        echart = {
            'symbolSize': sym,
            'data': data.get('data'),
        }
        return echart

    def to_dict(self):
        """
        将数据对象转换为字典格式，用于 JSON 序列化
        """
        return {
            'title': self.title,
            'counter': self.counter,
            'counter2': self.counter2,
            'echart1': self.echart1,
            'echart2': self.echart2,
            'echarts3_1': self.echarts3_1,
            'echarts3_2': self.echarts3_2,
            'echarts3_3': self.echarts3_3,
            'echart4': self.echart4,
            'echart5': self.echart5,
            'echart6': self.echart6,
            'map_1': self.map_1,
        }


class SourceData(SourceDataDemo):
    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        # 大标题
        self.title = '智慧医院医疗运营数据实时监控平台'
        
        # 2. 中间滚动的两个大数字
        self.counter = {'name': '年度总门诊接诊人次', 'value': 8845623}
        self.counter2 = {'name': '年度医保结算金额(万元)', 'value': 3912410}
        
        # 3. 左侧柱状图（echart1）：各科室门诊量
        self.echart1_data = {
            'title': '核心科室门诊接诊量分布',
            'data': [
                {"name": "内科", "value": 8500},
                {"name": "外科", "value": 6200},
                {"name": "儿科", "value": 5100},
                {"name": "妇产科", "value": 4800},
                {"name": "骨科", "value": 3900},
                {"name": "眼科", "value": 3500},
                {"name": "口腔科", "value": 2800},
            ]
        }
        
        # 4. 左侧柱状图（echart2）：成各年龄段患者分布
        self.echart2_data = {
            'title': '患者年龄段分布',
            'data': [
                {"name": "0-14岁", "value": 1200},
                {"name": "15-30岁", "value": 3500},
                {"name": "31-45岁", "value": 5200},
                {"name": "46-60岁", "value": 4800},
                {"name": "60岁以上", "value": 6500},
                {"name": "未知", "value": 500},
            ]
        }
        
        # 5. 左下三个饼图（echarts3_1, 3_2, 3_3）
        self.echarts3_1_data = {
            'title': '医保类型占比',
            'data': [
                {"name": "城镇职工医保", "value": 4500},
                {"name": "城乡居民医保", "value": 3200},
                {"name": "自费", "value": 1500},
                {"name": "商业保险", "value": 800},
            ]
        }
        self.echarts3_2_data = {
            'title': '患者来源分布',
            'data': [
                {"name": "本地市区", "value": 6000},
                {"name": "周边县市", "value": 2500},
                {"name": "省外转诊", "value": 1000},
                {"name": "其他", "value": 500},
            ]
        }
        self.echarts3_3_data = {
            'title': '药占比与耗材占比',
            'data': [
                {"name": "药占比", "value": 28},
                {"name": "耗材占比", "value": 15},
                {"name": "检查费占比", "value": 35},
                {"name": "其他", "value": 22},
            ]
        }
        
        # 6. 右侧折线图（echart4）：成24小时急诊/门诊流量趋势
        self.echart4_data = {
            'title': '全天候接诊量趋势',
            'data': [
                {"name": "急诊人次", "value": [10, 8, 5, 3, 2, 5, 15, 30, 45, 50, 48, 55, 60, 58, 50, 45, 40, 35, 30, 25, 20, 15, 12, 10]},
                {"name": "门诊人次", "value": [0, 0, 0, 0, 0, 0, 0, 20, 80, 150, 200, 180, 150, 120, 100, 80, 50, 20, 0, 0, 0, 0, 0, 0]},
            ],
            'xAxis': ['0点', '1点', '2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点', '13点', '14点', '15点', '16点', '17点', '18点', '19点', '20点', '21点', '22点', '23点'],
        }
        
        # 7. 右侧柱状图（echart5）：科室收入TOP排行
        self.echart5_data = {
            'title': '重点科室月度业务收入(万元)',
            'data': [
                {"name": "骨科", "value": 850},
                {"name": "心内科", "value": 720},
                {"name": "普外科", "value": 680},
                {"name": "妇产科", "value": 650},
                {"name": "神经外科", "value": 550},
                {"name": "肿瘤科", "value": 520},
                {"name": "呼吸内科", "value": 480},
                {"name": "消化内科", "value": 450},
            ]
        }
        
        # 8. 右侧环图（echart6）：成各院区/大楼饱和度
        self.echart6_data = {
            'title': '院区床位使用率监控',
            'data': [
                {"name": "本部院区", "value": 92, "value2": 8, "color": "01", "radius": ['59%', '70%']},
                {"name": "东院区", "value": 85, "value2": 15, "color": "02", "radius": ['49%', '60%']},
                {"name": "南院区", "value": 78, "value2": 22, "color": "03", "radius": ['39%', '50%']},
                {"name": "发热门诊", "value": 65, "value2": 35, "color": "04", "radius": ['29%', '40%']},
            ]
        }
        
        # 9. 地图（map_1_data）：保留城市名字（代表该地市患者数或合作医院数）
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '昆明', 'value': 320},
                {'name': '北京', 'value': 420},
                {'name': '上海', 'value': 380},
                {'name': '广州', 'value': 400},
                {'name': '深圳', 'value': 350},
                {'name': '成都', 'value': 300},
                {'name': '重庆', 'value': 280},
                {'name': '杭州', 'value': 270},
                {'name': '武汉', 'value': 250},
                {'name': '西安', 'value': 220}
            ]
        }