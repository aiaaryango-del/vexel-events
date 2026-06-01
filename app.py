from flask import (
Flask,
render_template,
request,
redirect,
url_for,
Response
)

from models.models import (
db,
Event,
Attendee,
Speaker,
Exhibitor,
FAQ
)

import csv
from io import StringIO

app = Flask(**name**)

app.config['SECRET_KEY'] = 'change-this-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
db.create_all()

# -----------------------------------

# HOME

# -----------------------------------

@app.route('/')
def home():
events = Event.query.all()

```
return render_template(
    'home.html',
    events=events
)
```

# -----------------------------------

# PUBLIC EVENT PAGE

# -----------------------------------

@app.route('/event/<slug>')
def event_page(slug):

```
event = Event.query.filter_by(
    slug=slug
).first_or_404()

speakers = Speaker.query.filter_by(
    event_id=event.id
).all()

exhibitors = Exhibitor.query.filter_by(
    event_id=event.id
).all()

faqs = FAQ.query.filter_by(
    event_id=event.id
).all()

return render_template(
    'event.html',
    event=event,
    speakers=speakers,
    exhibitors=exhibitors,
    faqs=faqs
)
```

# -----------------------------------

# EVENT REGISTRATION

# -----------------------------------

@app.route(
'/event/<slug>/register',
methods=['GET', 'POST']
)
def event_register(slug):

```
event = Event.query.filter_by(
    slug=slug
).first_or_404()

if request.method == 'POST':

    attendee = Attendee(
        event_id=event.id,
        full_name=request.form.get('full_name'),
        phone=request.form.get('phone'),
        email=request.form.get('email'),
        profession=request.form.get('profession'),
        company_name=request.form.get('company_name')
    )

    db.session.add(attendee)
    db.session.commit()

    return redirect(
        url_for(
            'registration_success',
            slug=slug
        )
    )

return render_template(
    'event_register.html',
    event=event
)
```

# -----------------------------------

# SUCCESS PAGE

# -----------------------------------

@app.route('/event/<slug>/success')
def registration_success(slug):

```
event = Event.query.filter_by(
    slug=slug
).first_or_404()

return render_template(
    'registration_success.html',
    event=event
)
```

# -----------------------------------

# EVENT DETAILS

# -----------------------------------

@app.route('/dashboard/event/[int:event_id](int:event_id)')
def event_details(event_id):

```
event = Event.query.get_or_404(event_id)

attendees = Attendee.query.filter_by(
    event_id=event.id
).all()

return render_template(
    'event_details.html',
    event=event,
    attendees=attendees
)
```

# -----------------------------------

# EXPORT CSV

# -----------------------------------

@app.route('/event/[int:event_id](int:event_id)/export')
def export_attendees(event_id):

```
attendees = Attendee.query.filter_by(
    event_id=event_id
).all()

output = StringIO()

writer = csv.writer(output)

writer.writerow([
    'Name',
    'Phone',
    'Email',
    'Profession',
    'Company'
])

for attendee in attendees:

    writer.writerow([
        attendee.full_name,
        attendee.phone,
        attendee.email,
        attendee.profession,
        attendee.company_name
    ])

response = Response(
    output.getvalue(),
    mimetype='text/csv'
)

response.headers[
    'Content-Disposition'
] = 'attachment; filename=attendees.csv'

return response
```

# -----------------------------------

# RUN APP

# -----------------------------------

if **name** == '**main**':
app.run(debug=True)
