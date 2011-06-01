import traceback
import logging
from datetime import datetime, date, timedelta

from django.conf import settings
from django.db.models import Q
from django.template import RequestContext
from django.contrib.auth.models import User
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, Http404, HttpResponseServerError, HttpResponseRedirect, HttpResponsePermanentRedirect

import twilio

from models import PhoneCall, Phone

VOICE = twilio.Say.WOMAN
LANGUAGE = twilio.Say.ENGLISH

def say(message):
	result = twilio.Response()
	result.append(twilio.Say(message, voice=VOICE, language=LANGUAGE))
	return result
	
def quick_say(message): return str(say(message))

def twilio_request(function):
	"""Decorate the request object with an incoming_phone and call attributes"""
	if not settings.REQUIRE_TWILIO_AUTH: return function
	def _rta(request, *args, **kwargs):
		if not request.REQUEST.get('Caller', None):
			return HttpResponse(quick_say("Sadly, I did not receive your number.  Good bye."))			
		phone = Phone.objects.get_or_create_by_number(request.REQUEST.get('Caller'))
		if phone.blocked:
			logging.debug('Refusing a blocked phone: %s' % request.REQUEST.get('Caller'))
			return HttpResponse(quick_say("Sorry, that did not work.  Good bye."))
		request.incoming_phone = phone
		
		if request.REQUEST.get('CallStatus', None) == 'completed':
			request.call = PhoneCall.objects.get(guid=request.REQUEST.get('CallSid'))
			request.call.completed = datetime.now()
			request.call.save()
		else:
			request.call = PhoneCall.objects.get_or_create(phone=request.incoming_phone, guid=request.REQUEST.get('CallSid'))[0]

		return function(request, *args, **kwargs)
	return _rta

@csrf_exempt
@twilio_request
def intro(request):
	"""The view called when a phone call arrives at Twilio"""
	logging.debug("%s called %s" % (request.REQUEST.get('Caller', None), request.REQUEST.get('Called', None)))
	return HttpResponse(quick_say('Hey, this is working.'))
