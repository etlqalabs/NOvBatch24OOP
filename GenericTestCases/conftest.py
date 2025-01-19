import pytest
import pandas as pd
from sqlalchemy import create_engine
@pytest.fixture()
def source_dataSetup():
    df_src = pd.read_csv('data/emp_src.csv')
    print("This is before test execution  - source file reading")
    yield df_src
    print("This is after test execution - source file reading")

@pytest.fixture()
def source_json_dataSetup():
    df_src = pd.read_json('data/emp_src.json')
    print("This is before test execution  - source file reading")
    yield df_src
    print("This is after test execution - source file reading")


@pytest.fixture()
def target_dataSetup():
    df_tgt = pd.read_csv('data/emp_tgt.csv')
    print("This is before test execution - Target file reading")
    yield df_tgt
    print("This is after test execution  - Target file reading")

@pytest.fixture()
def connect_to_oracle():
    engine = create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe")
    connection_oracle = engine.connect()
    yield connection_oracle
    connection_oracle.close()


@pytest.fixture()
def connect_to_mysql():
    engine = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/etlautomation")
    connection_mysql = engine.connect()
    yield connection_mysql
    connection_mysql.close()
