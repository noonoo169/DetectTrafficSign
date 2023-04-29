#convert raw NMEA string into degree decimal format   
import serial
def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position    

gpgga_info = "$GPGGA,"
ser = serial.Serial ("/dev/ttyAMA0")              #Open port with baud rate
def getGpsCoordi():
    while True:
        received_data = (str)(ser.readline())                   #read NMEA string received
        GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string                 
        if (GPGGA_data_available>0):
            GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string 
            NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
            
            lat = float(NMEA_buff[1])                  #convert string into float for calculation
            long = float(NMEA_buff[3])               #convertr string into float for calculation
            
            lat_in_degrees = convert_to_degrees(lat)    #get latitude in degree decimal format
            long_in_degrees = convert_to_degrees(long) #get longitude in degree decimal format
            
            print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees)
            break

getGpsCoordi()