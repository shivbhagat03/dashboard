import os
from dotenv import load_dotenv

load_dotenv()


INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
if not INFLUXDB_TOKEN:
    raise ValueError("INFLUXDB_TOKEN environment variable is not set")

INFLUX_CONFIG = {
    'token': INFLUXDB_TOKEN,
    'org': "test",
    'bucket': "newdataset",
    'url': "http://localhost:8086"
}

FIELDS = [
    "T1", "T2", "T3", "T4", "T5",
    "RH_1", "RH_2", "RH_3", "RH_4", "RH_5",
    "T_out", "RH_out", "windspeed", "Visibility"
]
