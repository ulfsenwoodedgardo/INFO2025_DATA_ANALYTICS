from os import path 
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_api import DatasetAPI
from data.data_saver import Datasaver


# Ruta del archivos
csv_path = path.join(path.dirname(__file__), "files/w_mean_prod.csv")
xlsx_path = path.join(path.dirname(__file__), "files/ventas.xlsx")

# Cargar y Transformar
csv = DatasetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()

xlsx = DatasetExcel(xlsx_path)
xlsx.cargar_datos()
xlsx.mostrar_resumen()

api = DatasetAPI("https://apis.datos.gob.ar/georef/api/provincias")
api.cargar_datos()

# Guardar en base de datos
db = Datasaver("db/recoleccion.db")
db.guardar_dataframe(csv.datos, "w_mean_prod_csv") 
db.guardar_dataframe(xlsx.datos, "ventas_xlsx") 
db.guardar_dataframe(api.datos, "provincias_api") 
