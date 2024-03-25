import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_worldbank_data(filename):
    """
    This function reads World Bank data, cleans it, and returns dataframes 
    with years as columns and countries as columns.
    """
    #skip unneccesary data
    data = pd.read_csv(filename, skiprows=4)
    data.set_index("Country Name", inplace=True)
    #Transpose the Data
    data_years = data.T
    #set meaningful header
    data_years.columns.name = "Country Name"
    return data_years, data
#Call the co2 dataframe
co2_dataframe_years, co2_dataframe_countries = clean_worldbank_data("co2.csv")
#Call the indicators
gdp_dataframe_years, gdp_dataframe_countries = clean_worldbank_data("GDP.csv") #Gdp per capita
forest_dataframe_years, forest_dataframe_countries = clean_worldbank_data("FRST.csv") #Forest Area in KM
urban_dataframe_years,urban_dataframe_countries = clean_worldbank_data("UrbanPop.csv") #Urban Population per country
agr_dataframe_years,agr_dataframe_countries = clean_worldbank_data("Ag-land.csv") #agricultural land per country in km
print(agr_dataframe_years)
