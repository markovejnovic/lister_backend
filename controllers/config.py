import database

def get_root():
    """Returns the root url of the database"""
    STMT = "SELECT DISTINCT root_url FROM config"

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT)
    val = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return val

def get_currency_short():
    """Returns the currency symbol"""
    STMT = "SELECT DISTINCT currency_short FROM config"

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT)
    val = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return val
