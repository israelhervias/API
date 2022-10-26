import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json


user = "ihhmoney"
passw = "loco123123"
host = "ihhmoney.mysql.pythonanywhere-services.com"
database = "ihhmoney$foodb"

db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
conn = db.connect()

#tables = conn.execute(
    #"SHOW DATABASES;"
#)

#for table in tables.fetchall():
    #print(table)



#url = 'https://drive.google.com/file/d/1aV2wVXbXRjUSWouCDIbzVyzyFbe4DreU/view?usp=sharing'
#path = 'https://drive.google.com/uc?export=download&id=' + url.split('/')[-2]
#food_df = pd.read_csv(path)

#cols = ["id", "name", "food_group", "food_subgroup"]
#print("FOOD DATAFRAME")
#print(food_df[cols].head())
#print("")

#food_df.to_sql('food', db)

rows = conn.execute(
"""
    SELECT
        id,
        name,
        name_scientific
    FROM food LIMIT 10;
""")

for row in rows.fetchall():
    print(row)


#url = 'https://drive.google.com/file/d/1t0kpGGWj53DFAiojLTUQd0juiH7NetYW/view?usp=sharing'
#path = 'https://drive.google.com/uc?export=download&id=' + url.split('/')[-2]
#enzime_df = pd.read_csv(path)

#enzime_df.to_sql('enzime', db)


conn.close()


