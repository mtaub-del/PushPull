import pandas as pd
portfolio = {
    "Aktie": ["BMW", "SAP", "Siemens"],
    "Kaufkurs": [90.0, 150.0, 170.0],
    "Aktueller_Kurs": [105.0, 180.0, 165.0]
}
df_port= pd.DataFrame(portfolio)
df_port["Gewinn_Prozent"] = ((df_port["Aktueller_Kurs"] - df_port["Kaufkurs"]) / df_port["Kaufkurs"])*100

df_port["Gewinner"] = df_port["Gewinn_Prozent"] > 0 

gewinner_namen = df_port.loc[df_port["Gewinn_Prozent"] > 0, "Aktie"]
print(gewinner_namen)

gesamtkauf = df_port["Kaufkurs"].sum()
durchschnittsgewinn = df_port["Gewinn_Prozent"].mean()
max_gewinn = df_port["Gewinn_Prozent"].max()

print(gesamtkauf, durchschnittsgewinn, max_gewinn)
print(df_port["Gewinn_Prozent"])