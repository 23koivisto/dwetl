# from dwetl import dw_etl
import data_quality_utilities
# import data_quality_specific_functions
'''
dataquality tests
'''

# test if right exceptions are thrown when given bad data

def test_is_numeric():
    assert data_quality_utilities.is_numeric(5634563) == True
    assert dwetl.data_quality_utilities.is_numeric("a") == False

def test_is_valid_length():
    assert dwetl.data_quality_utilities.is_valid_length("teststring", 10) == True
    assert dwetl.data_quality_utilities.is_valid_length("teststring", 3) == False
    assert dwetl.data_quality_utilities.is_valid_length(1234, 4) == True
    assert dwetl.data_quality_utilities.is_valid_length("123.2", 5) == True
    assert dwetl.data_quality_utilities.is_valid_length("123.2", 4) == False

# def test_is_less_than_eq_to_length():

# def test_no_missing_values():
#
#
# def test_trim():
#
#
# def test_is_valid_aleph_year():
#
#
# def test_is_valid_aleph_date():
#
# def test_is_valid_hour():
