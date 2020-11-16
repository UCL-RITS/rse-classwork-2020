# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:47:39 2020

@author: User
"""

from times import compute_overlap_time, time_range
import pytest


@pytest.mark.parametrize("test_times1,test_times2,expected",
                         [(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
                           time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
                           [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
                          (time_range("2010-01-12 10:45:00", "2010-01-12 12:00:00"),
                           time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
                           []),
                          (time_range("2010-01-12 10:45:00", "2010-01-12 12:00:00"),
                           time_range("2010-01-12 10:30:00", "2010-01-12 10:35:00", 2, 60),
                           [])
                          ]
)

def test_compute_overlap(test_times1,test_times2,expected):
    result=compute_overlap_time(test_times1,test_times2)
    assert result==expected

def test_given_input():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    
    result=compute_overlap_time(large,short)
    expected=[('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    
    assert result==expected
 
    
def test_given_input_edge():

    large = time_range("2010-01-12 10:45:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    
    result=compute_overlap_time(large,short)
    expected=[]
    
    assert result==expected
    

def test_given_input_no_overlap():

    large = time_range("2010-01-12 10:45:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:35:00", 2, 60)
    print(compute_overlap_time(large, short))
    
    result=compute_overlap_time(large,short)
    expected=[]
    
    assert result==expected
    
def test_end_before_start():

    
    with pytest.raises(ValueError):
        time_range("2010-01-12 11:45:00", "2010-01-12 10:00:00")  
        
        

    
    
# def test_given_input_empty_array():

#     large = time_range()
#     short = time_range("2010-01-12 10:45:00", "2010-01-12 10:45:00", 2, 60)
#     print(compute_overlap_time(large, short))
    
#     result=compute_overlap_time(large,short)
#     expected=[('2010-01-12 10:45:00', '2010-01-12 10:32:00'), ('2010-01-12 10:45:00', '2010-01-12 10:35:00')]
    
#     assert result==expected