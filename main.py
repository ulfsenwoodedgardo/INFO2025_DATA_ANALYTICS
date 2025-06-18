from os import path 
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel

# Ruta del archivos
csv_path = path.join(path.dirname(__file__), "files/w_mean_prod.csv")
xlsx_path = path.join(path.dirname(__file__), "files/ventas.xlsx")

# Cargar y Transformar
csv = DatasetCSV(csv_path)
csv.cargar_datos()

xlsx = DatasetExcel(xlsx_path)
xlsx.cargar_datos()

# Guardar en base de datos

