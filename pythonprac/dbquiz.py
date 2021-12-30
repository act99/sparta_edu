from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
#
# matrix = db.movies.find_one({"title":"매트릭스"})
# movie_l_mat = list(db.movies.find({"star":matrix["star"]}, {"_id":False}))
#
# print(matrix["star"])
#
# for m in movie_l_mat:
#     m_title = m["title"]
#     print(m_title)

db.movies.update_one({"title":"매트릭스"}, {"$set":{"star":"0"}})