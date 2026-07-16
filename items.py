import db

def add_item(place, times, players, user_id):
    sql = "INSERT INTO items (place, times, players, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [place, times, players, user_id])

def get_items():
    sql = "SELECT id, place FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.place,
                    items.times,
                    items.players,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id AND
                   items.id = ?"""
    return db.query(sql, [item_id])[0]
