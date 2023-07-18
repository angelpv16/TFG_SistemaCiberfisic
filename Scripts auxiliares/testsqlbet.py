import mysql.connector

conexion = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="manos"
)

cursor = conexion.cursor()

consulta = "INSERT INTO historialmanos (ManoPropia, ManoRival, Board, FichasPropias, FichasRival) VALUES (%s, %s, %s, %s, %s)"
valores = ('Ks6h', '5c2d', '7h4d3s4c7c', 2, 0)  # Valores de ejemplo, actualízalos según sea necesario

cursor.execute(consulta, valores)

conexion.commit()

cursor.close()
conexion.close()
