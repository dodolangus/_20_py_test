import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font = {'family' : 'normal','size'   : 7}
plt.rc('font', **font)   
class api_covid():
  
    def __init__(self):
        self.value = 'API COVID-19'


    def koneksi_api(self):
        # Parameter
        int_day = '1%3D1'
        fields = '*'
        geo = 'false'
        outsr = '4326'
        method = 'json'
        # API COVID19_Indonesia_per_Provinsi
        url_api_mod = "https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where="+int_day+"&outFields="+fields+"&returnGeometry="+geo+"&outSR="+outsr+"&f="+method+""
        # Get Data
        r = requests.get(url_api_mod)
        data_json = r.json()
        data_features = data_json['features']
        arr_provinsi = []
        for attr in data_features:
            arr_provinsi.append(attr['attributes'])

        return arr_provinsi
        # print(arr_provinsi)


    def graph_plot(self):
        data_prop = self.koneksi_api()
        df = pd.DataFrame(data_prop)
        Provinsi = df['Provinsi']
        Kasus_Positif = df['Kasus_Posi']
        Kasus_Sembuh = df['Kasus_Semb']
        Kasus_Meninggal = df['Kasus_Meni']
        fig, ax = plt.subplots()
        ax.plot([-1, -1], [1, 1], 'red', linewidth=10)
        ax.plot(Provinsi, Kasus_Positif, label="Kasus Positif")
        ax.plot(Provinsi, Kasus_Sembuh, label="Kasus Sembuh",  color='g')
        ax.plot(Provinsi, Kasus_Meninggal, label="Kasus Meninggal", color='r')
        plt.xticks(rotation=90)
        ax.legend()
        plt.show()
    
    def graph_barh(self):
        data_prop = self.koneksi_api()
        df = pd.DataFrame(data_prop)
        Provinsi = df['Provinsi']
        Kasus_Positif = df['Kasus_Posi']
        Kasus_Sembuh = df['Kasus_Semb']
        Kasus_Meninggal = df['Kasus_Meni']
        fig, ax = plt.subplots()
        y_pos = np.arange(len(Provinsi))
        ax.barh(y_pos, Kasus_Positif, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(Provinsi)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Kasus Positif')
        ax.set_title('Jumlah Kasus Per Propinsi')
        plt.show()


main = api_covid()

# print(main.koneksi_api())
# Bentuk Grafik Plot
print(main.graph_plot())
# Betuk Grafik Horizonatal Bar
print(main.graph_barh())