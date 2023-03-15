from sqlalchemy import create_engine, MetaData, Table, Column, Integer, VARCHAR, Numeric


host = "127.0.0.1"
user = "adam"
port = 3306
database = "starwarsDB"
password = "qwerty123"


def get_engine():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


if __name__ == "__main__":
    engine = get_engine()
    # engine.connect()
    breakpoint()
    meta = MetaData()

    # definition of table
    books = Table(
        "books",
        meta,
        Column("bookId", Integer),
        Column("book_price", Numeric),
        Column("genre", VARCHAR(250)),
        Column("book_name", VARCHAR(250))
    )

    # actual creation of table using sqlalchemy (ORM)
    meta.create_all(bind=engine)


    # insert records into table
    statement_1 = books.insert().values(
        bookId=1, book_price=12.2, genre="fiction", book_name="old age"
    )

    engine.execute(statement_1)
