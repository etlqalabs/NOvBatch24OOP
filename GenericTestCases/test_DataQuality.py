import pandas as pd
import pytest

@pytest.mark.skip
#1. data types check
def test_dataTypes(connect_to_mysql):
    print("Test started ....")
    query_tgt = """select * from city"""
    df_actual = pd.read_sql(query_tgt,connect_to_mysql)
    actual_dataypes = df_actual.dtypes.to_dict()
    print("Actual datatypes:", actual_dataypes)
    expected_datypes = {'id':'int64','name':'object','country':'object'}
    print("expected datatypes:" ,expected_datypes)
    assert actual_dataypes == expected_datypes,"Actual and expected datypes doesn't match"

    # 2. Foreign key/referential integrity check/
    # source vs target where target has less rows than source ( src : 100 , tgt : 10 )
@pytest.mark.smoke
@pytest.mark.regression
def test_ReferentialIntegrity_src_oracle_and_tgt_mysql(connect_to_oracle, connect_to_mysql):
    print("Test strated ....")
    query_src = """select id,name from city order by id"""
    query_tgt = """select id,name from city order by id"""
    df_src = pd.read_sql(query_src, connect_to_oracle)
    df_tgt = pd.read_sql(query_tgt, connect_to_mysql)
    df_missing_records = df_src[~df_src['id'].isin(df_tgt['id'])]
    df_missing_records.to_csv("TestResults/missingRecords.csv",index=False)
    assert df_missing_records.empty, "There are extra records in source - Please check the details of missing" \
                                     "records in test result folder"
    print("Test  completed ....")
@pytest.mark.smoke
#3. duplicate records check
def test_duplicateCheck(connect_to_mysql):
    print("Test started ....")
    query = """select * from city_duplicate"""
    df = pd.read_sql(query, connect_to_mysql)
    df_duplicateRows = df[df.duplicated()]
    df_duplicateRows.to_csv("TestResults/duplicates.csv",index=False)
    assert df.duplicated().sum() == 0, "There are duplicate rows -check TestResult folder for details"

@pytest.mark.regression
def test_row_count(connect_to_oracle, connect_to_mysql):
    print("Test strated ....")
    query_src = """select count(*) from city """
    query_tgt = """select count(*) from city """
    src_rowcount = pd.read_sql(query_src, connect_to_oracle).iloc[0,0]
    tgt_rowcount = pd.read_sql(query_tgt, connect_to_mysql).iloc[0,0]
    assert src_rowcount == tgt_rowcount ,"Row count does not match"
