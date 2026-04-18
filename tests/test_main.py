import pytest

def reverse_name(name):
    return ''.join(sorted(name, reverse=True))

def test_reverse_name():
    assert reverse_name('ali') == 'ila'
    assert reverse_name('bob') == 'bob'
    assert reverse_name('python') == 'ythnop'

def test_reverse_name_empty():
    assert reverse_name('') == ''

def test_reverse_name_single_char():
    assert reverse_name('a') == 'a'

def test_reverse_name_multiple_chars():
    assert reverse_name('abcdefg') == 'gfedcba'
