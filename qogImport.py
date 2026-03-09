import pandas as pd


# Useful variables and names from Quality of Government Codebook
variablesMap = {
    "ccode": "Country Code",
    "cname": "Country Name",
    "year": "Year",
    "wdi_gdpgr": "GDP growth (annual %)",
    "mad_gdppc": "Real GDP per Capita",
    "undp_hdi": "Human Development Index",
    "wbgi_cce": "Control of Corruption, Estimate",
    "wbgi_gee": "Government Effectiveness, Estimate",
    "ti_cpi": "Corruption Perceptions Index",
    "wdi_litrad": "Literacy rate, adult total",
    "pwt_hci": "Human Capital Index",
    "gggi_ggi": "Overall Global Gender Gap Index",
    "ciri_wopol": "Women's Political Rights",
    "wdi_wip": "Proportion of seats held by women in national parliaments (%)",
    "cspf_sfi": "State Fragility Index",
    "ht_colonial": "Colonial Origin",
    "ht_regtype": "Regime Type",
    "ajr_settmort": "Log Settler Mortality",
    "ht_regtype1": "Regime Type (simplified)",
    "bci_bci": "The Bayesian Corruption Indicator",
    "bci_bcistd": "Standard Deviation of BCI",
    "vdem_excrptps": "Public sector corrupt exchanges",
    "wdi_pop": "Population, total",
    "vdem_jucorrdc": "Judicial corruption decision",
    "wdi_unempedua": "Unemployment with advanced education",
    "wdi_lifexp": "Life expectancy at birth, total (years)",
    "wdi_co2": "CO2 emissions (metric tons per capita)",
    "fh_cl": "Civil Liberties"
}

# Returns a sub dataframe with only the wanted columns
def briefQOG(path="qog_std_ts_jan26.csv"):

    df = pd.read_csv(path, usecols=variablesMap.keys(), header=0)

    return df


# Testing
if __name__ == "__main__":
    df = briefQOG()
    print("Great Success")
    print(df.head())
