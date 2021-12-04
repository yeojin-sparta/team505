from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongodb 파이썬으로 접속
db = client.dbsparta  # dbsparta 이름의 데이터베이스 생성(get or create)

# users 콜렉션에 도큐먼트 추가
# db.users.insert_one({'name': '덤블도어', 'age': 116})

# 검색
# all_users = list(db.users.find())  # find() 모두 가져오기
# users = list(db.users.find({'age': 116}))  # 조건 검색
# for user in users:
#     print(user)
# dumbledore = db.users.find_one({'age': 116})  # 조건 검색(하나만)
# print(dumbledore)

# 수정
# 실무에서는 수정은 거의 안함
db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})

# 삭제
# 실무에서 삭제는 더더욱 안함
db.users.delete_one({'name': '덤블도어'})
