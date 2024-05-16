import random

for i in range(1, 7):
    print(f"INSERT INTO users (login, password_hash, first_name, middle_name, last_name, role_id) VALUES ('user{i}', SHA2('user{i}', 256), 'user{i}_firstname', 'user{i}_middlename', 'user{i}_lastname', {random.randint(1,2)});")