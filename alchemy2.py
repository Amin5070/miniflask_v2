"""

NOTE -


metadata_obj contains all the information about our database which is why we pass
it in when creating the table. The metadata.create_all(engine) binds the metadata
to the engine and create the profile table if table does not exist.

"""

import sqlalchemy as db


# define the DB engine
engine = db.create_engine("mysql+pymysql://adam:qwerty123@localhost:3306/starwarsDB")

# # actual connection with database
# engine.connect()

metadata_obj = db.MetaData()

# defining table
profile = db.Table(
    "newprofile",
    metadata_obj,
    db.Column("email", db.String(250), primary_key=True),
    db.Column("name", db.String(250),),
    db.Column("contact", db.Integer)
)

# creates the table
metadata_obj.create_all(engine)


