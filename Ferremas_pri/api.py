import json
import requests

class Mindicador:
    def __init__(self, indicador, year):
        self.indicador = indicador
        self.year = year

    def get_dolar_price(self):
        # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
        url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        
        if response.status_code == 200:
            dolar_price = data['serie'][0]['valor']
            return dolar_price
        else:
            # Manejar el caso de error de la solicitud
            print("Error al obtener el precio del dólar:", response.status_code)
            return None

# Ejemplo de uso:
if __name__ == "__main__":
    mindicador = Mindicador('dolar', 2024)
    dolar_price = mindicador.get_dolar_price()
    print("Precio del dólar:", dolar_price)