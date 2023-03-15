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
    statement_2 = books.insert().values(
        bookId=2, book_price=125.2, genre="non-fiction", book_name="random"
    )
    statement_3 = books.insert().values(
        bookId=3, book_price=152.2, genre="fiction", book_name="harry Potter"
    )
    statement_4 = books.insert().values(
        bookId=4, book_price=121.2, genre="non-fiction", book_name="monk who sold ferraru"
    )
    statement_5 = books.insert().values(
        bookId=5, book_price=124.2, genre="fiction", book_name="sapiens"
    )

    with engine.connect() as conn:
        result = conn.execute(statement_1)
        result = conn.execute(statement_2)
        result = conn.execute(statement_3)
        result = conn.execute(statement_4)
        result = conn.execute(statement_5)
        conn.commit()
