import database
from . import config

"""This file contains functions related to user management

A user JSON object should appear as such:
    {
        "id": <int:id>,
        "username": <str:username>,
        "email": <str:email>,
        "wechat": <str:wechat_username>,
        "wechat_qr": <str:wechat_qr_image_url>,
        "messenger": <str:messenger_username>,
        "whatsapp": <str:whatsapp_username>
    }
"""

def get_all():
    """Returns all users"""
    STMT = "SELECT * FROM users_public_view"

    users = []

    conn = database.get_conn()
    cursor = conn.cursor()
    cursor.execute(STMT)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for r in result:
        users.append(
                {
                    "id": r[0],
                    "username": r[1],
                    "email": r[2],
                    "wechat": r[3],
                    "wechat_qr": r[4],
                    "messenger": r[5],
                    "whatsapp": r[6]
                }
        )

    return users
