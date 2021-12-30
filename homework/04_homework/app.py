from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form["name_give"]
    count_receive = request.form["count_give"]
    address_receive = request.form["address_give"]
    phone_receive = request.form["phone_give"]

    doc = {
        "name":name_receive,
        "count":count_receive,
        "address":address_receive,
        "phone":phone_receive
    }
    db.order.insert_one(doc)

    return jsonify({'msg': '이 요청은 POST!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders =  list(db.order.find({}, {"_id":False}))
    return jsonify({"all_orders":orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)