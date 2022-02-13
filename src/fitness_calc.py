
import pandas as pd
import json

import utility as util

class fitness_calculation:
    dataframe= pd.DataFrame()
    dataframe_category= pd.DataFrame()


    def BMI_calc(self, jsonfile):
        dataframe = util.utility_main().read_json(jsonfile)
        dataframe["BMI"]= dataframe.apply(lambda x: (x.WeightKg/(x.HeightCm/100)**2), axis=1).round(2)
        fitness_calculation.dataframe = dataframe
        return dataframe

    def category_seg(self, jsonfile):
        dataframe_category = fitness_calculation.dataframe
        if dataframe_category.empty:
            dataframe_category = fitness_calculation.BMI_calc(self, jsonfile)
            fitness_calculation.dataframe_category = dataframe_category
        for i, row in dataframe_category.iterrows():    
            if dataframe_category.loc[i,'BMI'] <= 18.4:
                dataframe_category.loc[i,'BMI_Category'] = 'UnderWeight'
                dataframe_category.loc[i,'Health_Risk'] = 'Malnutrition Risk'

            elif dataframe_category.loc[i,'BMI'] > 18.4 and dataframe_category.loc[i,'BMI'] < 24.9:
                dataframe_category.loc[i,'BMI_Category'] = 'Normal Weight'
                dataframe_category.loc[i,'Health_Risk'] = 'Low Risk'
            
            elif dataframe_category.loc[i,'BMI'] > 25 and dataframe_category.loc[i,'BMI'] < 29.9:
                dataframe_category.loc[i,'BMI_Category'] = 'OverWeight'
                dataframe_category.loc[i,'Health_Risk'] = 'Enhanced Risk'
            
            elif dataframe_category.loc[i,'BMI'] > 30 and dataframe_category.loc[i,'BMI'] < 34.9:
                dataframe_category.loc[i,'BMI_Category'] = 'Moderately Obese'
                dataframe_category.loc[i,'Health_Risk'] = 'Medium Risk'
            
            elif dataframe_category.loc[i,'BMI'] > 35 and dataframe_category.loc[i,'BMI'] < 39.9:
                dataframe_category.loc[i,'BMI_Category'] = 'Severely Obese'
                dataframe_category.loc[i,'Health_Risk'] = 'High Risk'
            
            elif dataframe_category.loc[i,'BMI'] > 40:
                dataframe_category.loc[i,'BMI_Category'] = 'Very Severely Obese'
                dataframe_category.loc[i,'Health_Risk'] = 'Very High Risk'
        util.utility_main().write_dataframe(dataframe_category)
        return dataframe_category


    def Total_overweight_count(self, jsonfile):
        df = fitness_calculation.dataframe_category
        if df.empty:
            df = fitness_calculation.category_seg(self, jsonfile)
        count=len(df[df.BMI_Category=="OverWeight"])
        return count
     