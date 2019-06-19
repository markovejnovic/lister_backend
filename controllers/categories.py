import database
from . import config

"""This file contains functions related to categories

A categories JSON object should appear as such:
    {
        "id": <int:id>,
        "title": <str:title>,
        "description": <str:description>
    }
"""

def get_all():
    """Returns all categories"""
    STMT = "SELECT id, title, description FROM categories;"

    categories = []

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for r in result:
        categories.append(
                {
                    "id": r[0],
                    "title": r[1],
                    "description": r[2]
                }
        )

    return categories

def get_single(category_id):
    """Gets information related to a single category"""

    STMT = "SELECT id, title, description FROM categories WHERE id = %s;"

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT, (category_id, ))
    r = cursor.fetchone()
    cursor.close()

    return {
        "id": r[0],
        "title": r[1],
        "description": r[2]
    }