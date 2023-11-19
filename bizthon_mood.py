# -*- coding: utf-8 -*-
"""Bizthon_Mood.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lysXkjdWynzguUpmYfcJ4hPX1PofzDUe
"""

input_text = input('enter:  ')


# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("bhadresh-savani/distilbert-base-uncased-emotion")
model = AutoModelForSequenceClassification.from_pretrained("bhadresh-savani/distilbert-base-uncased-emotion")

from transformers import pipeline
classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
prediction = classifier(input_text,top_k=None )
print(prediction)

new_record = prediction

for item in prediction:
  print(item['label'], "      ",item['score'])

import sqlite3
from datetime import datetime

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('emotions.db')
cursor = conn.cursor()

# Create the Emotions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Emotions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        joy REAL,
        anger REAL,
        love REAL,
        sadness REAL,
        fear REAL,
        surprise REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

import sqlite3
from datetime import datetime

def insert_emotion_record(emotion_data):
    conn = sqlite3.connect('emotions.db')
    cursor = conn.cursor()

    # Extracting values from the dictionary
    joy = next((item['score'] for item in emotion_data if item['label'] == 'joy'), 0.0)
    anger = next((item['score'] for item in emotion_data if item['label'] == 'anger'), 0.0)
    love = next((item['score'] for item in emotion_data if item['label'] == 'love'), 0.0)
    sadness = next((item['score'] for item in emotion_data if item['label'] == 'sadness'), 0.0)
    fear = next((item['score'] for item in emotion_data if item['label'] == 'fear'), 0.0)
    surprise = next((item['score'] for item in emotion_data if item['label'] == 'surprise'), 0.0)

    # Insert data into the Emotions table
    cursor.execute('''
        INSERT INTO Emotions (joy, anger, love, sadness, fear, surprise)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (joy, anger, love, sadness, fear, surprise))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage


insert_emotion_record(new_record)

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('emotions.db')
cursor = conn.cursor()

# Retrieve all records from the Emotions table
cursor.execute('SELECT * FROM Emotions')
records = cursor.fetchall()

# Display the records
for record in records:
    print("ID:", record[0])
    print("Joy:", record[1])
    print("Anger:", record[2])
    print("Love:", record[3])
    print("Sadness:", record[4])
    print("Fear:", record[5])
    print("Surprise:", record[6])
    print("Timestamp:", record[7])
    print("\n")

# Close the connection
conn.close()

