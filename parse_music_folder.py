import os
import sqlite3
from sqlighter import SQLighter

db = SQLighter('database.db')
path = r'C:\Users\d1409\Documents\Лагерь\Музыка\дискотека'

songs = next(os.walk(path), (None, None, []))[2]


for song in songs:
    try:
        db.add_song(song.replace('.mp3', ''))
        print(f'Песня "{song.replace(".mp3", "")}" добавлена')
    except sqlite3.IntegrityError:
        pass
