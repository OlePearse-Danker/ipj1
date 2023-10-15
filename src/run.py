import pandas as pd 
import csv
from datetime import datetime
import streamlit as st




def main():
    st.set_page_config(page_title= "Gesamtbilanz Energiewende",
                        page_icon=":bar chart:",
                        layout = "wide"
    )

    st.title("Hello this is working!")

    excel_file = './res/file.xlsx'
    sheetname = 'Realisierte_Erzeugung_202001010'


    df = pd.read_excel(excel_file, 
                        sheet_name = sheetname,
                        usecols='A:O',
                        header= 3 )

    st.dataframe(df)

    with open('./res/file.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')

        next(reader)
        data = set()
        
        for row in reader:
            # skip header

            data_entry = Data(row)
            data.add(data_entry)

    print('Durchschnittlicher PV-Leistungsertrag in MWh: ', sum([d.pv for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Biomasse-Leistungsertrag in MWh: ', sum([d.biomass for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Wasserkraf-Leistungsertrag in MWh: ', sum([d.water for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Wind-Offshore-Leistungsertrag in MWh: ', sum([d.wind_off for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Wind-Onshore-Leistungsertrag in MWh: ', sum([d.wind_on for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Sonstige-Leistungsertrag in MWh: ', sum([d.other for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Nuklearenergie-Leistungsertrag in MWh: ', sum([d.nuclear for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Braunkohle-Leistungsertrag in MWh: ', sum([d.coal for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Steinkohle-Leistungsertrag in MWh: ', sum([d.stone_coal for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Erdgas-Leistungsertrag in MWh: ', sum([d.gas for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Pumpspeicherkraft-Leistungsertrag in MWh: ', sum([d.gravity_energy_storage for d in data]) / len(data) / 1_000_000)
    print('Durchschnittlicher Sonstige-Konventionelle-Leistungsertrag in MWh: ', sum([d.other_conventional for d in data]) / len(data) / 1_000_000)


class Data:
    def __init__(self, values):
        start_date_as_string = values[0] + ' ' + values[1]
        end_date_as_string = values[0] + ' ' + values[2]

        self.start = datetime.strptime(start_date_as_string, '%d.%m.%Y %H:%M')
        self.end = datetime.strptime(end_date_as_string, '%d.%m.%Y %H:%M')
        self.biomass = float(values[3].replace('.', '').replace(',','.')) * 1_000_000
        self.water = float(values[4].replace('.', '').replace(',','.')) * 1_000_000
        self.wind_off = float(values[5].replace('.', '').replace(',','.')) * 1_000_000
        self.wind_on = float(values[6].replace('.', '').replace(',','.')) * 1_000_000
        self.pv = float(values[7].replace('.', '').replace(',','.')) * 1_000_000
        self.other = float(values[8].replace('-', '0').replace('.', '').replace(',','.')) * 1_000_000
        self.nuclear = float(values[9].replace('.', '').replace(',','.')) * 1_000_000
        self.coal = float(values[10].replace('.', '').replace(',','.')) * 1_000_000
        self.stone_coal = float(values[11].replace('.', '').replace(',','.')) * 1_000_000
        self.gas = float(values[12].replace('.', '').replace(',','.')) * 1_000_000
        self.gravity_energy_storage = float(values[13].replace('.', '').replace(',','.')) * 1_000_000
        self.other_conventional = float(values[14].replace('.', '').replace(',','.')) * 1_000_000


        print('Data object created')



if __name__ == '__main__':
    main()
