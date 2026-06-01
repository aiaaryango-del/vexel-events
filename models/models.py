from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# -----------------------------

# ORGANIZERS

# -----------------------------

class Organizer(db.Model):
**tablename** = "organizers"

```
id = db.Column(db.Integer, primary_key=True)

name = db.Column(
    db.String(150),
    nullable=False
)

email = db.Column(
    db.String(150),
    unique=True,
    nullable=False
)

password_hash = db.Column(
    db.String(255),
    nullable=False
)
```

# -----------------------------

# EVENTS

# -----------------------------

class Event(db.Model):
**tablename** = "events"

```
id = db.Column(
    db.Integer,
    primary_key=True
)

organizer_id = db.Column(
    db.Integer,
    db.ForeignKey('organizers.id')
)

title = db.Column(
    db.String(255),
    nullable=False
)

slug = db.Column(
    db.String(255),
    unique=True,
    nullable=False
)

description = db.Column(
    db.Text
)

date = db.Column(
    db.String(100)
)

venue = db.Column(
    db.String(255)
)

banner_image = db.Column(
    db.String(255)
)
```

# -----------------------------

# ATTENDEES

# -----------------------------

class Attendee(db.Model):
**tablename** = "attendees"

```
id = db.Column(
    db.Integer,
    primary_key=True
)

event_id = db.Column(
    db.Integer,
    db.ForeignKey('events.id')
)

full_name = db.Column(
    db.String(255),
    nullable=False
)

phone = db.Column(
    db.String(50),
    nullable=False
)

email = db.Column(
    db.String(255),
    nullable=False
)

profession = db.Column(
    db.String(255)
)

company_name = db.Column(
    db.String(255)
)

registration_time = db.Column(
    db.DateTime,
    default=datetime.utcnow
)
```

# -----------------------------

# SPEAKERS

# -----------------------------

class Speaker(db.Model):
**tablename** = "speakers"

```
id = db.Column(
    db.Integer,
    primary_key=True
)

event_id = db.Column(
    db.Integer,
    db.ForeignKey('events.id')
)

name = db.Column(
    db.String(255),
    nullable=False
)

designation = db.Column(
    db.String(255)
)

company = db.Column(
    db.String(255)
)

image = db.Column(
    db.String(255)
)
```

# -----------------------------

# EXHIBITORS

# -----------------------------

class Exhibitor(db.Model):
**tablename** = "exhibitors"

```
id = db.Column(
    db.Integer,
    primary_key=True
)

event_id = db.Column(
    db.Integer,
    db.ForeignKey('events.id')
)

company_name = db.Column(
    db.String(255),
    nullable=False
)

category = db.Column(
    db.String(255)
)

website = db.Column(
    db.String(255)
)

logo = db.Column(
    db.String(255)
)
```

# -----------------------------

# FAQS

# -----------------------------

class FAQ(db.Model):
**tablename** = "faqs"

```
id = db.Column(
    db.Integer,
    primary_key=True
)

event_id = db.Column(
    db.Integer,
    db.ForeignKey('events.id')
)

question = db.Column(
    db.Text,
    nullable=False
)

answer = db.Column(
    db.Text,
    nullable=False
)
```
