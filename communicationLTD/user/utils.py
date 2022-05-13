from typing import Any

from django.db import connection
from django.utils.timezone import now


def create_user_with_sqli_demonstration(username: str, email: str, password: str, is_superuser: bool = False,
                                        first_name: str = "", last_name: str = "", is_staff: bool = False,
                                        is_active: bool = True) -> Any:
    """ Bypass the ORM and execute raw sql query directly to th database """
    create_query = "INSERT INTO auth_user(username, email, password, is_superuser, first_name, last_name, is_staff," \
                   "is_active, date_joined) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    fetch_query = "SELECT * FROM auth_user WHERE username = %s;"
    with connection.cursor() as cursor:
        cursor.execute(create_query, [username, email, password, is_superuser, first_name, last_name,
                                      is_staff, is_active, now()])
        cursor.execute(fetch_query, [username])
        row = cursor.fetchall()
        print(row)

    return row
