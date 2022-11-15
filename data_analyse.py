import matplotlib.pyplot as plt
from model import model_annual_headline_consumer_price_index
from helper import *


def analyze_monthly_hcpi_ccpi_epi_fpi_usa():
    print("Headline Consumer Price Index, Official Core Consumer Price Index, Energy Price Index and"
          "  Food Price Index of USA by year Bar Chart")
    df = read_sheet(['hcpi_m', 'ccpi_m', 'ecpi_m', 'fcpi_m'], 'Inflation-data.xlsx')

    hcpi_m = get_country_data(df['hcpi_m'], 'USA')
    ccpi_m = get_country_data(df['ccpi_m'], 'USA')
    ecpi_m = get_country_data(df['ecpi_m'], 'USA')
    fcpi_m = get_country_data(df['fcpi_m'], 'USA')

    hcefcpi_m = concat_indicators([hcpi_m, ccpi_m, ecpi_m, fcpi_m])
    hcefcpi_m = concat_columns(hcefcpi_m, ['Country Code', 'Series Name'], 'CC_SN')

    hcefcpi_m = calculate_annual_rate(hcefcpi_m)

    drop_columns(hcefcpi_m, 197001, 201612)
    drop_columns(hcefcpi_m, 202201, 202202)

    hcefcpi_m = transpose(hcefcpi_m, 'CC_SN', 'Year')

    plt.figure(figsize=(16, 8))
    axis = pd.to_datetime(hcefcpi_m.index.values, format='%Y%m')
    plt.plot(axis, hcefcpi_m['USA Headline Consumer Price Index'], color='black', linewidth=2.5)
    plt.plot(axis, hcefcpi_m['USA Official Core Consumer Price Index'], ':', color='red', linewidth=2.5)
    plt.bar(axis, hcefcpi_m['USA Energy Price Index'], color='blue', width=25.5)
    plt.bar(axis, hcefcpi_m['USA Food Price Index'], color='green', width=25.5)
    plt.xlabel("Year")
    plt.ylabel("USA HCPI, USA Official CPI, USA Energy PI and USA Food PI")
    plt.legend(["USA Headline Consumer Price Index", "USA Official Core Consumer Price Index", "USA Energy Price Index",
                "USA Food Price Index"])
    plt.title("Headline Consumer Price Index, Official Core Consumer Price Index, Energy Price Index and"
              "Food Price Index of USA")

    plt.show()


def analyze_annual_ecpi_ocpi_usa():
    print("Estimated Annual USA Core Consumer Price Inflation vs Official Core Consumer Price Index")
    df = read_sheet(['ccpi_a_e', 'ccpi_a'], 'Inflation-data.xlsx')

    ccpi_a_e = get_country_data(df['ccpi_a_e'], 'USA')
    ccpi_a = get_country_data(df['ccpi_a'], 'USA')

    ccpi_a_e_a = concat_indicators([ccpi_a_e, ccpi_a])
    ccpi_a_e_a = concat_columns(ccpi_a_e_a, ['Country Code', 'Series Name'], 'CC_SN')

    ccpi_a_e_a = calculate_annual_rate(ccpi_a_e_a)

    drop_columns(ccpi_a_e_a, 1970, 2013)
    ccpi_a_e_a = transpose(ccpi_a_e_a, 'CC_SN', 'Year')

    plt.figure(figsize=(16, 8))
    axis = pd.to_datetime(ccpi_a_e_a.index.values, format='%Y')
    plt.plot(axis, ccpi_a_e_a['USA Estimated Core Consumer Price Inflation'], color='black', linewidth=2.5)
    plt.plot(axis, ccpi_a_e_a['USA Official Core Consumer Price Inflation'], ':', color='red', linewidth=2.5)
    plt.xlabel("Year")
    plt.ylabel("Estimated Core Consumer Price Inflation and Official Core Consumer Price Inflation")
    plt.legend(["Estimated Core Consumer Price Inflation", "Official Core Consumer Price Inflation"])
    plt.title("Estimated Core Consumer Price Inflation vs Official Core Consumer Price Inflation")

    plt.show()


