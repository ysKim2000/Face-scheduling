from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from matplotlib.pyplot import connect
# from Project1.back.flask.face_detection import face_detection_img
from model.model import Members
import cv2
import numpy as np
# from face_recognition import face_recognition
from face_recognition.face_recognition import face_recognition_cli
import face_detection
import pymysql
import recognition

app = Flask(__name__)
#database 설정파일

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@49.169.175.135:3306/members"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



# def as_dict(self):
#         return {x.name: getattr(self, x.name) for x in self.__table__.columns}

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/image', methods = ['GET', 'POST'])
def image():
    # conn = pymysql.connect(host='49.169.175.135', user='root', charset='utf8', db='members', port=3306)
    # cur = conn.cursor() #디폴트 커서 생성
    # sql = "INSERT INTO tablename () VALUES (\"{}\",\"{}\");"
    # data = []
    # names = []
    # members = Members.query.all()
    # for user in members:
    #     data.append(user.image)
    #     names.append(user.name)
    # print(data)
    try:
        img = cv2.imdecode(np.array(list(request.data), 'uint8'), cv2.IMREAD_COLOR)
        img = cv2.imdecode(np.array(list(request.data), 'uint8'), cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face = np.array(face_detection.face_detection_img([img])[0])
    except:
        print("얼굴이 찍히지 않았습니다.")
        return    
        
    # for i in range(len(data)):
    #     data[i] = cv2.imdecode(np.array(list(data[i]), 'uint8'), cv2.IMREAD_COLOR)
    #     data[i] = cv2.cvtColor(data[i], cv2.COLOR_BGR2RGB)
    #     data[i] = np.array(face_detect([data[i]])[0])
    result = recognition.recognition(face)
    if result:
        name = list(result.keys())[0]
        boolean = list(result.values())[0]
        print("{}님이 입장하셨습니다. Recognition Result {}".format(name, boolean))
    else:
        print("등록되지 않은 사람입니다. Recognition Result{}".format(result))
    # sql = "INSERT INTO users () VALUES (\"{}\",\"{}\");".format(name, boolean)
    # cur.execute(sql)
    # conn.commit()
    # conn.close()
    return render_template('test.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=8080)
