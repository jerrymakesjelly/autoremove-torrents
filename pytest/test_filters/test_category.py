#-*- coding:utf-8 -*-
from autoremovetorrents.filter.category import CategoryFilter

def test_all_categories(load_data):
    category_filt = CategoryFilter(True, [], [])
    assert [x.name for x in category_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['all_categories']

def test_categories(load_data):
    category_filt = CategoryFilter(False, ['Category - 1'], [])
    assert [x.name for x in category_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['category_1']

def test_all_excluded_categories(load_data):
    category_filt = CategoryFilter(False, [], ['Category - 2'])
    assert [x.name for x in category_filt.apply(load_data['input'])] == []

def test_all_categories_and_categories(load_data):
    # Note: 'Category - 4' does not exist
    category_filt = CategoryFilter(True, ['Category - 4'], [])
    assert [x.name for x in category_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['all_categories']

def test_all_categories_and_excluded_categories(load_data):
    category_filt = CategoryFilter(True, [], ['Category - 2'])
    assert [x.name for x in category_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['category_1_and_category_3']

def test_categories_and_excluded_categories(load_data):
    category_filt = CategoryFilter(False, ['Category - 1', 'Category - 2'], ['Category - 2'])
    assert [x.name for x in category_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['category_1']