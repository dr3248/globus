# Danai Roumelioti, dr3248@drexel.edu
# CS530: dr3248, Assignment 2 

import sqlite3

class Database:

    def __init__(self, path):
        self.conn = sqlite3.connect(path)

    def select(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        return c.fetchall()

    def execute(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        self.conn.commit()

    def get_goats(self, n, offset):
        data = self.select(
            'SELECT * FROM goats ORDER BY id ASC LIMIT ? OFFSET ?', [n, offset])
        return [{
            'id': d[0],
            'name': d[1],
            'age': d[2],
            'adopted': d[3],
            'image': d[4]
        } for d in data]

    def get_user_goats(self, user_id):
        data = self.select(
            'SELECT * FROM goats WHERE adopted=? ORDER BY id ASC', [user_id])
        return [{
            'id': d[0],
            'name': d[1],
            'age': d[2],
            'adopted': d[3],
            'image': d[4]
        } for d in data]

    def get_num_goats(self):
        data = self.select('SELECT COUNT(*) FROM goats')
        return data[0][0]

    def update_goat(self, id, adopted):
        self.execute('UPDATE goats SET adopted=? WHERE id=?', [adopted, id])

    def create_user(self, name, username, encrypted_password):
        self.execute('INSERT INTO users (name, username, encrypted_password) VALUES (?, ?, ?)',
                     [name, username, encrypted_password])

    def get_user(self, username):
        data = self.select(
            'SELECT * FROM users WHERE username=?', [username])
        if data:
            d = data[0]
            return {
                'id': d[0],
                'name': d[1],
                'username': d[2],
                'encrypted_password': d[3],
            }
        else:
            return None

    def close(self):
        self.conn.close()


# import sqlite3

# class Database:
#     def __init__(self, path):
#         self.conn = sqlite3.connect(path)

#     def select(self, sql, parameters = []):
#         c = self.conn.cursor()
#         c.execute(sql, parameters)
#         return c.fetchall()

#     def execute(self, sql, parameters = []):
#         c = self.conn.cursor()
#         c.execute(sql, parameters)
#         self.conn.commit()

#     def get_bikes(self):
#         data = self.select(
#             'SELECT * FROM bikes'
#         )
#         return [{
#             'id': d[0],
#             'name': d[1],
#             'wheels': d[2],
#             'size': d[3],
#             'motor': d[4],
#             'folding': d[5],
#             'image': d[6],
#             'available': d[7] 
#         } for d in data]

#     def update_bike(self, id, availability):
#         self.execute('UPDATE bikes SET available=? WHERE id=?', [availability, id])

#     def reset_bikes(self):
#         self.execute('UPDATE bikes SET available=3')


#     def close(self):
#         self.conn.close()

