CREATE TABLE
  IF NOT EXISTS moex (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(5),
    per VARCHAR(1),
    date INT,
    time INT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    vol BIGINT
  );
