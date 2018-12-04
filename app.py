import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
from keras.models import load_model
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix
from keras.preprocessing import image
from flask import Flask, render_template, request,json,jsonify

global graph
graph = tf.get_default_graph()
model=load_model('F:\\20with91.h5')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
   return render_template("main1.html")

@app.route("/upload", methods=['POST'])
def upload():
   print('hi')
   target = os.path.join(APP_ROOT, '/')
   print(target)

   if not os.path.isdir(target):
       os.mkdir(target)

   for file in request.files.getlist("file"):
       print(file)
       filename = file.filename
       destination = "".join([target, filename])
       print(destination)
       file.save(destination)
   test_image = image.load_img('/'+filename,
                               target_size=(224, 224))
   print(test_image)
   test_image = image.img_to_array(test_image)
   test_image = np.expand_dims(test_image, axis=0)
   with graph.as_default():
        a=model.predict(test_image)

   print(np.argmax(a))

   return jsonify(str(np.argmax(a)
                      ))
@app.route("/vendor", methods=['POST'])

def fucn():
    text = request.json
    print(text['details']['name'])
    name=text['details']['name']
    number=text['details']['number']
    mail=text['details']['mail']
    msg = MIMEMultipart()
    message = "Someone is looking up for pesticides.Call Him up\n Name:"+ name+ "\n Phone number"+number+"\n Mail id:"+mail
    password = "i4ulabs@193"
    msg['To'] = "krishnakanthkrrish1@gmail.com"
    msg['From'] = "neuustore.vnc@gmail.com"
    msg['Subject'] = "New Customer"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))

    #SMS SERVICE
    import urllib.request

    mbl = "91"+number
    astr = "Pesticide Dealers 1: Vaigai Crop Life Mattuthavani +919152655503 2: Jeyaram Agro Trader (Head Office) Tirumangalam +914549320861 +919842980861 3: Madurai Pesticides +914522629019 4: Devi Pesticides Pvt Ltd Simmakkal +914522341624 +914522342612  5: Arun Agro Marketing Kattukottai +919152766389 +919843949566  6:Agribegri.com Harihar Chowk +917984602107 +919327647270  7:ZSAK Merchants Rt Nagar +919152600206  8:Nivshakti Bioenergy Pvt. Ltd. Ballygunge +919152910697  9:Unnat Bio Technologies Pvt Ltd Kankarbagh +919152867643  10: Richa Bio Tech Vasavi College +919152799373"

    data = urllib.request.urlopen(
        "http://api.msg91.com/api/sendhttp.php?country=91&sender=MSGIND&route=4&mobiles=" + mbl + "&authkey=244776ATNebMfpINZd5bd33639&message=" + astr).read()

    print(data)
    return "hello"


def upload():

    return
if __name__ == "__main__":
   app.run(port=4555,host="0.0.0.0", debug=True)