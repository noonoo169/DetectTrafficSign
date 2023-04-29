import pyrebase
import pynmea2
import serial
import random
class FBConFig:
    def __init__(self):
        self.firebaseConfig = {
                                "apiKey": "AIzaSyDvwYM2KwdyoQ71hnv90XQAWJuwtu1WuPw",
                                "authDomain": "gps-tracker-5cc33.firebaseapp.com",
                                "projectId": "gps-tracker-5cc33",
                                "storageBucket": "gps-tracker-5cc33.appspot.com",
                                "messagingSenderId": "905173629923",
                                "appId": "1:905173629923:web:ea2b5ce3f2e301b8747ed6",
                                "databaseURL": "https://gps-tracker-5cc33-default-rtdb.asia-southeast1.firebasedatabase.app",
                                }
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = self.firebase.database()
    
    def sendGPS(self, label):
        latitude, longitude = self.getGPS()
        data = {"LAT": latitude, "LNG": longitude, "Label": label}
        self.db.update(data)
        print(data)

    def getGPS(self):
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        n_data = newdata.decode('latin-1')
        if n_data[0:6] == '$GPRMC':
                newmsg=pynmea2.parse(n_data)
                lat=newmsg.latitude
                lng=newmsg.longitude
                return lat, lng

