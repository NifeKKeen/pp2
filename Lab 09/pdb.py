import psycopg2
from config import load_config


def connect(cfg):
  try:
    with psycopg2.connect(**cfg) as conn:
      print("Conntected to psql server")
      return conn
  except (psycopg2.DatabaseError, Exception) as e:
    print(e)
    raise e


# BELOW ARE GLOBAL VARIABLES

db = None  # we are not interested in parallel connection,
           # so we should just keep it simple, not overthink :)
def get_db_session(should_reconnect=False):
  global db

  if not should_reconnect and db is not None:
    return db
  
  cfg = load_config("database.ini", "postgresql")
  db = connect(cfg)
  return db
