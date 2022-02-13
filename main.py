import pandas as pd
from src import fitness_calc as fitness

class main:
    if __name__ == "__main__":
        ft_cal = fitness.fitness_calculation()
        df_bmi = ft_cal.BMI_calc("person_detail.json")
        print("\n Printing out the person details with BMI :: \n\n\n ", df_bmi)
        df_cat = ft_cal.category_seg("person_detail.json")
        print("\n Printing out the person details with BMI and categories :: \n\n ", df_cat)
        print("\n Total number of overweight people is :: ", ft_cal.Total_overweight_count("person_detail.json"))