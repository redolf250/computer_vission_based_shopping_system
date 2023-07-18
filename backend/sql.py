
def create_table():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_products(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name varchar(100) NOT NULL UNIQUE,
            product_price BIGINT NOT NULL
            )
        """
    return sql