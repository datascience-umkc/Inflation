import pandas as pd


def read_sheet(sheet_name_lst, data_sheet_name):
    """
    @
    :param sheet_name_lst: List of sheets to read
    :param data_sheet_name: Excel data sheet name
    :return: A dictionary which contains the key value pairs of sheet name and their data.
    """
    try:
        excel_file = pd.ExcelFile(data_sheet_name)
        data_frame = {}
        for each_sheet in sheet_name_lst:
            data_frame[each_sheet] = pd.read_excel(excel_file, sheet_name=each_sheet)
        return data_frame
    except FileNotFoundError:
        print(f'Excel file not found: {FileNotFoundError}')
        exit(0)


def get_country_data(indicator_df, country_code):
    """
    :param indicator_df: Data frame which hold the relevant indicator.
    :param country_code: Country code.
    :return: Return a df which holds the values of the received country code.
    """
    return indicator_df.loc[indicator_df['Country Code'] == country_code]


def concat_indicators(indicators_df_lst):
    """
    @
    :param indicators_df_lst: List of indicators to concat.
    :return: Concatenated indicator list.
    """
    return pd.concat(indicators_df_lst)


def concat_columns(indicator_df, columns_to_concat, new_column_name, loc=0, remove_column=True):
    """
    :param indicator_df: Data frame in which columns to be concatenated
    :param columns_to_concat: List of columns to concat
    :param new_column_name: Name given to concatenated columns
    :param loc: Loc to place newly created column
    :param remove_column: Removes concatenated columns, Default set to True
    :return: Resulting df
    """
    df = indicator_df[f'{columns_to_concat[0]}'].str.cat(indicator_df[f'{columns_to_concat[1]}'], sep=' ')
    indicator_df.insert(loc=loc, column=new_column_name, value=df)
    if remove_column:
        indicator_df.drop(indicator_df.loc[:, columns_to_concat[0]: columns_to_concat[1]], axis=1, inplace=True)
    indicator_df.fillna(0, inplace=True)
    return indicator_df


def calculate_annual_rate(indicator_df):
    """
    :param indicator_df: Df on which math operation to perform
    :return: Resulting df
    """
    transform_df = {}
    for col in indicator_df.columns:
        if isinstance(col, (int, float)):
            if col in range(0, 197101):
                continue
            try:
                transform_df[col] = indicator_df.apply(lambda x: ((x[col] - x[col - 100]) / x[col - 100]) * 100, axis=1)
            except ZeroDivisionError:
                pass

    for col_df in transform_df.keys():
        indicator_df[col_df] = transform_df[col_df]

    return indicator_df


def transpose(indicator_df, index_value, index_name):
    """
    :param indicator_df: Df on which transpose to apply
    :param index_value: Index value
    :param index_name: Index name
    :return: Return resulting data frame
    """
    indicator_df.set_index(index_value, inplace=True)
    indicator_df = indicator_df.transpose()
    indicator_df.index.name = index_name
    return indicator_df


def unpivot_df(indicator_df):
    raise NotImplementedError
    # Un pivout
    # hcpiCcpiDf = pd.melt(hcpiCcpiDf, id_vars=['CC_SN'], var_name='year', value_name='value')


def pivot_df(indicator_df):
    raise NotImplementedError
    # Pivot
    # hcpiCcpiDf = hcpiCcpiDf.pivot(index=['year'], columns=['CC_SN'], values='value')


def drop_columns(indicator_df, from_value, to_value):
    """
    :param indicator_df: Data frame on which column to drop
    :param from_value: From column value
    :param to_value: To column value
    :return: Resulting df
    """
    indicator_df.drop(indicator_df.loc[:, from_value:to_value], axis=1, inplace=True)