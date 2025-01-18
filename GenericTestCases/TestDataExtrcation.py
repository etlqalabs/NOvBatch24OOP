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

@pytest.fixture()
def source_dataSetup():
    df_src = pd.read_csv('data/emp_src.csv')
    print("This is before test execution  - source file reading")
    yield df_src
    print("This is after test execution - source file reading")

@pytest.fixture()
def target_dataSetup():
    df_tgt = pd.read_csv('data/emp_tgt.csv')
    print("This is before test execution - Target file reading")
    yield df_tgt
    print("This is after test execution  - Target file reading")

#1. comparae the data in src and tgt using pytest
def test_compare_employees_data_usingPytest_test1(source_dataSetup,target_dataSetup):
    print("Test strated ....")
    df_src = source_dataSetup
    df_tgt = target_dataSetup
    assert df_src.equals(df_tgt),"The data in src and tgt does not match"
    print("Test  completed ....")

'''
#1. comparae the data in src and tgt using pytest
def test_compare_employees_data_usingPytest_test2(source_dataSetup,target_dataSetup):
    print("Test strated ....")
    df_src = source_dataSetup
    df_tgt = target_dataSetup
    assert df_src.equals(df_tgt),"The data in src and tgt does not match"
    print("Test  completed ....")

#1. comparae the data in src and tgt using pytest
def test_compare_employees_data_usingPytest_test3(source_dataSetup,target_dataSetup):
    print("Test strated ....")
    df_src = source_dataSetup
    df_tgt = target_dataSetup
    assert df_src.equals(df_tgt),"The data in src and tgt does not match"
    print("Test  completed ....")
'''

