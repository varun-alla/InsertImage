from flask import Flask, render_template, flash, request,Markup
from wtforms import Form,validators, StringField, SubmitField,FloatField
import kaka
# App config.
DEBUG = True
app = Flask(__name__,template_folder='Template')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    #my_id = StringField('id:', validators=[validators.required(),validators.length(min=5)])
    url = StringField('url:', validators=[validators.required(),validators.url()])
    rating = FloatField('rating:', validators=[validators.required(), validators.number_range(0,5)])
    price = FloatField('rating:', validators=[validators.required(), validators.number_range(0.99)])
    name = StringField('name:', validators=[validators.required(), validators.Length(min=4, max=75)])
    @app.route("/", methods=['GET', 'POST'])
    def hello() :
        form = ReusableForm(request.form)

        print
        form.errors
        if request.method == 'POST':
            #my_id = request.form['my_id']
            rating = request.form['rating']
            url = request.form['url']
            price = request.form['price']
            name = request.form['name']
            print(" ", url, " ", price, " ", rating, " ", name)
            print('bababa')
        if form.validate():
            # Save the comment here.
            print(form.validate())
            print(form.errors.items())
        else:
            l=['url','rating','price','name']
            kam=l[:]
            print(form.validate())
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


