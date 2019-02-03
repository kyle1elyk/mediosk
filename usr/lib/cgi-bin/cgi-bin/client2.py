#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgi


from sys import stdin, stdout
from license_parse import Drivers_License
from sickness import sickness
from bucket import Bucket_Manager
import serial
import urllib2
import json
log = ""
pill_amount = 0
arguments = cgi.FieldStorage()

raw_data = urllib2.urlopen("http://mediosk.com/data.json").read()
parsed_dr_data = json.loads(raw_data)

license = Drivers_License(arguments["license_string"].value)
argument_dictionary = {}
for i in arguments.keys():
    argument_dictionary[i] = arguments[i].value

sicc_dicc = sickness(argument_dictionary)



html = open("/usr/lib/cgi-bin/PatientEnd.html", "r").read()
html = html.replace("$", license.first_name, 1)

if (sicc_dicc["br"] >= parsed_dr_data["minlevel"]):
    html = html.replace("$", "It seems you're at high risk for a bacterial infection. Dispensing your presciption now", 1)
    log = "Patient " + license.first_name + " " +license.last_name + " is at high risk for bacterial infection. Their risk score is " + str(sicc_dicc["br"])
    pill_amount = 3
elif (sicc_dicc["vr"] >= parsed_dr_data["minlevel"]):
    html = html.replace("$", "It seems you're at high risk for a viral infection Dispensing your presciption now", 1)
    log = "Patient " + license.first_name + " " +license.last_name + " is at high risk for viral infection. Their risk score is " + str(sicc_dicc["vr"])
    pill_amount = 4
elif (sicc_dicc["sr"] >= parsed_dr_data["minlevel"]):
    html = html.replace("$", "Your symptoms seem low-concern. Mild symptom treatment is recommended. Dispensing your presciption now", 1)
    log = "Patient " + license.first_name + " " +license.last_name + " has general symptoms. Light sympotom treatment is recommended. Their risk score is " + str(sicc_dicc["sr"])
    pill_amount = 2
elif (sicc_dicc["hosr"] >= parsed_dr_data["minlevel"]):
    html = html.replace("$", "Your symptoms are of high concern. Please visit a hospital. Dispensing your presciption now", 1)
    log = "Patient " + license.first_name + " " +license.last_name + " IS AT HIGH RISK. HOSPITAL VISIT STRONGLY RECOMMENDED! Their risk score is " + str(["hosr"])
    pill_amount = 4
else:
    html = html.replace("$", "Your symptoms are of lowest concern. No medication is recommended, Dr. Mango says you're good to go", 1)
    log = "Patient " + license.first_name + " " +license.last_name + " is at no percieved risk. No action is recommended."

#ser = serial.Serial('/dev/ttyUSB0', 9600)
with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
    ser.write("{mode=2,num=$}\r\n".replace("$", pill_amount))
    

print("Content-Type: text/html;charset=utf-8\r\n")
print(html)
print("\r\n")