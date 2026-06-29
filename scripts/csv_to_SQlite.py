import os
import re
import sqlite3

import pandas as pd

os.makedirs("database", exist_ok=True)


def clean_column(column):

    column = column.lower().strip()

    column = re.sub(r"[()]", "", column)

    column = column.replace("/", "_")

    column = column.replace("-", "_")

    column = column.replace(" ", "_")

    column = re.sub(r"__+", "_", column)

    return column


def csv_to_sqlite(csv_file, db_name, table_name):

    print(f"\nProcessing {csv_file}")

    df = pd.read_csv(csv_file)

    df.columns = [clean_column(c) for c in df.columns]

    df = df.fillna("")

    db_path = f"database/{db_name}"

    conn = sqlite3.connect(db_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print(f"✅ Created {db_name}")

    print(f"Rows : {len(df)}")

    print(df.columns.tolist())


csv_to_sqlite(
    "data\hospitals.csv",
    "hospitals.db",
    "hospitals"
)

csv_to_sqlite(
    "data\institutions.csv",
    "institutions.db",
    "institutions"
)

csv_to_sqlite(
    "data\Restaurants.csv",
    "restaurants.db",
    "restaurants"
)

print("\n✅ All databases created successfully")