def analyze_annual_usa_vs_rest_of_world():
    print("Headline Consumer Price Inflation, USA vs Rest of World(India, China, GBR, Germany) ")
    df = read_sheet(['hcpi_a'], 'Inflation-data.xlsx')

    hcpi_usa = get_country_data(df['hcpi_a'], 'USA')
    hcpi_ind = get_country_data(df['hcpi_a'], 'IND')
    hcpi_mac = get_country_data(df['hcpi_a'], 'MAC')
    hcpi_gbr = get_country_data(df['hcpi_a'], 'GBR')
    hcpi_deu = get_country_data(df['hcpi_a'], 'DEU')

    hcpi_usa_row = concat_indicators([hcpi_usa, hcpi_ind, hcpi_mac, hcpi_gbr, hcpi_deu])
    hcpi_usa_row = concat_columns(hcpi_usa_row, ['Country Code', 'Series Name'], 'CC_SN')

    hcpi_usa_row = calculate_annual_rate(hcpi_usa_row)

    drop_columns(hcpi_usa_row, 1970, 2013)
    hcpi_usa_row = transpose(hcpi_usa_row, 'CC_SN', 'Year')

    plt.figure(figsize=(16, 8))
    axis = pd.to_datetime(hcpi_usa_row.index.values, format='%Y')
    plt.plot(axis, hcpi_usa_row['USA Headline Consumer Price Inflation'], color='blue', linewidth=2.5)
    plt.plot(axis, hcpi_usa_row['IND Headline Consumer Price Inflation'], ':', color='red', linewidth=2.5)
    plt.plot(axis, hcpi_usa_row['MAC Headline Consumer Price Inflation'], color='black', linewidth=2.5)
    plt.plot(axis, hcpi_usa_row['GBR Headline Consumer Price Inflation'], color='green', linewidth=2.5)
    plt.plot(axis, hcpi_usa_row['DEU Headline Consumer Price Inflation'], color='orange', linewidth=2.5)
    plt.xlabel("Year")
    plt.ylabel('Headline Consumer Inflation Rate Annually, USA vs ROW')
    plt.legend(["USA HCPI", "IND HCPI", "MAC HCPI", "GBR HCPI", "DEU HCPI"])
    plt.title('Headline Consumer Price Inflation, USA vs Rest of World(India, China, GBR, Germany)')

    plt.show()


def func(pct, allvalues):
    absolute = int(pct)
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


def analyze_2021_annual_change_indicators_usa():
    print('2021 Annual Inflation Rate Change in HCPI, CCPI, ECPI, FCPI and GDP Deflector')
    df = read_sheet(['hcpi_a', 'ccpi_a', 'ecpi_a', 'fcpi_a', 'def_a'], 'Inflation-data.xlsx')

    hcpi_a = get_country_data(df['hcpi_a'], 'USA')
    ccpi_a = get_country_data(df['ccpi_a'], 'USA')
    ecpi_a = get_country_data(df['ecpi_a'], 'USA')
    fcpi_a = get_country_data(df['fcpi_a'], 'USA')
    def_a = get_country_data(df['def_a'], 'USA')

    hcefcpi_a = concat_indicators([hcpi_a, ccpi_a, ecpi_a, fcpi_a, def_a])
    hcefcpi_a = concat_columns(hcefcpi_a, ['Country Code', 'Series Name'], 'CC_SN')

    hcefcpi_a = calculate_annual_rate(hcefcpi_a)

    drop_columns(hcefcpi_a, 1970, 2020)

    explode = (0.1, 0.0, 0.2, 0.3, 0.0)

    # Creating color parameters
    colors = ("orange", "blue", "brown",
              "grey", "purple")

    # Wedge properties
    wp = {'linewidth': 1, 'edgecolor': "green"}

    data = []
    for val in hcefcpi_a[2021]:
        data.append(val)

    df_label = [f'hcpi_a: {data[0]}', f'ccpi_a: {data[1]}', f'ecpi_a: {data[2]}', f'fcpi_a: {data[3]}',
                f'def_a: {data[4]}']

    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      labels=df_label,
                                      shadow=True,
                                      colors=colors,
                                      startangle=90,
                                      wedgeprops=wp,
                                      textprops=dict(color="magenta"))

    # Adding legend
    ax.legend(wedges, df_label,
              title="Indicators",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("2021 Annual Inflation Rate Change in HCPI, CCPI, ECPI, FCPI and GDP Deflector")

    plt.show()


def model_consumer_price_index():
    df = read_sheet(['hcpi_a'], 'Inflation-data.xlsx')

    hcpi_m = get_country_data(df['hcpi_a'], 'USA')

    hcpi_m = concat_indicators([hcpi_m])
    hcpi_m = concat_columns(hcpi_m, ['Country Code', 'Series Name'], 'CC_SN')

    hcpi_m = calculate_annual_rate(hcpi_m)

    drop_columns(hcpi_m, 1970, 1999)
    hcpi_m = transpose(hcpi_m, 'CC_SN', 'Year')

    model_annual_headline_consumer_price_index(hcpi_m.index.values, hcpi_m['USA Headline Consumer Price Inflation'])


def _exit():
    exit(0)


if __name__ == '__main__':
    indicator_repo = {1: 'Analyze the USA Monthly HCPI vs CPI vs Energy PI vs Food PI',
                      2: 'Analyze the USA Annualy Estimated CPI vs Official CPI',
                      3: 'Analyze the USA vs Rest of World(Leading Nations), Headline Consumer Price Inflation',
                      4: 'Analyze 2021 Annual Change in Various Indicators of the USA',
                      5: 'Model Headline Consumer Price Index',
                      6: 'To Exit the Application'}
    print('Hello Welcome')

    while True:
        print('Inflation Annual Rate Change Analysis with Different Countries')
        for k, value in indicator_repo.items():
            print(f'{k} : {value}')
        user_input = int(input('Choose any one of the above data to view analysis: '))
        func_repo = {1: 'analyze_monthly_hcpi_ccpi_epi_fpi_usa()',
                     2: 'analyze_annual_ecpi_ocpi_usa()',
                     3: 'analyze_annual_usa_vs_rest_of_world()',
                     4: 'analyze_2021_annual_change_indicators_usa()',
                     5: 'model_consumer_price_index()',
                     6: '_exit()'}

        eval(func_repo[user_input])
