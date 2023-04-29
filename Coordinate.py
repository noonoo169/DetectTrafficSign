import pyrebase
import serial
class CoordinateFinder:
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
        self.gpgga_info = "$GPGGA,"
        self.ser = serial.Serial ("/dev/ttyAMA0")
    
    def sendGPS(self, label, latitude, longitude ):
        data = {"LAT": latitude, "LONG": longitude, "Label": label}
        self.db.update(data)
        print(data)

    def convert_to_degrees(raw_value):
        decimal_value = raw_value/100.00
        degrees = int(decimal_value)
        mm_mmmm = (decimal_value - int(decimal_value))/0.6
        position = degrees + mm_mmmm
        position = "%.4f" %(position)
        return position    

    def getGpsCoordi(self):
        while True:
            received_data = (str)(self.ser.readline())                   #read NMEA string received
            GPGGA_data_available = received_data.find(self.gpgga_info)   #check for NMEA GPGGA string                 
            if (GPGGA_data_available>0):
                GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string 
                NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
                
                lat = float(NMEA_buff[1])                  #convert string into float for calculation
                long = float(NMEA_buff[3])               #convertr string into float for calculation
                
                lat_in_degrees = self.convert_to_degrees(lat)    #get latitude in degree decimal format
                long_in_degrees = self.convert_to_degrees(long) #get longitude in degree decimal format

                return lat_in_degrees, long_in_degrees

    

