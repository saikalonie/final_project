import sqlite3
from db import queries


db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def DataBase_create():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_store)

async def sql_insert_store(name_product, size, price, product_id, photo):
    cursor.execute(queries.INSERT_store_QUERY, (
        name_product, size, price, product_id, photo
    ))
    db.commit()


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():

    conn = get_db_connection()
    products = conn.execute("""
    SELECT s.id, s.name_product, s.size, s.price, s.product_id, s.photo
    FROM store
    INNER JOIN store s 
    ON s.product_id
    """).fetchall()
    conn.close()
    conn.commit()
    return products




