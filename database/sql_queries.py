CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY, 
TELEGRAM_ID INTEGER, 
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""


INSERT_USER_TABLE_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
"""

CREATE_REGISTRATION_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS registration_mk
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
FIRST_NAME CHAR(50),
AGE INTEGER,
DIRECTION CHAR(50),
CALL_NUMBER INTEGER
)
"""

INSERT_REGISTRATION_QUERY = """
INSERT INTO registration_mk VALUES (?,?,?,?,?,?)
"""


CREATE_REVIEW_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS review_from_users
(
ID INTEGER PRIMARY KEY, 
TELEGRAM_ID INTEGER, 
REVIEW TEXT
)
"""

INSERT_REVIEW_QUERY = """
INSERT INTO review_from_users VALUES (?,?,?)
"""

CREATE_SIGN_UP_TO_COURSE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS signup_to_course
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
LAST_NAME CHAR(50),
FIRST_NAME CHAR(50),
AGE INTEGER,
DIRECTION CHAR(50),
CALL_NUMBER INTEGER
)
"""

INSERT_SIGN_UP_TO_COURSE_QUERY = """
INSERT INTO signup_to_course VALUES (?,?,?,?,?,?,?)
"""
