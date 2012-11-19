# -*- coding: utf-8 -*-
import os

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.files.base import ContentFile


def first(request):

	PATH = os.path.abspath(os.path.dirname(__file__))

	return render_to_response('base.html', locals(),\
    context_instance = RequestContext(request))