#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : zealous (doublezjia@163.com)
# @Date    : 2020/7/9
# @Link    : https://github.com/doublezjia
# @Desc    :

from flask import Flask,redirect,url_for,render_template,request,session
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime

app = Flask(__name__)

# 生成表情包图片函数
def BiaoQingBao(img,content,size,color,location):
    font_set = {}
    typeface = './static/fonts/msyh.ttc'
    # 设置字典添加字体大小、位置、内容等信息
    font_set['type'] = typeface
    font_set['size'] = size
    font_set['content'] = content
    font_set['color'] = color
    font_set['location'] = location

    # 原图路径和新生成保存的图片路径
    old_img = './static/images/%s' % img
    new_img = '%s.png' % datetime.now().strftime("%Y%m%d%H%M%S")

    # 打开图片
    img = Image.open(old_img)
    # 创建画刷
    draw = ImageDraw.Draw(img)
    # 设置字体类型、大小
    font = ImageFont.truetype(font_set['type'], font_set['size'])
    # 根据位置、内容、颜色、字体把内容写入图上
    draw.text(font_set['location'], font_set['content'], font_set['color'], font=font)
    # 保存新图片
    img.save('./static/Nimages/%s' % new_img, 'PNG', quality=95)
    return new_img

# 生成表情包函数，判断是生成那种表情包
def Bqb_main(imgName,content):
    # 初始化变量
    img = 'nb.PNG'
    size = 0
    color = '#000000'
    location = (0, 0)

    # 判断是哪个图片
    if imgName == '抱大腿':
        img = 'bdt.png'
        size = 20
        location = (150, 25)
        content = content[0:4]
        color = '#000000'

    elif imgName == '牛逼':
        img = 'nb.png'
        size = 30
        location = (50, 220)
        content = '%s 牛逼' % content[0:4]
        color = '#000000'

    elif imgName == '女神':
        img = 'ns.png'
        size = 70
        location = (150, 90)
        content = '%s 我女神' % content[0:4]
        color = '#FFFFFF'

    elif imgName == '男神':
        img = 'ns.png'
        size = 70
        location = (150, 90)
        content = '%s 我男神' % content[0:4]
        color = '#FFFFFF'

    elif imgName == '看好你':
        img = 'khn.png'
        size = 25
        location = (20, 190)
        content = '%s 看好你哟' % content[0:4]
        color = '#000000'

    elif imgName == '兄弟':
        img = 'xd.png'
        size = 28
        location = (50, 300)
        content = '%s 我们是兄弟，我怎么会鸽你呢' % content[0:4]
        color = '#FFFFFF'

    New_imgName = BiaoQingBao(img=img,content=content,size=size,color=color,location=location)
    return New_imgName

# 主页
@app.route('/')
def index():
    # 下拉列表的内容
    sel_list = ['抱大腿','牛逼','男神','女神','兄弟','看好你']
    return render_template('index.html',sel_list = sel_list,imgName=session.get('imgName'))

# ajax请求地址，用来生成表情包并返回表情包文件名
@app.route('/msg/',methods=['GET','POST'])
def msg():
    im = request.args.get('im')
    content = request.args.get('content')
    if im != '' and content != '':
        img_Name = Bqb_main(im,content)
    else:
        img_Name = ''
    return img_Name


if __name__ == '__main__':
    app.run()
