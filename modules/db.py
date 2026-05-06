import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def save_user(name, role):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, role) VALUES (%s, %s)"
    cursor.execute(query, (name, role))
    conn.commit()
    cursor.close()
    conn.close()

def save_session(user_name, role, question, answer, score, feedback):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO interview_sessions (user_name, role, question, answer, score, feedback)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (user_name, role, question, answer, score, feedback))
    conn.commit()
    cursor.close()
    conn.close()