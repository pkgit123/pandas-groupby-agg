import pandas as pd

# create sample data using dictionary
di_sample = {'UnderlyingSymbol': {0: 'FXA', 1: 'FXY', 2: 'FXA', 3: 'FXY', 4: 'FXY'},
 'UnderlyingPrice': {0: 72.4399, 1: 88.73, 2: 72.4399, 3: 88.73, 4: 88.73},
 'Type': {0: 'call', 1: 'call', 2: 'call', 3: 'put', 4: 'put'},
 'Expiration': {0: '10/16/2020',
  1: '09/11/2020',
  2: '09/18/2020',
  3: '12/18/2020',
  4: '09/18/2020'},
 ' DataDate': {0: '08/27/2020 16:00',
  1: '08/27/2020 16:00',
  2: '08/27/2020 16:00',
  3: '08/27/2020 16:00',
  4: '08/27/2020 16:00'},
 'Strike': {0: 55.0, 1: 87.5, 2: 74.0, 3: 96.0, 4: 125.0},
 'Last': {0: 0.0, 1: 0.0, 2: 0.2, 3: 0.0, 4: 0.0},
 'Bid': {0: 15.1, 1: 1.2, 2: 0.15, 3: 7.4, 4: 33.9},
 'Ask': {0: 19.8, 1: 4.8, 2: 0.2, 3: 7.7, 4: 38.5},
 'OpenInterest': {0: 0, 1: 0, 2: 193, 3: 0, 4: 0}}

# create sample dataframe
df_sample = pd.DataFrame(di_sample)

print("Here is the dataframe sample.")
print(df_sample)
print()

# create groupby-agg dataframe, flatten the multi-index-columns
df_gb_agg = pd.DataFrame(df_sample.groupby('UnderlyingSymbol').agg({
    'Strike': [len, pd.Series.nunique]
}).to_records())
df_gb_agg.columns = [x.replace(', ', '_').replace('(', '').replace(')', '').replace("'", "") for x in df_gb_agg.columns]

print("Here is the groupby-agg sample.")
print(df_gb_agg)
print()
