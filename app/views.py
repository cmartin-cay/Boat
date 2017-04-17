from flask import render_template, redirect, url_for, flash, request
from app import app, db
from .models import Cunt, Reason
from .forms import CuntField, CuntVote

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    most_hated = Cunt.query.first()
    form = CuntField()
    reason_id = Reason.query.first()
    remaining = 5000 - Cunt.query.count()
    if form.validate_on_submit():
        cunt = form.cuntname.data
        c = Cunt.query.filter_by(name=cunt).first()
        #If this is a new cunt, add them to the database
        if c is None:
            c1 = Cunt(name=cunt, dickhead=reason_id, votes=1)
            db.session.add(c1)
            db.session.commit()
            flash("You have added {} to the Boat".format(cunt))
            return redirect(url_for('cunt', cuntname=cunt))
        # If this cunt already exists just show the page
        else:
            flash("{} was already on the Boat".format(cunt))
            return redirect(url_for('cunt', cuntname=cunt))
    return render_template('index.html',
                           title="Home",
                           most_hated=most_hated,
                           form=form,
                           remaining=remaining)

@app.route('/<cuntname>', methods=["GET", "POST"])
def cunt(cuntname):
    person = Cunt.query.filter_by(name=cuntname).first()
    form = CuntVote()
    rank = Cunt.query.filter(Cunt.votes > person.votes).count() + 1

    if form.is_submitted():
        person.votes += 1
        db.session.add(person)
        db.session.commit()
        flash("Thank you for voting to put {} closer to the head of the queue".format(cuntname))
        #TODO replace with redirect
        return render_template('cunt.html',
                               title='Cunt',
                               person=person,
                               rank=rank)
    return render_template('cunt.html',
                           title="Cunt",
                           person=person,
                           rank=rank)

@app.route('/who')
def who():
    cunts = Cunt.query.order_by(Cunt.name.asc()).all()
    return render_template('who.html',
                           title="The Cunts",
                           cunts=cunts)

@app.route('/priorty')
def priority():
    cunts = Cunt.query.order_by(Cunt.votes.desc()).all()
    return render_template('priority.html',
                           title="Priority Boarding",
                           cunts=cunts)