from pdb import get_db_session


def create_tables():
  commands = [
    """
    CREATE TABLE contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL
    );
    """,
  ]

  db = get_db_session()
  with db.cursor() as cursor:
    for command in commands:
      cursor.execute(command)
    db.commit()


if __name__ == "__main__":
  create_tables()
  print("Successfully created tables!")
