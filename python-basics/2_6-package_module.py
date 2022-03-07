#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 모듈, 패키지

# Section. 모듈

# sms.py
class SMS:
  def send(self, from_number, to_number, body):
    print(from_number + " 에서 " + to_number + " 로 문자를 보냈습니다: " + body)

# email.py
class Email:
  def send(self, from_address, to_address, body):
    print(from_address + " 에서 " + to_address + " 로 이메일을 보냈습니다: " + body)

import sms
import email

s = sms.SMS()
s.send("010-1234-1234", "010-5123-1231", "안녕, 잘 지내니?")
e = email.Email()
e.send("wonie@gmail.com", "charles@gmail.com", "난 잘 지내")

# ./msg/sms.py
# ./msg/email.py

import msg.sms
import msg.email
s = msg.sms.SMS()
e = msg.email.Email()

from msg import sms
from msg import email
from msg import *
