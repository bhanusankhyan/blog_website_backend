from django.shortcuts import render
import json
from django.http import JsonResponse
from .database import insert_blog, get_blogs, get_blog, post_comment, check_login, sign_up, blogs_tag, delete_blog, delete_comment, forgot_password
from bson.objectid import ObjectId
from django.http import HttpResponse
from django.middleware.csrf import get_token

# Create your views here.
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect, requires_csrf_token



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# @csrf_exempt
# @ensure_csrf_cookie
@csrf_exempt
def insertBlog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user_id = request.POST.get('user_id')
        tags =request.POST.get('tags').split(',')
        image = request.FILES['image'].read()
        res = insert_blog(title, description, image, tags, user_id = ObjectId(user_id))
        return HttpResponse(json.dumps({'resp': res}), content_type="application/json")



@csrf_exempt
# @ensure_csrf_cookie
# @csrf_protect
# @requires_csrf_token
def getBlogs(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        res = get_blogs(page = data['page'])
        token = get_token(request)
        print(token)
        resp = HttpResponse(json.dumps(res), content_type="application/json")
        resp.set_cookie('csrf','sdfjlsdf')
        resp.cookies['token'] = 'asdlkajslkdajlkd'
        return resp

@csrf_exempt
def getBlog(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        resp = get_blog(data['id'])
        return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def postComment(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        resp = post_comment(data['id'], data['comment'], data['user_id'])
        return HttpResponse(json.dumps({'success':True}), content_type="application/json")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        resp = check_login(data['email'], data['password'])
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        resp = sign_up(data['user_name'], data['password'], data['email'])
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def blogsTag(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        resp = blogs_tag(data['tag'], data['page'])
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def deleteBlog(request):
    if request.method == 'DELETE':
        data = request.body
        data = json.loads(data)
        resp = delete_blog(data['blog_id'], data['user_id'])
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def deleteComment(request):
    if request.method == "DELETE":
        data = request.body
        data = json.loads(data)
        resp = delete_comment(data['blog_id'], data['user_id'], data['comment'])
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def forgotPassword(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data)
        resp = forgot_password(data['email'], data['password'])
        return HttpResponse(json.dumps({'success': resp}), content_type="application/json")
