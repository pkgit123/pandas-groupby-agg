import pandas as pd

def gb_agg_df(df, gb_key, di_gb_agg):
    '''
    Run .groupby().agg() based on key and a dictionary of aggregations.
    
    Inputs:
        df - dataframe, input
        gb_key - str, dataframe column as groupby key
        di_gb_agg - dict, keys are columns to aggregate, values are list of aggregation functions
    
    Example di_gb_agg:
    {
        'col1', [length, np.sum]
    }
    
    Cleanup columns:
     * Replace ', '  =>  '_'
     * Remove '('
     * Remove ')'
     * Remove ','
    '''
    
    # step 1: create raw .groupby().agg() dataframe ... problem is multi-index columns
    df_raw_gb_agg = df.groupby(gb_key).agg(di_gb_agg)
    
    # step 2: convert to numpy records ... flatten columns
    np_rec_gb_agg = df_raw_gb_agg.to_records()
    
    # step 3: convert numpy records to dataframe
    df_flatten_gb_agg = pd.DataFrame(np_rec_gb_agg)
    
    # step 4: save original column names to list
    ls_original_cols = df_flatten_gb_agg.columns
    
    # step 5: cleanup column names
    ls_cleanup_cols = [x.replace(', ', '_').replace('(', '').replace(')', '').replace("'", "") for x in ls_original_cols]
    
    # step 6: return new dataframe with clean column names
    df_clean_gb_agg = df_flatten_gb_agg.copy()
    df_clean_gb_agg.columns = ls_cleanup_cols
    
    return df_clean_gb_agg


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

# step 1: create groupby-agg dataframe
df_gb_agg_raw = df_sample.groupby('UnderlyingSymbol').agg({
    'Strike': [len, pd.Series.nunique]
})

# step 2: flatten multi-index-columns into numpy record array
np_flatten = df_gb_agg_raw.to_records()

# step 3: convert numpy record array back to dataframe
df_flatten_rawcols = pd.DataFrame(np_flatten)

# step 4: clean column names
df_gb_agg_clean = df_flatten_rawcols.copy()
df_gb_agg_clean.columns = [x.replace(', ', '_').replace('(', '').replace(')', '').replace("'", "") for x in df_flatten_rawcols.columns]

print("Here is the clean groupby-agg sample.")
print(df_gb_agg_clean)
print()

# create example of di_gb_agg
di_gb_agg_example = {
    'Strike': [len, pd.Series.nunique]
}

# create gb_agg
df_gb_agg_version2 = gb_agg_df(df_sample, 'UnderlyingSymbol', di_gb_agg_example)

print("Here is the version2 sample.")
print(df_gb_agg_version2)
print()
