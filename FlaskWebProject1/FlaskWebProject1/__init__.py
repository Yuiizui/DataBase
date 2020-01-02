"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb+srv://yujui:paul1939@cluster0-omrxj.gcp.mongodb.net/test?retryWrites=true&w=majority',
    MONGO_USERNAME='yujui',
    MONGO_PASSWORD='paul1939'
)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False
# app.config.from_envvar(app.config)

mongo = PyMongo(app)
# coursemap = mongo.db.users1.find({})
# json_zip = mongo.db.users2.find({})
# mongo.db.create_collection('student_detail_course')
# mongo.db.course_detail.remove()
# mongo.db.student_detail_course.remove()
# all_course_detail = mongo.db.all_course_detail.find({})
# student_detail = mongo.db.student_detail.find({})
# grade = mongo.db.grade.find({})
# student_detail_course = mongo.db.student_detail_course.find({})
# print(all_course_detail.count())
# course = {}
# pre = {}
# i = 0
# for u2 in json_zip:
#     dic = {}
#     #print(i)
#     if('cProvider' in u2):
#         dic['cProvider'] = u2['cProvider']
#     if('cPhotoLink' in u2):
#         dic['cPhotoLink'] = u2['cPhotoLink']
#     if('cDirectLink' in u2):
#         dic['cDirectLink'] = u2['cDirectLink']
#     if('cDescription' in u2):
#         dic['cDescription'] = u2['cDescription']
#     else:
#         dic['cDescription'] = ""
#     if('cAuthor' in u2):
#         dic['cAuthor'] = u2['cAuthor']
#     else:
#         dic['cAuthor'] = ""
#     if('label' in u2):
#         dic['label'] = u2['label']
#     else:
#         dic['label'] = ""
#     if('cLanguage' in u2):
#         dic['cLanguage'] = u2['cLanguage']
#     else:
#         dic['cLanguage'] = ""
#     if('cTitle' in u2):
#         dic['cTitle'] = u2['cTitle']
#     else:
#         dic['cTitle'] = ""
#     cat_ = eval(u2['tmpCateg'])[0]
#     #print(cat_)
#     tmp = mongo.db.users1.find_one({'index':cat_})
#     #print(tmp)
#     if(tmp is None):
#         dic['pre'] = []
#     else:
#         dic['pre'] = []
#         for k in range(0,len(eval(tmp['pre']))):
#             pre_course = eval(tmp['pre'])[k]
#             find_name = mongo.db.users1.find_one({'index':pre_course})
#             dic['pre'].append(find_name['name'])
#     course[i] = dic
#     i += 1

# #print(len(course))
# if(all_course_detail.count() is 0):
#     for k, v in course.items():
#         mongo.db.all_course_detail.insert(v)
# print(all_course_detail.count())
# print("end")

# student = {}
# i = 0
# for u2 in student_detail:
#     dic = {}
    
#     dic['user_name'] = u2['user_name']
#     dic['enrollment_date'] = u2['enrollment_date']
#     dic['gender'] = u2['gender']
#     dic['department'] = u2['department']
#     dic['used_id'] = u2['used_id']
#     cat_ = u2['used_id']
#     #print(cat_)
#     tmp1 = mongo.db.grade.find({'used_id':cat_})
#     #print(tmp)
#     dic['grade'] = {}
#     for tmp in tmp1:
#         if(tmp['course_name']=='Data Visualization and D3.js'):
#             print("okkkkkk")
#             tmp['course_name'] = tmp['course_name'].replace(".", "_")
#             print(tmp['course_name'])
#         pre_course = tmp['course_name']
#         pre_course_grade = tmp['score']
#         dic['grade'][pre_course] = pre_course_grade
#     student[i] = dic
#     i += 1

# print(student)
# if(student_detail_course.count() is 0):
#     for k, v in student.items():
#         mongo.db.student_detail_course.insert(v)
# print(student_detail_course.count())
# print("end")
import FlaskWebProject1.views
