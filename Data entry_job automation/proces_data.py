# --- Clear the scraped data ---

import pandas as pd
from data import Data

data_set = Data().find_data()

data_dict = {
    "info": data_set[0],
    "price": data_set[1],
    "url": data_set[2]
}

df = pd.DataFrame(data_dict)
pd.set_option('display.max_columns', None)


def bike_list():
    df_filter = df["price"].str.split("zł", n=1, expand=True)
    df["price"] = df_filter[0].astype(int)
    df.insert(2, "others", df_filter[1])
    df_filter = df["info"].str.contains('rowerek|rower|rowerki', case=False, regex=True)
    df_filter = df[df_filter].drop_duplicates(subset=["info"])
    df_filter = df_filter.sort_values(by=["price"], ascending=True)
    return df_filter
