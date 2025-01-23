from time import time
import os
from sqlalchemy import create_engine
import pyarrow.parquet as pq

def get_data(filename):
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/' + filename + '.parquet'
    output_file = '/app/data/' + filename + '.parquet'
    os.system(f'wget {url} -O {output_file}')
    return pq.ParquetFile('/app/data/' + filename + '.parquet')

def get_engine(user, password, db):
    return create_engine(f'postgresql://{user}:{password}@postgres:5432/{db}')

def process_taxi_data_batches(pf, table_name, engine, batch_size=100000):
    total_time = 0
    total_data = 0
    for i, batch in enumerate(pf.iter_batches(batch_size=100000)):
        start = time()
        batch.to_pandas().to_sql(table_name, engine, if_exists='append')
        end = time() - start
        print(f'Batch: {i}. Elapsed time: {end:.2f} sec')
        total_time += end
        total_data += len(batch)
    print(f'Total time: {total_time:.2f} sec. Total data: {total_data}')

if __name__ == '__main__':
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    db = os.getenv('POSTGRES_DB')
    table = os.getenv('TABLE')
    filename = os.getenv('FILENAME')

    engine = get_engine(user, password, db)
    pf = get_data(filename)
    process_taxi_data_batches(pf, table, engine)