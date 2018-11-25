DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS runs;
DROP TABLE IF EXISTS shoe;

CREATE TABLE user (
        user_id INTEGER PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE run (
        run_id INTEGER PRIMARY KEY,
        date varchar(255),
        distance real,
        time varchar(255),
        user_id INTEGER,
        shoe_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (user_id),
        FOREIGN KEY (shoe_id) REFERENCES shoes (shoe_id)
);

CREATE TABLE shoe (
        shoe_id INTEGER PRIMARY KEY,
        name varchar(255),
        total_miles real,
        target_miles real,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    );

CREATE TABLE lifting_activity (
        lift_id INTEGER PRIMARY KEY,
        date varchar(255),
        desc varchar(255),
        start_time varchar(255),
        end_time varchar(255),
        lifting_data TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES USERS(USER_ID)
);