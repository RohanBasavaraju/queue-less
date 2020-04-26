import json
from db import db, Store, Traffic
from flask import Flask, request

app = Flask(__name__)
db_filename = 'cms.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

# Your routes here

@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/api/stores/', methods=['GET'])
def get_stores():
    stores = Store.query.all()
    res = {'success': True, 'data': [st.serialize() for st in stores]}
    return json.dumps(res), 200

@app.route('/api/stores/', methods=['POST'])
def create_store():
    post_body = json.loads(request.data)
    name = post_body['name']
    coordinate = post_body['coordinate']
    store = Store(
        name=name,
        coordinate=coordinate
    )
    db.session.add(store)
    db.session.commit()
    return json.dumps({'success': True, 'data': store.serialize()}), 200


@app.route('/api/course/<int:store_id>/', methods=['GET'])
def get_store(store_id):
    store = Store.query.filter_by(id=store_id).first()
    if not store:
        return json.dumps({'success': False, 'error': 'Store not found'}), 404
    return json.dumps({'success': True, 'data': store.serialize()}), 200


@app.route('/api/traffic/', methods=['POST'])
def create_traffic():
    post_body = json.loads(request.data)
    store = post_body['store']
    hour = post_body['hour']
    traffic = post_body['traffic']
    traf = Traffic(
        store=store,
        hour=hour,
        traffic = traffic
    )
    db.session.add(traf)
    db.session.commit()
    return json.dumps({'success': True, 'data': user.serialize()}), 200


@app.route('/api/user/<int:store_id>/', methods=['GET'])
def get_all_traffic(store_id, hour_requested):
    traffic = Traffic.query.filter_by(storeId=store_id).first()
    if not traffic:
        return json.dumps({'success': False, 'error': 'No traffic data found'}), 404
    return json.dumps({'success': True, 'data': traffic.serialize()}), 200

@app.route('/api/user/<int:store_id>, <int: hour_requested>/', methods=['GET'])
def get_one_traffic(store_id, hour_requested):
    traffic = Traffic.query.filter_by(storeId=store_id, hour = hour_requested).first()
    if not traffic:
        return json.dumps({'success': False, 'error': 'No traffic data found'}), 404
    return json.dumps({'success': True, 'data': traffic.serialize()}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
