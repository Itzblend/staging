import json
import os
from typing import Dict


def set_db_config(env: str) -> Dict:
    """Set configuration for the app."""
    dbconfig = {
        'host': os.environ.get('DB_HOST', 'localhost'),
        'port': os.environ.get('DB_PORT', 5434),
        'user': os.environ.get('DB_USER', 'postgres'),
        'password': os.environ.get('DB_PASSWORD', 'password'),
        'database': os.environ.get('DB_NAME', f'brooklyn_{env}')
    }

    return dbconfig


#https://data.ouka.fi/data/fi/dataset/oulun-kaupungin-terveysasemien-ja-hyvinvointikeskusten-kiireettomien-aikojen-jonotilanne
#https://api.ouka.fi/v1/chc_waiting_times_monthly_stats?order=year.desc,month.desc