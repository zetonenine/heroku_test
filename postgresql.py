import psycopg2


class BD:

    def __init__(self, user="wvchqdkoqufxyl", password="2ced0a7a543f2dbbf87e9852f9e1deede3d5457b57af37f599b708c3f58a4701", dbname="d3pbcui9qttpa1", host="ec2-18-204-74-74.compute-1.amazonaws.com
"):
        self.connection = psycopg2.connect(
            user=user,
            password=password,
            dbname=dbname,
            host=host)
        self.cursor = self.connection.cursor()

    def create(self):
        commands = (
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                chat INTEGER NOT NULL,
                partner_chat INTEGER,
                status BOOLEAN DEFAULT FALSE
                )
            """
        )    
        with self.connection:
            return self.cursor.execute(commands)

    def add_user(self, chatID, status=False):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (chat, status) VALUES (%s, %s)", (chatID, status))

    def user_exists(self, chatID):
        with self.connection:
            self.cursor.execute("SELECT exists(SELECT 1 FROM users WHERE chat = (%s))", (chatID,))
            obj = self.cursor.fetchall()
            return obj[0][0]
