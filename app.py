#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2026/01/01
# @Author : 施建文
# @Describe: 医疗业务数据可视化看板后端服务

from flask import Flask, render_template, jsonify
# 只引入医疗数据类
from data import SourceData
from data_fake import get_accumulated_data

app = Flask(__name__)

@app.route('/')
def index():
    # 加载医疗数据源，渲染前端页面
    data = SourceData()
    return render_template('index.html', form=data, title=data.title)

@app.route('/api/data')
def api_data():
    """
    核心API接口：返回医疗数据的 JSON 格式。
    前端页面会每3秒请求一次这个接口，实现数字自动增长。
    """
    # 调用 get_accumulated_data 模拟实时数据增长
    data = get_accumulated_data('data', SourceData)  
    return jsonify(data.to_dict())

if __name__ == "__main__":
    # 启动 Flask 服务
    app.run(host='127.0.0.1', debug=False)