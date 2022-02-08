from flask import Flask, request
import serial
ser = serial.Serial('/dev/cu.usbserial-1110',9600)

per = 1000

ser.write(per)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    global per
    try:
        new = int(request.args.get("per"))
        print("new: ", new)
        if new != per and new>=10 and new<10000:
            per = new
            r = ser.write(("%d"%per).encode("ascii"))
            print("r: ", r)
    except: 
        pass
    h = "<h1>PHYB54 Harmonic Oscillator</h1> "
    h += "<form action=\"/\" method=\"get\" autocomplete=\"off\"> <label for=\"per\">Period (ms):</label> <input  autocomplete=\"off\" type=\"text\" name=\"per\" value=\"%d\">    <input type=\"submit\" value=\"Submit\"> </form>"%per
    return h

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, threaded=False)
