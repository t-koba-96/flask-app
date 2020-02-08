# -*- coding: utf-8 -*-
import os.path
import io , base64  
import cv2
import numpy as np
from PIL import Image
from model import network
from flask import Flask, jsonify, abort, make_response,render_template,url_for,request,redirect,send_file

app = Flask(__name__)

#グレイスケール関数
def gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#エッジ検出関数
def canny(image):
    return cv2.Canny(image, 100, 200)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result',methods = ['post'])
def posttest():
    img_file = request.files['img_file']

    # パスの取得
    fileName = img_file.filename

    # 名前と拡張子に分割
    root, extension = os.path.splitext(fileName)

    # 拡張子の制限
    extension = extension.lower()
    types = set([".jpg", ".jpeg", ".png"])
    if extension not in types:
        return render_template('index.html',message = "Image must be jpg or png ",color = "red")

    # 空のインスタンス作成
    start = io.BytesIO()
    end = io.BytesIO()

    if request.form['task'] == 'imagenet':

        # PILで読み込む
        image = Image.open(img_file).convert("RGB")
        label_1,label_2,label_3 = network.predict(image)
        #空のインスタンスに保存
        image.save(start, 'png')
        #b64型に変換
        s_b64str = base64.b64encode(start.getvalue()).decode("utf-8")
        s_b64data = "data:image/png;base64,{}".format(s_b64str)

        return render_template('predict.html' ,s_img = s_b64data ,cl_label_1 = label_1,cl_label_2 = label_2,cl_label_3 = label_3)

    # グレースケール
    elif request.form['task'] == 'gray':

        # PILで読み込む
        image = Image.open(img_file)
        # opencvで使えるよう変換
        opcv_img = np.asarray(image)
        #グレースケール化
        opcv_img = gray(opcv_img)
        #PILに戻す
        pil_img = Image.fromarray(opcv_img)
        #空のインスタンスに保存
        image.save(start, 'png')
        pil_img.save(end, 'png')
        #b64型に変換
        s_b64str = base64.b64encode(start.getvalue()).decode("utf-8")
        s_b64data = "data:image/png;base64,{}".format(s_b64str)
        e_b64str = base64.b64encode(end.getvalue()).decode("utf-8")
        e_b64data = "data:image/png;base64,{}".format(e_b64str)

        return render_template('result.html' ,s_img = s_b64data ,e_img = e_b64data)
        
    # エッジ検出
    elif request.form['task'] == 'edge':
      
        # PILで読み込む
        image = Image.open(img_file)
        # opencvで使えるよう変換
        opcv_img = np.asarray(image)
        #エッジ検出
        opcv_img = canny(opcv_img)
        #PILに戻す
        pil_img = Image.fromarray(opcv_img)
        #空のインスタンスに保存
        image.save(start, 'png')
        pil_img.save(end, 'png')
        #b64型に変換
        s_b64str = base64.b64encode(start.getvalue()).decode("utf-8")
        s_b64data = "data:image/png;base64,{}".format(s_b64str)
        e_b64str = base64.b64encode(end.getvalue()).decode("utf-8")
        e_b64data = "data:image/png;base64,{}".format(e_b64str)

        return render_template('result.html' ,s_img = s_b64data ,e_img = e_b64data)




# errors
@app.errorhandler(400)
def noimage_error(error):
    return render_template('index.html',message = "Choose both image and processing type!",color = "red")
@app.errorhandler(413)
def size_error(error):
    return render_template('index.html',message = "Image size too big!",color = "red")
@app.errorhandler(503)
def other_error(error):
     return 'InternalServerError\n', 503

# 実行
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=80)