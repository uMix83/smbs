CREATE SEQUENCE smbs_seq START 10 INCREMENT BY 10;

CREATE TABLE
  IF NOT EXISTS moex (
    id INT DEFAULT nextval ('smbs_seq') PRIMARY KEY,
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
