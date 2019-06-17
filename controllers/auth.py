from passlib.hash import argon2
import database
from .validator import cred_validator

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

def create_user(username, password):
    """Creates a user and commits him to the database

    Parameters:
        username (str): The username
        password (str): Plaintext password
    """

    if not cred_validator.username(username) or \
        not cred_validator.password(password):
        return False

    STMT = "INSERT INTO users (username, password_hash) VALUES (%s, %s);"
    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT, (username, argon2.hash(password)))
    conn.commit()
    cursor.close()
    conn.close()

    return True