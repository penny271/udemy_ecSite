from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import .models 

import os


class ProductListView(ListView):
    model = Products
    template_name = "TEMPLATE_NAME"

