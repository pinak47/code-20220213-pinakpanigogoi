
import pandas as pd
import json


class utility_main:

    def read_json(self,jsonfile):
        data_file = open(jsonfile, 'r')
        data = json.load(data_file)
        data_file.close()
        return pd.DataFrame(data)

    
    def write_dataframe(self, dataframe):
        dataframe.to_csv('Final_BMI_Results.csv')


    