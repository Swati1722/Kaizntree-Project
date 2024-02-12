from django.shortcuts import render, HttpResponse, redirect
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
   return redirect('/login')

def handle_login(request):
   try:
      if request.method == 'POST':
         email = request.POST.get('login-email')
         print("email =>", email)
         password = request.POST.get('login-password')
         print("password =>", password)
         user = authenticate(username=email, password=password)
         print("user =>", user)
         if user:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/items')
         else:
            messages.error(request, 'Invalid email or password. Please try again.')
            return render(request, 'login.html')
      else:
         print("into else online 30")
         return render(request, 'login.html')
   except Exception as e:
      print("Error in login page", str(e))

def handle_logout(request):
   logout(request)
   messages.success(request, "Successfully logged out")
   return redirect('/')


def signup(request):
   try:
      if request.method == 'POST':
         # Get the post parameters
         name = request.POST.get('signup-name')
         email = request.POST.get('signup-email')
         pass1 = request.POST.get('signup-password')
         pass2 = request.POST.get('signup-password-confirmed')
         fname = name.split(' ')[0]
         lname = name.split(' ')[1]
         print(name, email, pass1, pass2)
         # Check for errorneous inputs
         
         if pass1 != pass2:
               print("on line 55")
               messages.error(request, "Passwords do not match")
               return redirect('/signup/')
         
         #  create the user
         if User.objects.filter(username = email).first():
               print("on line 61")
               messages.error(request, "This username is already taken")
               return redirect('/signup/')
         
         print("on check 1.")
         myuser = User.objects.create_user(username=email, password= pass1)
         myuser.first_name = fname
         myuser.last_name = lname
         myuser.save()
         messages.success(request , "Your account has been successfully created.")
         print("redirecting to login page.")
         return redirect('/login/')
      print("redirecting to singup page.")
      return render(request, "signup.html")
   except Exception as e:
      print("Error in login page", str(e))
      
   return render(request, "signup.html")

def Item(request):
   try:
      if request.user.is_authenticated:
         item_objs = Items.objects.all()
         total_items = item_objs.count()
         category_objs = Category.objects.all()
         total_categories = category_objs.count()
         tag_objs = Tag.objects.all()

         # Set the number of items to display per page
         items_per_page = 10
         paginator = Paginator(item_objs, items_per_page)
         page = request.GET.get('page', 1)

         try:
               items = paginator.page(page)
         except PageNotAnInteger:
               items = paginator.page(1)
         except EmptyPage:
               items = paginator.page(paginator.num_pages)

         return render(request, "items.html", {
               'items': items,
               'total_items': total_items,
               'total_categories': total_categories,
               'category_objs': category_objs,
               'tag_objs': tag_objs,
         })
      else:
         return HttpResponse("You are not authorized!")
   except Exception as e:
      print("Error in Item page", str(e))

   


class CreateNewCategoryAPI(APIView):
   
   def post(self, request, *args, **kwargs):
      try:
         response = {}
         response["status"] = 500
         if request.user.is_authenticated:
            data = request.data["json_string"]
            data = json.loads(data)
            category_name = data["category_name"]
            Category.objects.create(name=category_name)
            response["status"] = 200
         else:
            return HttpResponse("You are not authorised!")
         
      except Exception as e:
         print("Error in CreateNewCategoryAPI " + str(e))
         
      return Response(data=(response))
   
CreateNewCategory = CreateNewCategoryAPI.as_view()


class CreateNewItemAPI(APIView):
   
   def post(self, request, *args, **kwargs):
      try:
         response = {"status": 500}
         if request.user.is_authenticated:
            data = request.data.get("json_string")
            data = json.loads(data)
            
            sku = data.get("itemSKU")
            name = data.get("itemName")
            category_ids = data.get("selectedCategory")
            tag_ids = data.get("selectedTags")
            in_stock = data.get("inStock")
            available_stock = data.get("availableStock")
            
            item = Items.objects.create(
                  sku=sku,
                  name=name,
                  in_stocks=in_stock,
                  available_stocks=available_stock
            )

            if category_ids:
                  categories = Category.objects.filter(pk__in=category_ids)
                  item.category.set(categories)

            if tag_ids:
                  tags = Tag.objects.filter(pk__in=tag_ids)
                  item.tags.set(tags)

            response["status"] = 200
         else:
            return HttpResponse("You are not authorised!")
         
      except Exception as e:
         print("Error in CreateNewItemAPI: ", str(e))
         
      return Response(data=response)

CreateNewItem = CreateNewItemAPI.as_view()

