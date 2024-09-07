from src.filters import count_words, filter_more_than_five_words, filter_five_or_less_words

def test_count_words():
    assert count_words("This is - a self-explained example") == 5
    assert count_words("Short title") == 2

def test_filter_more_than_five_words():
    entries = [
        {'title': 'This is a long title', 'comments': 10},
        {'title': 'Short', 'comments': 5},
        {'title': 'Another long title here', 'comments': 15}
    ]
    filtered = filter_more_than_five_words(entries)
    assert len(filtered) == 2
    assert filtered[0]['comments'] == 15

def test_filter_five_or_less_words():
    entries = [
        {'title': 'This is a long title', 'points': 100},
        {'title': 'Short', 'points': 50},
        {'title': 'Another short one', 'points': 75}
    ]
    filtered = filter_five_or_less_words(entries)
    assert len(filtered) == 2
    assert filtered[0]['points'] == 75