# Flask app deployed using AWS(EC2)  


<img width="1436" alt="スクリーンショット 2020-02-08 20 49 22" src="https://user-images.githubusercontent.com/38309191/74084674-8f7b1b80-4ab4-11ea-84a0-0f0b29b8ff24.png">


## Details  

・Example app I made using python web framework [Flask](http://flask.pocoo.org/) and [AWS](https://aws.amazon.com/jp/).

・Using it for showcasing my research demo in the future.

・Now its still just a test , though you can try making grayscale images or classifying images using renet50 pretrained by Imagenet.

[ ＜ Try it here ＞](http://biancaceleste.com/)  

・Updating with new apps in the future.
(※ 2020/02/08 : Due to the lack of resource of virtual machine, I`m not showcasing the flask apps on websites. Check out my [app-page](https://t-koba-96.github.io/section/app/) for other apps. Their are informations for building on your local einvironment.)

## Use it on your local

・Clone this repo:

`$ git clone https://github.com/t-koba-96/flask-app.git`  
`$ cd flask-app`

・Setup virtual environment with venv

`$ python3 -m venv <environment-name>`  
`$ source <environment-name>/bin/activate`

・Install required package  

`$ pip install -r requirements.txt`

・Launch the app  

`$ python app.py`

You can now see your website at local host http://0.0.0.0:80/ 
Now, restile the website as you like.
