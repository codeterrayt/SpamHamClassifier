# 📧 Spam Ham Classifier

A Python Flask application for classifying messages as spam or ham. The classification is based on existing data in the database, fetching LIKE data, and predicting the likelihood of a message being spam or ham.

## Overview

This Spam Ham Classifier utilizes Python and Flask to provide predictions on messages. The classification is driven by analyzing existing data in the database and counting the most likely spam or ham occurrences.

## Setup

### Prerequisites

- Python installed on your server.
- Flask for the web application.
- Database (e.g., using SQLite, MySQL, or another database system).

### Steps

1. **Clone the GitHub Repository:**

    ```bash
    git clone https://github.com/codeterrayt/SpamHamClassifier.git
    cd SpamHamClassifier
    ```

2. **Setup the Database:**

    - Create a database named `spam_detector`.

    - Configure the database connection details in the Flask application.

3. **Run the Application:**

    - Execute the Flask application:

        ```bash
        python main.py
        ```

    - Open your browser and navigate to `http://localhost:{port}` to use the Spam Ham Classifier.

## Usage

1. **Predict Spam or Ham:**

    - Input a message into the application.

    - Get the prediction based on existing data in the database.

## File Structure

- `main.py`: Main Flask application file.
- `templates/`: Folder containing HTML templates for the web application.
- `static/`: Folder containing static files (CSS, images, etc.).

## Notes

- This classifier is designed to make predictions based on existing data in the database.
- Ensure proper database configurations and connection details.
- The application is built using Python Flask for simplicity.

📧 Happy Classifying! 🚀
