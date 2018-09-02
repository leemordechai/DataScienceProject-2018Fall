import pandas as pd
import io
import ast

# if on Google Colab
from google.colab import files
uploaded = files.upload()
df_org = pd.read_csv(io.StringIO(uploaded['second_dataset.csv'].decode('utf-8')))

# if not on Google Colab, comment the previous 3 lines and just do:
# df_org = pd.read_csv('second_dataset.csv')

split_field = df_org['spacegroup'].apply(lambda x: ast.literal_eval(x))

addon = pd.DataFrame(split_field.values.tolist(), index=split_field.index)

rev_df = df_org.drop(columns=['spacegroup'])
df = pd.concat([rev_df, addon], axis=1)

df.head()

