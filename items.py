import db

def add_item(place, times, players, user_id):
    sql = "INSERT INTO items (place, times, players, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [place, times, players, user_id])
