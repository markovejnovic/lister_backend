from passlib.hash import argon2
import database

def check_creds(username, password):
    """Checks if username and password are in the database

    Returns:
        True - if the creds are registered
        False - if the creds are not registered
    """

    STMT = "SELECT username, password_hash FROM users WHERE username = %s"
    
    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT, (username, ))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user is None:
        return False

    return argon2.verify(password, user[1])
