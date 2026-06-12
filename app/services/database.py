import os

from dotenv import load_dotenv
from psycopg2.pool import ThreadedConnectionPool

load_dotenv()

pool = ThreadedConnectionPool(
    minconn=5,
    maxconn=20,
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    port=os.getenv("DB_PORT")
)

def get_connection():
    return pool.getconn()

def release_connection(conn):
    pool.putconn(conn)
