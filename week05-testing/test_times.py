import times
import pytest
import datetime

@pytest.mark.parametrize("test_input1, test_input2, expected", [
    # no ovelap
    (('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
     ('2010-01-12 10:38:00', '2010-01-12 12:20:00'), 
     tuple()),

    # inside edge overlap
    (('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
     ('2010-01-12 10:30:00', '2010-01-12 10:35:00'),
     ('2010-01-12 10:30:00', '2010-01-12 10:35:00')),

    # equal intervals
    (('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
     ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
     ('2010-01-12 10:30:00', '2010-01-12 10:37:00')),

    # outside edge overlap
    (('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
     ('2010-01-12 10:37:00', '2010-01-12 10:39:00'),
     tuple()),

    # partial overlap
    (('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
     ('2010-01-12 10:34:00', '2010-01-12 10:42:00'),
     ('2010-01-12 10:34:00', '2010-01-12 10:37:00')),

    # subset overlap
    (('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
     ('2010-01-12 10:32:00', '2010-01-12 10:35:00'),
     ('2010-01-12 10:32:00', '2010-01-12 10:35:00')),

])
def test_overlap_helper(test_input1, test_input2, expected):
    assert times.compute_overlap_helper(test_input1, test_input2) == expected


@pytest.mark.parametrize("test_input1, test_input2, expected", [
    # inverted interval
    (('2010-01-12 10:35:00', '2010-01-12 10:32:00'),
     ('2010-01-12 10:38:00', '2010-01-12 12:20:00'),
     pytest.raises(ValueError)),

    # non-tuple input
    (['2010-01-12 10:30:00', '2010-01-12 10:37:00'],
     ['2010-01-12 10:34:00', '2010-01-12 10:42:00'],
     pytest.raises(TypeError)),

    # tuple interval of length != 2
    (('2010-01-12 10:35:00', '2010-01-12 10:32:00', '2010-01-12 10:39:00'),
     ('2010-01-12 10:38:00', '2010-01-12 12:20:00'),
     pytest.raises(TypeError)),

    # star and end of tuple interval of different datatypes
    (('2010-01-12 10:35:00', datetime.datetime.strptime('2010-01-12 10:39:00', "%Y-%m-%d %H:%M:%S")),
     ('2010-01-12 10:34:00', '2010-01-12 12:20:00'),
     pytest.raises(TypeError)),

])
def test_overlap_helper_errors(test_input1, test_input2, expected):
    with expected:
        times.compute_overlap_helper(test_input1, test_input2)

# def test_no_overlap():
#     assert(
#         times.compute_overlap_helper(
#             ('2010-01-12 10:30:00', '2010-01-12 10:37:00'), 
#             ('2010-01-12 10:38:00', '2010-01-12 12:20:00')
#         ) 
#         == tuple()
#     )

# def test_inside_edge_overlap():
#     assert(
#         times.compute_overlap_helper(
#             ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
#             ('2010-01-12 10:30:00', '2010-01-12 10:35:00')
#         )
#         == ('2010-01-12 10:30:00', '2010-01-12 10:35:00')
#     )


# def test_same_overlap():
#     assert(
#         times.compute_overlap_helper(
#             ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
#             ('2010-01-12 10:30:00', '2010-01-12 10:37:00')
#         )
#         == ('2010-01-12 10:30:00', '2010-01-12 10:37:00')
#     )

# def test_outside_edge_overlap():
#     assert(
#         times.compute_overlap_helper(
#             ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
#             ('2010-01-12 10:37:00', '2010-01-12 10:39:00')
#         )
#         == tuple()
#     )

# def test_partial_overlap():
#     assert(
#         times.compute_overlap_helper(
#             ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
#             ('2010-01-12 10:34:00', '2010-01-12 10:42:00')
#         )
#         == ('2010-01-12 10:34:00', '2010-01-12 10:37:00')
#     )

# def test_subset_overlap():
#     assert(
#         times.compute_overlap_helper(
#             ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
#             ('2010-01-12 10:32:00', '2010-01-12 10:36:30')
#         )
#         == ('2010-01-12 10:32:00', '2010-01-12 10:36:30')
#     )


# def test_inverted_interval():
#     with pytest.raises(ValueError) as exception:
#         times.compute_overlap_helper(
#             ('2010-01-12 10:35:00', '2010-01-12 10:30:00'),
#             ('2010-01-12 10:32:00', '2010-01-12 10:36:30')
#         )

#
#
#
        
    
