import psycopg
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время загрузки составило {end_time - start_time} секунд.')
        return result
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        print(f'В таблицу, загружается файл {args[0]}')
        result = func(*args, **kwargs)
        print(f'{result} строк загружено')
        return result
    return wrapper


@benchmark
@logger
def insert_from_csv(filename, sql):
    with (
        psycopg.connect(dbname='smbs', user='user', password='12345', host='localhost', port='5432') as connection,
        open(filename, 'r') as file
    ):
        with connection.cursor().copy(sql) as copy:
            next(file)
            count = 0
            for line in file:
                copy.write(line)
                count += 1
            return count


insert_data_sql = 'COPY moex(ticker, per, date, time, open, high, low, close, vol) FROM STDIN (format csv, delimiter ";")'
filename = 'IMOEX_230101_240601.csv'

try:
    insert_from_csv(filename, insert_data_sql)
except Exception as e:
    print(f'Ошибка: {str(e)}')
