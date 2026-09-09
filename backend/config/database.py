"""
Database connection configuration.

This module is responsible for creating
connections between the backend repositories
and the MariaDB server.
"""

import os

import mariadb
from dotenv import load_dotenv


# Load database configuration from .env
load_dotenv()


def get_db_connection():
    """
    Create and return a connection to MariaDB.

    Returns:
        mariadb.Connection: Active MariaDB connection.
    """

    connection = mariadb.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection
