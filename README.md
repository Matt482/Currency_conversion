Name
# Currency_conversion


Background
Currency conversion is one of the basic operations in the finance field - first step in any data transformation
is normalizing the currency of the data to be processed.

Description

Part 1:
Exchange rate data can be retrieved from the REST API of the European Central Bank.

"https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.GBP.EUR.SP00.A?detail=dataonly"

In the URL above, GBP is the source currency and EUR is the target one. These values can be replaced with
any combination of currency codes (e.g. PLN.EUR).

function get_exchange_rate():
    Function should fetch the exchange rate data from the appropriate URL and convert it to a pandas
    DataFrame, with columns TIME_PERIOD and OBS_VALUE, corresponding to values of
    generic:ObsDimension and generic:ObsValue tags from the XML. OBS_VALUE should be converted to float.

Running get_exchange_rate("GBP") should produce the following:
TIME_PERIOD, OBS_VALUE
1999-01, 0.702913
1999-02, 0.688505

Part 2:
Other data of interest can be be retrieved from the REST API of the European Central Bank, using the URL below:

https://sdwwsrest.ecb.europa.eu/service/data/BP6/M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N?detail=dataonly

In the URL above, M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N is the data identifier and can be
replaced with any user-specified identifier.

function def get_raw_data():
    Function should fetch the data from the appropriate URL and convert it to a pandas DataFrame. Format of
    the response XML, as well as the format of the resulting pandas DataFrame is same as in the part #1.

Running get_raw_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N"): 
TIME_PERIOD, OBS_VALUE
1999-01, 1427.666667
1999-02, 379.666667

Part 3:
Final part is combined from both first and second parts above

function get_data(identifier: str, target_currency: Optional[str] = None)
    If the target_currency parameter is None, leave the resulting DataFrame as-is.
    If the target_currency parameter is not None, convert the data from the source currency to the target
    one, defined by the target_currency parameter. Exchange rates for the currency conversion should be
    retrieved using the function described in part #1.
    
Running get_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N", "GBP")
TIME_PERIOD, OBS_VALUE
1999-01, 1003.52546
1999-02, 261.402399










