# login.py

from database import connect


def register(username, password):

    if username == "" or password == "":
        return False, "Fill all fields"


    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users(username, password)
            VALUES(?, ?)
            """,
            (username, password)
        )

        conn.commit()
        conn.close()

        return True, "Registration successful"


    except:
        conn.close()
        return False, "Username already exists"



def login(username, password):

    conn = connect()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT username 
        FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )


    user = cursor.fetchone()

    conn.close()


    if user:
        return True, user[0]

    else:
        return False, None