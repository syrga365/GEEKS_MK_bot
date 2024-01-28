import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('geeks.db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REGISTRATION_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REVIEW_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_SIGN_UP_TO_COURSE_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_users(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_TABLE_QUERY,
            (None, tg_id, username, first_name, last_name)
        )
        self.connection.commit()

    def sql_insert_registration_users(self, tg_id, first_name, age, direction, call_number):
        self.cursor.execute(
            sql_queries.INSERT_REGISTRATION_QUERY,
            (None, tg_id, first_name, age, direction, call_number)
        )
        self.connection.commit()

    def sql_insert_review_from_users(self, tg_id, review):
        self.cursor.execute(
            sql_queries.INSERT_REVIEW_QUERY,
            (None, tg_id, review)
        )
        self.connection.commit()

    def sql_insert_signup_to_course(self, tg_id, last_name, first_name, age, direction, call_number):
        self.cursor.execute(
            sql_queries.INSERT_SIGN_UP_TO_COURSE_QUERY,
            (None, tg_id,  last_name, first_name, age, direction, call_number)
        )
        self.connection.commit()