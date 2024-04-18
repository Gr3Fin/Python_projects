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


def bed_list():
    df_filter = df["info"].str.contains('Łóżko|Łóżeczko', case=False, regex=True)
    return df[df_filter]


