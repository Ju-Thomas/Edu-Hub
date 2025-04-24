import pandas as pd
import scipy.stats as stats


df = pd.read_csv("./data.txt", sep=",")

# Konvertiere die Datum-Spalte in ein Datetime-Format
df["Datum"] = pd.to_datetime(df["Datum"], format="%Y-%m-%d")


# average temperature gesamnt berechnen
average_temperature = df["Temperatur"].mean()
print(f"Durchschnittle komplette Temperatur ist: {average_temperature:.2f}")


# Filtere die Daten für den Monat Juli
july_data = df[df["Datum"].dt.month == 7]
july_temperatures = july_data["Temperatur"].dropna()


# Filtere die Daten für den Monat Mai
mai_data = df[df["Datum"].dt.month == 5]
mai_temperatures = mai_data["Temperatur"].dropna()


# Berechne die durchschnittliche Temperatur für den Monat Juli
average_temperature_july = july_data["Temperatur"].mean()
print(f"Durchschnittliche Temperatur im Juli: {average_temperature_july:.2f}\n")

# Berechne die durchschnittliche Temperatur für den Monat Mai
average_temperature_mai = mai_data["Temperatur"].mean()
print(f"Durchschnittliche Temperatur im Mai: {average_temperature_mai:.2f}\n")

# Vergleiche die durchschnittlichen Temperaturen von Juli und Mai
if average_temperature_july > average_temperature_mai:
    print(
        f"Die durchschnittliche Temperatur im Juli ist höher als im Mai. {average_temperature_july:.2f} > {average_temperature_mai:.2f}\n"
    )
else:
    print(
        f"Die durchschnittliche Temperatur im Mai ist höher als im Juli. {average_temperature_mai:.2f} > {average_temperature_july:.2f}\n"
    )

# Berechnung der descriptiven Statistik für Juli und Mai
july_descriptive = july_data["Temperatur"].describe()
mai_descriptive = mai_data["Temperatur"].describe()
print(f"Deskriptive Statistik für Juli:\n{july_descriptive}\n")
print(f"Deskriptive Statistik für Mai:\n{mai_descriptive}\n")


t_stat, p_value = stats.ttest_ind(july_temperatures, mai_temperatures)
print(f"T-Statistik: {t_stat:.2f}, p-Wert: {p_value}")

if p_value < 0.05:
    print(
        f"Die Unterschiede zwischen den Temperaturen im Juli und Mai sind signifikant, p-Wert: {p_value}.\n"
    )
else:
    print(
        "Die Unterschiede zwischen den Temperaturen im Juli und Mai sind nicht signifikant.\n"
    )
