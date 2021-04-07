from flask import Flask, render_template, flash, request,Markup
from wtforms import Form,validators, StringField, SubmitField,FloatField
import kaka
# App config.
app = Flask(__name__,template_folder='Template')
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'

class ReusableForm(Form):
    #my_id = StringField('id:', validators=[validators.required(),validators.length(min=5)])
    url = StringField('url:', validators=[validators.required(),validators.url()])
    rating = FloatField('rating:', validators=[validators.required(), validators.number_range(0,5)])
    price = FloatField('rating:', validators=[validators.required(), validators.number_range(0.99)])
    name = StringField('name:', validators=[validators.required(), validators.Length(min=4, max=75)])
@app.route("/")
def hello() :
    form = ReusableForm(request.form)
            #my_id = request.form['my_id']
    try:
        rating = request.form['rating']
        url = request.form['url']
        price = request.form['price']
        name = request.form['name']
        #print(" ", url, " ", price, " ", rating, " ", name)
        #print('bababa')
    except Exception as e:
        return render_template("home.html",form=form)
    if form.validate():
            # Save the comment here.
        #print(form.validate())
        #print(form.errors.items())
        pass
    else:
        l=['url','rating','price','name']
        kam=l[:]
        #print(form.validate())
        for ik in form.errors.keys():
            if ik in l:
                l.remove(ik)
                if(form.errors[ik][0]=='This field is required.'):
                    pass
                else:
                    break
        if(l==[]):
            pass
        else:
            s = ""
            for ik in kam:
                if ik in form.errors.keys():
                    s += ik +" "+form.errors[ik][0]+'<br>'
            flash(Markup('Error: <br>'+s))
        return render_template('home.html', form=form)
    stk = kaka.hello_world(request.form)
    if(stk['return']=='error'):
        flash('Error '+stk['msg'])
        return render_template('home.html', form=form)
    flash('Input succesfull for item ' + name)
    return render_template('home.html', form=form)
#if(__name__=='__main__'):
#    app.run(debug=True)
