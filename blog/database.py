from .settings import db
from datetime import datetime
import base64
from bson.objectid import ObjectId
import math

now = datetime.now()

def insert_blog(title, description, image, tags, user_id):
    db.blogs.insert_one(
    {
        'title': title,
        'description': description,
        'image': image,
        'date': now.strftime("%d/%m/%Y %H:%M:%S"),
        'tags': tags,
        'user_id': user_id,
        'comments': []
    }
    )

def get_blogs(page):

    pageCount = math.ceil(db.blogs.find({}).count()/6)
    blog_limit = 0
    blog_skip = 0
    if page == 1:
        blog_limit = 7
        blog_skip = 0
    else:
        blog_limit = 6
        blog_skip = (page - 2)*6 + 7
    blogs = db.blogs.find({}).skip(blog_skip).limit(blog_limit)
    data = []
    for item in blogs:
        item['_id'] = str(item['_id'])
        item['user_id'] = str(item['user_id'])
        # item['image'] = item['image'].decode('utf-8')
        item['image'] = base64.b64encode(item['image']).decode('utf-8')
        users = db.users.find( {"_id": ObjectId(item['user_id'])})
        for user in users:
            item['user_name'] = user['name']
        # print(item['user_id'])
        data.append(item)
    # print(data)
    # pageCount = math.ceil(len(data)/6)

    resp = {'resp': data, 'pageCount': pageCount}
    return resp

def get_blog(id):
    blog = db.blogs.find({"_id": ObjectId(id) })
    data = []
    for item in blog:
        item['_id'] = str(item['_id'])
        item['user_id'] = str(item['user_id'])
        item['image'] = base64.b64encode(item['image']).decode('utf-8')
        user = db.users.find({ "_id": ObjectId(item['user_id']) })
        # print(user)
        for a in user:
            # print(a['name'])
            item['user_name'] = a['name']
            item['user_email'] = a['email']
        for comment in item['comments']:
            u = db.users.find({"_id": ObjectId(comment['user_id'])})
            for _ in u:
                comment['user_name'] = _['name']
        data.append(item)
    # print(data)
    return data
    # print(blog)

def post_comment(id, comment, user_id):
    resp = db.blogs.update({
    "_id": ObjectId(id)
    },
    {
        '$push': {'comments': {'user_id': user_id, 'comment':comment, 'time': now.strftime("%d/%m/%Y %H:%M:%S")}}
    }
    )
    # print(resp)
    return True


def check_login(email, password):
    resp = db.users.find_one({
    "email": email,
    "password": password
    })
    # print(type(resp))
    # print(resp)
    if resp == None:
        return {'success': False}
    resp['_id'] = str(resp['_id'])
    resp['success'] = True
    # print(resp)
    return resp

def sign_up(name, password, email):
    user = db.users.find({
        "email": email
    })
    # print(list(user))
    resp = {}
    if len(list(user)) > 0 :
        resp['success'] = False
        resp['error'] = "User Already Exist!"
    else:
        data = db.users.insert({
        "name": name,
        "email": email,
        "password": password
        })
        inserted_user = db.users.find({
        "_id": ObjectId(data)
        })
        resp['data'] = list(inserted_user)
        resp['data'][0]['_id'] = str(resp['data'][0]['_id'])
        resp['success'] = True
    return resp

def blogs_tag(tag, page):
    count = db.blogs.find({
    "tags": { "$eq" : tag }
    }).collation(
    { 'locale': 'en', 'strength': 2 }
    ).count()
    pageCount = math.ceil(count/6)
    blogs = db.blogs.find({
    "tags": { "$eq" : tag }
    }).collation(
    { 'locale': 'en', 'strength': 2 }
    ). skip((page-1)*6).limit(6)
    data = []
    for item in blogs:
        item['_id'] = str(item['_id'])
        item['image'] = base64.b64encode(item['image']).decode('utf-8')
        item['user_id'] = str(item['user_id'])
        users = db.users.find( {"_id": ObjectId(item['user_id'])})
        for user in users:
            item['user_name'] = user['name']
        data.append(item)

    return {'resp': data, 'pageCount': pageCount}

def delete_blog(blog_id, user_id):
    delete = db.blogs.remove({"_id": ObjectId(blog_id), "user_id": ObjectId(user_id)} , {"justOne": True})
    if delete.get('n', None) == 1:
        return {'success': True}
    else:
        return {'success': False}

def delete_comment(blog_id, user_id, comment):
    delete = db.blogs.update({"_id": ObjectId(blog_id)}, {
    "$pull": {"comments": {"user_id": user_id, "comment":comment}}
    })
    print(delete)
    if delete.get('nModified', None) == 1:
        return {'success': True}
    else:
        return {'success': False}
