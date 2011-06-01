import os
import re
import Image
import logging
import traceback

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.encoding import force_unicode, smart_unicode
from django.contrib.localflavor.us.forms import phone_digits_re
from django.contrib.localflavor.us.models import PhoneNumberField

def clean_us_phone_number(number):
	number = ''.join([c for c in number if c.isdigit() or c == '+'])
	if number.startswith('+'): number = number[1:]
	if number.startswith('1'): number = number[1:]
	if len(number) != 10: return None
	return '+1%s%s%s' % (number[0:3], number[3:6], number[6:])

def get_by_phone_number(manager, number):
	number = clean_us_phone_number(number)
	if not number: return None
	try:
		return manager.get(phone_number=number)
	except:
		return None

class PhoneManager(models.Manager):
	def get_by_number(self, phone_number):
		return get_by_phone_number(self, phone_number)
		
	def get_or_create_by_number(self, phone_number):
		phone = self.get_by_number(phone_number)
		if phone: return phone
		return self.create(phone_number=phone_number)
		
class Phone(models.Model):
	phone_number = PhoneNumberField(blank=False, null=False, unique=True)
	blocked = models.BooleanField(blank=False, null=False, default=False)
	objects = PhoneManager()
	def __unicode__(self):
	 	number = re.sub('(\(|\)|\s+)', '', self.phone_number)
		matches = phone_digits_re.search(number)
		if not matches: return self.phone_number
		return '(%s) %s-%s' % (matches.group(1), matches.group(2), matches.group(3))

class PhoneCall(models.Model):
	phone = models.ForeignKey(Phone, null=False, blank=False)
	guid = models.CharField(max_length=64, blank=False, null=False, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	completed = models.DateTimeField(blank=True, null=True)

# Copyright 2011 GORBET + BANERJEE (http://www.gorbetbanerjee.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
