CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    place TEXT,
    times TEXT,
    players INTEGER,
    user_id INTEGER REFERENCES users
);
