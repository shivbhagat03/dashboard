import pandas as pd
from influxdb_client import InfluxDBClient
from config import INFLUX_CONFIG

def fetch_data(field, start_time=None, end_time=None):
   
    if start_time and not start_time.endswith("Z"):
        start_time += "Z"
    if end_time and not end_time.endswith("Z"):
        end_time += "Z"

    query = f'''
    from(bucket: "{INFLUX_CONFIG['bucket']}")
    |> range(start: {start_time}, stop: {end_time})
    |> filter(fn: (r) => r._field == "{field}")
    '''

    try:
        client = InfluxDBClient(
            url=INFLUX_CONFIG['url'], 
            token=INFLUX_CONFIG['token'], 
            org=INFLUX_CONFIG['org']
        )
        tables = client.query_api().query(query, org=INFLUX_CONFIG['org'])
    except Exception as e:
        print(f"Error querying InfluxDB: {e}")
        return pd.DataFrame()

    data = []
    for table in tables:
        for record in table.records:
            data.append({'time': record.get_time(), field: record.get_value()})
    return pd.DataFrame(data)
