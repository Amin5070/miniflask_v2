"""

engine =
"""

from sqlalchemy import create_engine


host = "127.0.0.1"
user = "adam"
port = 3306
database = "starwarsDB"
password = "qwerty123"


def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


if __name__ == "__main__":
    connection = get_connection()
    if connection:
        print("[ INFO ] connection has been created successfully")
        connection.connect()
        breakpoint()
    else:
        print("[ ERROR ] please check your DB username and password")
