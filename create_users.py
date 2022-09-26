from main import User, Session, engine

users=[

    {
        "username": "amita",
        "email": "amita@company.com"
    },
    {"username": "pranavi",
    "email": "pranavi@company.com"
     },
{"username": "harathi",
    "email": "harathi@company.com"
     },
{"username": "fatima",
    "email": "fatima@company.com"
     },
{"username": "srini",
    "email": "srini@company.com"
     },
{"username": "tarun",
    "email": "tarun@company.com"
     },

]

local_session=Session(bind=engine)
'''
#new_user=User(username="hari", email="hari@gmail.com")

#local_session.add(new_user)
#local_session.commit()
'''
for u in users:
    new_user = User(username=u['username'], email=u['email'])
    local_session.add(new_user)
    local_session.commit()

    print(f"Added {u['username']}")