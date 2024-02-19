from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BlockedApplication


@api_view(http_method_names=["POST"])
def create_blocked_application(request):
    if request.method == 'POST':
        data = request.data
        name = data.get("name")
        BlockedApplication.objects.create(name=name)
    return Response({"status": 201})

@api_view(http_method_names=['GET'])
def get_blocked_applications_list(request):
    apps = BlockedApplication.objects.all()
    data = []
    for i in apps:
        data.append(i.name)
    return Response({"processes":data})
