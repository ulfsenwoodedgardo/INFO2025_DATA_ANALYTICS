import sqlite3
import pandas as pd

class Datasaver:
    def __init__(self, db_path):
        self.__db_path = db_path


    def guardar_dataframe(self, df, nombre_tabla):
        if df is None:
            print(f"No se puede guardar: datos vacios para {nombre_tabla}")
            return

        if not isinstance(df, pd.DataFrame):
            print(f"Tipo invalido: se esperaba un dataframe, se recibió {type(df)}")
            return
        
        try:
            conn = sqlite3.connect(self.__db_path)
            df.to_sql(nombre_tabla, conn, if_exists= 'replace', index=False)
            conn.close()
            print(f"Datos guardados en tabla: {nombre_tabla}")

        except Exception as e:
            print(f"Error guardando datos: {e}")