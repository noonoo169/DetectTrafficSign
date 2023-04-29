import pyrebase
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
        data = {"LAT": random.randint(1,10), "LNG": random.randint(11,20), "Label": label}
        self.db.update(data)
        print(data)

