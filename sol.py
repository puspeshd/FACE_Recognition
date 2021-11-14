from flask import *
import cv2


app = Flask(__name__)
video = cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

@app.route('/')
def index():
    
    return render_template('video.html')
    

def gen(video):
          
           
             while True:
        
                    _,img=video.read()
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_cascade.detectMultiScale(gray,1.1,4)
                    for(x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    ret,jpeg = cv2.imencode('.jpeg', img)    
                    frame = jpeg.tobytes()
                    yield (b'--frame\r\n'
                               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/confirm')
def confirm():
    
    return render_template('video1.html')
                    
@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run()
    
        