INSERT INTO user (email, password)
VALUES
    ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
    ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO run (date, distance, time, user_id, shoe_id)
VALUES
    ("1-1-2011", 11.11, "01:01:01", 0, 0);

INSERT INTO shoe (name, total_miles, target_miles, user_id)
VALUES
    ("Inov8 235", 20.5, 350, 1)