from app.exceptions import UserError, UserAlreadyExistsError, UserDoesNotExistError
from app.db import get_db

def register(username, age):
    if not username or not age:
        raise UserError("Invalid input! Insert correct values for 'username' and 'age'.")
        
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    candidate = cursor.fetchone()

    if candidate:
        raise UserAlreadyExistsError()
    
    cursor.execute("INSERT INTO users (username, age) VALUES (?, ?)", (username, age))

    cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
    user = cursor.fetchone()

    db.commit()
    db.close()

    return dict(user)


def update_usernme(id, new_username):
    if not id or not new_username:
        raise UserError("Invalid input! Insert correct values for 'new_username' and 'id'.")
    
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (id, ))
    candidate = cursor.fetchone()

    if not candidate:
        raise UserDoesNotExistError()
    
    cursor.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, id))
    cursor.execute("SELECT * FROM users WHERE id = ?", (id, ))
    updated_user = cursor.fetchone()

    db.commit()
    db.close()

    return dict(updated_user)