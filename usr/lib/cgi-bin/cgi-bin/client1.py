#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgi

from sys import stdin, stdout
from license_parse import Drivers_License
arguments = cgi.FieldStorage()


html = open("/usr/lib/cgi-bin/health-form.html", "r").read()
html = html.replace("$", arguments["license_input"].value, 1)
print("Content-Type: text/html;charset=utf-8\r\n")
print(html)
print("\r\n")