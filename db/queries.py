

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT, 
    product_id TEXT,
    photo TEXT
    )
"""


INSERT_store_QUERY = """
    INSERT INTO store (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""

