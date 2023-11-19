# Import necessary libraries
from flask import Flask, request, render_template, jsonify
from transformers import pipeline
import sqlite3

app = Flask(__name__)

# Function to insert emotion record into the SQLite database
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

# Flask route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('data', '')
    print('Received data:', data)

    # Use a pipeline for sentiment analysis
    classifier = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
    prediction = classifier(data, top_k=None)

    # Insert the emotion record into the SQLite database
    insert_emotion_record(prediction)

    return jsonify({'status': 'success'})

# Main entry point for the application
if __name__ == '__main__':
    # Ensure the server is running on host 0.0.0.0 to make it accessible externally
    app.run(debug=True, host='127.0.0.1', port=5000)
    




