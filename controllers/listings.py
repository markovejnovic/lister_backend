import database
from . import config

"""This file contains functions related to fetching listings

A listing JSON object should appear as such:
    {
        "id": <int:id>,
        "title": <str:title_of_the_listing>,
        "userId": <int:user_id>,
        "descriptionBrief": <str:short_description>,
        "descriptionLong": <str:long_description>,
        "isActive": <bool:is_active>,
        "price": <str:price_in_configured_currency_with_currency_sign>,
        "images": [
            "http://url1.com",
            "http://url2.com"
        ],
        "categoryId": <int:category_id>
    }
"""

def get_available():
    """Returns the available listings"""
    STMT = "SELECT * FROM listings_default_active_view"

    listings = []

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT)
    result = cursor.fetchall()
    cursor.close()

    for r in result:
        cursor = conn.cursor()
        cursor.execute("SELECT url FROM listing_images WHERE listing_id = %s",
                (r[0], ))
        imgs = [i[0] for i in cursor.fetchall()]
        cursor.close()
        listings.append(
                {
                    "id": r[0],
                    "title": r[1],
                    "userId": r[2],
                    "descriptionBrief": r[3],
                    "descriptionLong": r[4],
                    "isActive": True,
                    "price": r[6],
                    "images": imgs,
                    "categoryId": r[5]
                }
        )

    conn.close()

    return listings

def get_available_q(q):
    """Returns the available listings with query"""
    STMT = "SELECT * FROM listings_default_active_view WHERE SOUNDEX(title) = SOUNDEX(%s);"

    listings = []

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT, (q, ))
    result = cursor.fetchall()
    cursor.close()

    for r in result:
        cursor = conn.cursor()
        cursor.execute("SELECT url FROM listing_images WHERE listing_id = %s",
                (r[0], ))
        imgs = [i[0] for i in cursor.fetchall()]
        cursor.close()
        listings.append(
                {
                    "id": r[0],
                    "title": r[1],
                    "userId": r[2],
                    "descriptionBrief": r[3],
                    "descriptionLong": r[4],
                    "isActive": True,
                    "price": r[6],
                    "images": imgs,
                    "categoryId": r[5]
                }
        )

    conn.close()

    return listings

def get_all():
    """Returns all listings"""
    STMT = "SELECT * FROM listings_default_view"

    listings = []

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT)
    result = cursor.fetchall()
    cursor.close()
    for r in result:
        cursor = conn.cursor()
        cursor.execute("SELECT url FROM listing_images WHERE listing_id = %s",
                (r[0], ))
        imgs = [i[0] for i in cursor.fetchall()]
        cursor.close()
        listings.append(
                {
                    "id": r[0],
                    "title": r[1],
                    "userId": r[2],
                    "descriptionBrief": r[3],
                    "descriptionLong": r[4],
                    "isActive": r[5],
                    "price": r[6],
                    "images": imgs,
                    "categoryId": r[7]
                }
        )

    conn.close()

    return listings

def get_single(listing_id):
    """Returns a single listing"""
    STMT = "SELECT * FROM listings_full_view WHERE id = %s"

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT, (listing_id, ))
    r = cursor.fetchone()
    cursor.close()
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM listing_images WHERE listing_id = %s",
            (listing_id, ))
    imgs = [i[0] for i in cursor.fetchall()]
    cursor.close()

    conn.close()

    return {
        "id": r[0],
        "title": r[1],
        "userId": r[2],
        "descriptionBrief": r[3],
        "descriptionLong": r[4],
        "isActive": r[5],
        "price": r[6],
        "categoryId": r[7],
        "dateTimePosted": r[8].strftime('%Y-%m-%d %H:%M:%S'),
        "views": r[9],
        "images": imgs
    }

def insert(title, user_id, desc_brief, desc_long, is_active, price, cat_id):
    STMT = "INSERT INTO listings (title, user_id, description_brief, " + \
            "description_long, is_active, price, category_id, " + \
            "datetime_posted, views) VALUES (%s, %s, %s, %s, %s, %s, %s, " + \
            "NOW(), 1);"
    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT, (title, user_id, desc_brief, desc_long, is_active,
        price, cat_id))
    conn.commit()
    cursor.close()
    conn.close()
    
