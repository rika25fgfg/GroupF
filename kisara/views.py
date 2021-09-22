from django.shortcuts import render
from .forms import InquiryForm

from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm