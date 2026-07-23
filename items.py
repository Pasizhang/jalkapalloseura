import db

def add_item(place, times, players, user_id):
    sql = "INSERT INTO items (place, times, players, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [place, times, players, user_id])

def get_items():
    sql = "SELECT id, place FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.place,
                    items.times,
                    items.players,
                    users.id user_id,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id AND
                   items.id = ?"""
    return db.query(sql, [item_id])[0]

def update_item(item_id, place, times, players):
    sql = """UPDATE items SET place = ?,
                              times = ?,
                              players = ?
                          WHERE id = ?"""
    db.execute(sql, [place, times, players, item_id])

def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])
