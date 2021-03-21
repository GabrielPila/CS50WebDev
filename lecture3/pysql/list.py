import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#export DATABASE_URL="postgresql://username:password@host:port/database"

# print(os.getenv("DATABASE_URL"))

engine = create_engine(os.getenv("DATABASE_URL"))
db     = scoped_session(sessionmaker(bind=engine))

def main():
    fligths = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for fligth in fligths:
        print(f"{fligth.origin} to {fligth.destination}, {fligth.duration} minutes")
   
if __name__ == "__main__":
    main()

# ANOTHER WAY -- worked for db.py
# connect to the db
#con = psycopg2.connect(
#    host = "127.0.0.1",
#    database = "postgres",
#    user = "gpila",
#    password = "Ambiguedades20",
#    port = 5432
#)