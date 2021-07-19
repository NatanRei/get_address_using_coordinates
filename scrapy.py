import pandas as pd
from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError

key = 'your_token'
geocoder = OpenCageGeocode(key)

name = input("Digite o Nome do Arquivo:")
coordenadas_df = pd.read_excel(f"{name}.xlsx")
def convert():
    for line in coordenadas_df.index:
        primeira_coordenada = coordenadas_df.loc[line, 'y']
        segunda_coordenada = coordenadas_df.loc[line, 'x']
        primeira_coordenada = "%.7f" % primeira_coordenada
        segunda_coordenada = "%.7f" % segunda_coordenada
        primeira_coordenada = str(primeira_coordenada)
        segunda_coordenada = str(segunda_coordenada)
        try:
            results = geocoder.reverse_geocode(primeira_coordenada, segunda_coordenada, language='pt-br', no_annotations='1')
            if results and len(results):
                print(results[0]['formatted'])
                dados = results[0]['formatted']
                coordenadas_df.loc[line, "result"] = dados
        except RateLimitExceededError as ex:
            print(ex)
            print("error_0x00")
        except InvalidInputError as ex:
            print("error_0x01")
convert()
display(coordenadas_df)
coordenadas_df.to_excel('result.xlsx', index=False)
