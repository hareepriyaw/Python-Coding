from main import User, Session, engine
local_session=Session(bind=engine)
user_to_update=local_session.query(User).filter(User.username=='hari').first()
user_to_update.username ='haripriya'
user_to_update.email='haripriya.company.com'

local_session.commit()
