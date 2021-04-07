import psycopg2
from cred import la as cred
def add_quotation(input_string):
    return "\'" + input_string + "\'"

def hello_world(request):
    con = psycopg2.connect(host=cred[0], password=cred[3], user=cred[1], database=cred[2])

    cur = con.cursor()

    #values = add_quotation(request['my_id']) + ","
    values =  add_quotation(str(request['url']) )+ ","
    values = values + str(request['price'])+ ","
    values = values + str(request['rating'])+','
    values = values + add_quotation(str(request['name']))
    ret = ""
    try:
        print('INSERT INTO items(image,price,rating,title) VALUES(' + values + ') returning id')
        cur.execute(
            'INSERT INTO items(image,price,rating,title) VALUES(' + values + ') returning title;')
        # ("hello")
    except psycopg2.Error as e:
        # get error code
        error = e.pgcode

        ret = "id is not unique" + error
        # then do something.
    if ret == "":
        while True:
            db_version = cur.fetchone()
            # ("processing")
            if db_version is None:
                break
            ret += db_version[0]
        con.commit()
        cur.close()
        con.close()
        return {"return": ret}
    else:
        con.rollback()
        cur.close()
        con.close()
        return {"return": "error","msg":ret}