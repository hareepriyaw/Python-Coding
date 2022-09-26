from main import User, Session, engine

local_session=Session(bind=engine)
'''
users=local_session.query(User).all()[:3]

for user in users:
    print(user.username)
'''
#query for one object

hari=local_session.query(User).filter(User.username=='hari').first()
print(hari)