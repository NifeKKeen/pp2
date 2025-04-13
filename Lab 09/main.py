from psycopg2 import extras
from pdb import get_db_session
import csv


def get_csv_data(path):
  with open(path) as f:
    reader = csv.reader(f)
    return list(reader)
    for row in reader:
      print(row)


def get_phonebook_records(limit = None):
  db = get_db_session()

  with db.cursor() as cursor:
    cursor.execute(
      """
      SELECT * FROM contacts;
      """
    )
    # db.commit()
    data = cursor.fetchall()
    cursor.close()

    return data
  

def add_phonebook_record(name, phone):
  db = get_db_session()

  with db.cursor() as cursor:
    cursor.execute(
      """
      INSERT INTO contacts (name, phone)
      VALUES (%s, %s);
      """,
      (name, phone)
    )
    db.commit()


def add_phonebook_records(records):
  db = get_db_session()

  with db.cursor() as cursor:
    for record in records:
      extras.execute_values(
        cursor,
        """
        INSERT INTO contacts (name, phone)
        VALUES %s;
        """,
        [(record["name"], record["phone"]) for record in records]
      )
    
    db.commit()


def update_records(conditions, column_names, new_values):  # make sure column_names and new_values are compatible
  db = get_db_session()

  with db.cursor() as cursor:
    cursor.execute(
      f"""
      UPDATE contacts
      SET {", ".join(
        ["=".join([column, f"'{new_value}'"]) for column, new_value in zip(column_names, new_values)]
      )}
      WHERE {" AND ".join(conditions)};
      """
)

    db.commit()
  

def delete_records(conditions):
  db = get_db_session()

  with db.cursor() as cursor:
    cursor.execute(
      f"""
      DELETE FROM contacts
      WHERE {" AND ".join(conditions)};
      """
    )

    db.commit()


def delete_by_col(col_name, value):
  delete_records([f"{col_name}={value}"])


if __name__ == "__main__":
  db = get_db_session()
  # data = get_phonebook_records()
  # print(data)

  # update_records(  # error: sql injection successfully executed URA!
  #   ["name LIKE '%a'", "id > 1"],
  #   ["name", "phone"],
  #   ["A", "B' WHERE 1=1; DROP TABLE contacts; CREATE TABLE razrab_loh (name varchar(1), id INTEGER); SELECT * FROM razrab_loh --"]
  # )

  # uploading data from dummy.csv
  # records = get_csv_data("Lab 09/dummy.csv")
  # add_phonebook_records({"name": r[0], "phone": r[1]} for r in records)

  while "Pahaem":
    print("c: check, i: insert, u: update, d: delete")
    try:
      query = input()
      if query == "c":
        data = get_phonebook_records()
        print(data)
      elif query == "i":
        name, phone = input("name, phone: ").split()
        add_phonebook_record(name, phone)
      elif query == "u":
        col_names = input("Column names: ").split()
        new_values = input("New values, respectively: ").split()
        condition = input("Condition: ")
        update_records([condition], col_names, new_values)
      elif query == "d":
        condition = input("Condition: ")
        delete_records([condition])
    except Exception as e:
      db = get_db_session(True)
      print("Error occured!", e)
