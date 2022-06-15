
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

def home(request):
   return HttpResponse(
      '<!DOCTYPE html> <div style="text-align: center; font-family: sans-serif; position: absolute;top: 30%;left: 50%; transform: translate(-50%, -50%); "> <h1> Welcome to IoT Biometric System. </h1>  <button style="padding: 0.8rem 0.5rem;"> <a href="/accounts/login" style="text-decoration: none; color: #000"> Cick here to Enter the Systen . </a> </button> </div> </html>'
   )    


