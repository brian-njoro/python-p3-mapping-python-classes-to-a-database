from config import CONN, CURSOR
import sqlite3

class Song:

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))

        self.id = CURSOR.executr("SELECT last_insert_row_id() FROM songs").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

hello = Song("hello", '25')
hello.save()
despacito = Song('despacito', 'espanyol')
despacito.save()
goosebumps = Song("goosebumps", "astroworld")
goosebumps.save()