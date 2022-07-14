""" (module) context
This contains a context manager for asyncpg
"""

__all__ = ["asyncpg_connect"]

import os
from typing import Optional
from contextlib import asynccontextmanager

import dotenv
import asyncpg

dotenv.load_dotenv()


@asynccontextmanager
async def asyncpg_connect(database_url: Optional[str] = None):
    """
    Custom context manager to use asyncpg

    Parameters
    ----------
        database_url (str, Optional): If not provided it will use the DATABASE_URL 
            from the .env file as the link to the db

    Returns
    -------
        asyncpg.connection.Connection: The connection to the database
    """
    if database_url is None:
        database_url = os.environ["DATABASE_URL"]

    # Connect to the database
    connection = await asyncpg.connect(database_url)

    # Return connection for with statement
    yield connection

    # close connection once context manager is closed
    await connection.close()
