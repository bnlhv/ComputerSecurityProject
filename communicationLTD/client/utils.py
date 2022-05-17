from datetime import datetime
from typing import Any

from django.db import connection


def create_client_with_sqli_demonstration(full_name: str, email: str, data_package: str) -> Any:
    """ Bypass the ORM and execute raw sql query directly to th database """
    create_query = "INSERT INTO clients(full_name, email, date_created, " \
                   "data_package) VALUES (%s, %s, %s, %s);"
    fetch_query = f"SELECT * FROM clients WHERE full_name = {full_name};"
    with connection.cursor() as cursor:
        cursor.execute(create_query, [full_name, email, data_package, datetime.now()])
        cursor.execute(fetch_query)
        row = cursor.fetchall()
        print(row)

    return row


#fixing the problem 
# def create_client_with_sqli_demonstration(full_name: str, email: str, data_package: str) -> Any:
#     """ Bypass the ORM and execute raw sql query directly to th database """
#     create_query = "INSERT INTO clients(full_name, email, date_created, " \
#                    "data_package) VALUES (%s, %s, %s, %s);"
#     fetch_query = "SELECT * FROM clients WHERE full_name = %s;"
#     with connection.cursor() as cursor:
#         cursor.execute(create_query, [full_name, email, data_package, datetime.now()])
#         cursor.execute(fetch_query, [full_name])
#         row = cursor.fetchall()
#         print(row)

#     return row