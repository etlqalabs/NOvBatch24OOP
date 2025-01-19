import pandas as pd
import pytest
'''
## 1. compare src and tgt data using python if...else...
def compare_employees_data():
    df_src = pd.read_csv('data/emp_src.csv')
    df_tgt = pd.read_csv('data/emp_tgt.csv')
    #print(df_src)
    #print(df_tgt)
    if(df_src.equals(df_tgt)):
        print("pass")
    else:
        print("fail")

#compare_employees_data()
'''




# method to spot the diffreence in src and target and write the diffrences ina csv file
def get_differences(df_src,df_tgt,file_path):
    df_merged = pd.concat([df_src,df_tgt])
    df_diff = df_merged.drop_duplicates(keep=False)
    if not df_diff.empty:
        df_diff.to_csv(file_path,index=False)
    return df_diff





@pytest.mark.skip
#1. comparae the data in src as csv and tgt as csv using pytest
def test_compare_src_csv_and_tgt_csv(source_dataSetup,target_dataSetup):
    print("Test strated ....")
    df_src = source_dataSetup
    df_tgt = target_dataSetup
    assert df_src.equals(df_tgt),"The data in src and tgt does not match"
    print("Test  completed ....")

@pytest.mark.skip
#2. comparae the data in src as json and tgt as csv using pytest
def test_compare_src_json_and_tgt_csv(source_json_dataSetup,target_dataSetup):
    print("Test strated ....")
    df_src = source_json_dataSetup
    df_tgt = target_dataSetup
    assert df_src.equals(df_tgt),"The data in src and tgt does not match"
    print("Test  completed ....")

#3. comparae the data in oracle as source and mysql as target using pytest
def test_compare_src_oracle_and_tgt_mysql(connect_to_oracle,connect_to_mysql):
    print("Test strated ....")
    query_src = """select id,name from city order by id"""
    query_tgt = """select id,name from city order by id"""
    df_src = pd.read_sql(query_src,connect_to_oracle)
    df_tgt = pd.read_sql(query_tgt,connect_to_mysql)
    df_differences = get_differences(df_src,df_tgt,"TestResults/diff_orcl_mysql.csv")
    assert df_src.equals(df_tgt),"The data in src and tgt does not match"
    print("Test  completed ....")

