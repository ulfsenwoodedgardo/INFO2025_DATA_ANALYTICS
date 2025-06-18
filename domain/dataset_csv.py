import pandas as pd
from domain.dataset import Dataset


class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente)
            self.datos = df
            print("CSV cargado")
            if self.validar_datos():
                print ("Datos validados en el CSV")
                # self.transformar_datos()
        except Exception as e:
            print(f"Error cargando CSV:{e}")