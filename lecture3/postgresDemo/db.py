import psycopg2 

# connect to the db
con = psycopg2.connect(
    host = "127.0.0.1",
    database = "postgres",
    user = "gpila",
    password = "Ambiguedades20",
    port = 5432
)

# cursor
cur = con.cursor()

cur.execute("select * from flights limit 10")

rows = cur.fetchall()

for r in rows:
    print(f"El vuelo que parte de {r[1]} llega a {r[2]} en {r[3]} minutos.")


# close the cursor
cur.close()

# close the connection
con.close()