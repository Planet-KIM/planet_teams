from bs4 import BeautifulSoup
from urllib.request import urlopen
from flask import Flask, render_template, request
import os
from flask_dropzone import Dropzone

#현재진행하는 파일에서 절대경로를 얻어주는 것이다.
currentdir = os.path.abspath(os.path.dirname(__file__))

#웹서버를 구동할 수 있는 부분을 Flask라는 함수에 주고 app이라는 변수에 처리할 수 있도록 합니다.
app = Flask(__name__)
#웹서버에 환경설정을 해줍니다.
app.config.update(
    UPLOADED_PATH=currentdir + '/uploads',
    DROPZONE_ALLOWED_FILE_CUSTOM=True,
    DROPZONE_ALLOWED_FILE_TYPE='.jpeg, .png, .py',
    DROPZONE_MAX_FILE_SIZE=15,
    DROPZONE_MAX_FILES=2,
    DROPZONE_UPLOAD_ON_CLICK=True
)

#어플리케이션에 해당(hello) 라우터를 설정해줍니다.
#이 라우터를 통해서 가는 메소드는 메인페이지 입니다. 해당메인페이지가 호출되면 hello라는 문자열이 반환됩니다.
@app.route("/hello")
def mainpage():
    return "hello"

#dropzone함수에 app의 환경설정을 해줍니다.
dropzone = Dropzone(app)

#페이지로부터 정보교환을 위해 POST와 GET을 사용합니다.
@app.route('/dragdrop', methods=['POST','GET'])
def dragdrop():

    #해당 웹페이지로부터 정보를 보낼 때....
    if request.method == 'POST':
        #보낸 파일로부터 ket와 file을 하나씩 불러옵니다.
       for key, f in request.files.items():
           #위에서 지정한 절대경로와 업로드한 파일이름을 읽어와 합쳐주고 그 해당경로에 저장합니다.
            f.save(app.config['UPLOADED_PATH'] + '/' + f.filename)

    #render_template를 이용하여 drag_drop.html파일을 읽어옵니다.
    return render_template('drag_drop.html')