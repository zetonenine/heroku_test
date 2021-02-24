import psycopg2


class BD:

    def __init__(self, user="dvasvcayevscby", password="e8b87679d0dbfeabde476ba8fef3f904aa5e1f5aeb6dcb1dd0a7dc096005eece", dbname="dadjq0evhseks", host="ec2-52-209-134-160.eu-west-1.compute.amazonaws.com
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
