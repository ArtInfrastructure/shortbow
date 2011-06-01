from django.core import mail
from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class FrontTest(TestCase):
	def setUp(self):
		self.client = Client()

	def tearDown(self):
		pass
	
	def test_api(self):
		call_sid = '1234abcd'
		phone_number = '+12065551212'
		response = self.client.post(reverse('front.api_views.intro'), {'CallSid':call_sid, 'AccountSid':'BOGUS222333', 'CallStatus':'in-progress', 'Caller':phone_number })
		print response
		self.failUnlessEqual(response.status_code, 200, 'status was %s' % response.status_code )





# Copyright 2011 GORBET + BANERJEE (http://www.gorbetbanerjee.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
