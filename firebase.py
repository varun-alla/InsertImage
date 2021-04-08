import firebase_admin
from firebase_admin import credentials, firestore
import  psycopg2
from cred import la as cred
# initialize sdk
def bla():
    creda = credentials.Certificate("challenge-9ec4c-firebase-adminsdk-eg33o-88af8bf15e.json")
    firebase_admin.initialize_app(creda)
    # initialize firestore instance
    firestore_db = firestore.client()
    '''snapshots = list(firestore_db.collection(u'users').get())
    for snapshot in snapshots:
        print(snapshot.to_dict())#['basket'][0]['id'])'''
    con = psycopg2.connect(host=cred[0], password=cred[3], user=cred[1], database=cred[2])
    cur = con.cursor()
    cur.execute('SELECT * FROM items');
    while True:
        db_version = cur.fetchone()
        # ("processing")
        if db_version is None:
            break
        data = dict()
        data['id'] = str(100000+db_version[0])
        data['image'] =db_version[1]#"https://image.shutterstock.com/image-photo/bangsar-malaysia-january-30th-2020-260nw-1630199971.jpg"
        data['price'] = db_version[2]
        data['rating'] = db_version[3]
        data['title'] = db_version[4]
        k=data
        firestore_db.collection(u'sample').document(data['title']).set(k)
    cur.close()
    con.close()
def kaka(data):
    creda = credentials.Certificate("challenge-9ec4c-firebase-adminsdk-eg33o-88af8bf15e.json")
    firebase_admin.initialize_app(creda)
    # initialize firestore instance
    firestore_db = firestore.client()
    print(data)
    firestore_db.collection(u'sample').document(data['title']).set(data)