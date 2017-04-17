from app import app, db
from app.models import Cunt, Reason

c = Cunt.query.get(1)
print(c.name, c.votes)

rank = Cunt.query.count()
print(5000 - rank)