from django.shortcuts import render
import json
from django.http import JsonResponse
from .database import insert_blog, get_blogs, get_blog, post_comment, check_login, sign_up, blogs_tag, delete_blog, delete_comment
from bson.objectid import ObjectId
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# @csrf_exempt
# @ensure_csrf_cookie
@csrf_exempt
def insertBlog(request):
    if request.method == 'POST':
        # print(request.body.get('title'))
        # form = YourForm(request.body)
        # data = form.cleaned_data
        # print(JsonResponse(data))
        # print(json.dumps(request.body.decode('utf-8', errors='ignore')))
        title = request.POST.get('title')
        description = request.POST.get('description')
        user_id = request.POST.get('user_id')
        tags =request.POST.get('tags').split(',')
        image = request.FILES['image'].read()
        # tags = ['Software Development', 'Development']
        insert_blog(title, description, image, tags, user_id = ObjectId(user_id))
        return HttpResponse(json.dumps({'resp': 'success'}), content_type="application/json")



# @csrf_exempt
# @ensure_csrf_cookie
@csrf_exempt
def getBlogs(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        print(data['page'])
        resp = get_blogs(page = data['page'])
        # print(resp)
        # return JsonResponse(json.dumps(resp), safe=False)
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def getBlog(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        # print(data)
        resp = get_blog(data['id'])
        # print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def postComment(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        print(data)
        resp = post_comment(data['id'], data['comment'], data['user_id'])
        return HttpResponse(json.dumps({'success':True}), content_type="application/json")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        resp = check_login(data['email'], data['password'])
        # print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        resp = sign_up(data['user_name'], data['password'], data['email'])
        # print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def blogsTag(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        resp = blogs_tag(data['tag'], data['page'])
        # print(resp)
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
