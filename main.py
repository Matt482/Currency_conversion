import pandas as pd
from typing import Optional

from helpers import get_exchange_rate_url, create_df,get_data_identifier_url


def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    """
    From input get exchange rate url
    Args:
        source: exporting currency value - source
        target: default EUR inporting currency value
    Returns: df with TIME_PERIOD and OBS_VALUE cols
            TIME_PERIOD rows format YYYY-MM
    """
    exchange_url = get_exchange_rate_url(source, target)
    my_df = create_df(exchange_url)

    return my_df


def get_raw_data(identifier: str) -> pd.DataFrame:
    """
    identifier: data identifier and can be replaced
                with any user-specified identifier
    Returns: df with TIME_PERIOD and OBS_VALUE cols
            TIME_PERIOD rows format YYYY-MM
    """
    identifier_url = get_data_identifier_url(identifier)
    my_df = create_df(identifier_url)
    return my_df


def get_data(identifier: str,
             target_currency: Optional[str] = None
             ) -> pd.DataFrame:
    """
    target_currency: currency taken from get_exchange_rate func
    Returns: if target_currency == None return df from
            get_raw_data() func above
            if target_currency != None
            column "OBS_VALUE" from get_raw_data func concat
            with another column from get_exchange_rate func
    """
    new_data = get_raw_data(identifier)

    if target_currency == None:
        return new_data

    else:
        moj_rate = get_exchange_rate(target_currency)
        multiply_series = moj_rate['OBS_VALUE'] * new_data['OBS_VALUE']

        frame = {'TIME_PERIOD': new_data['TIME_PERIOD'], 'OBS_VALUE': multiply_series}
        result = pd.DataFrame(frame).dropna()
        # result.to_csv('result.csv', sep=',', index=False)  # -> uncomment to export

        return result


# print(get_exchange_rate('PLN'))
# print(get_raw_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N"))
# print(get_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N", "GBP"))
