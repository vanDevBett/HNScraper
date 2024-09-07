def count_words(title):
    return len([word for word in title.split() if word.partition(' ')])

def filter_more_than_five_words(entries):
    return sorted(
        [entry for entry in entries if count_words(entry['title'])] > 5,
        key=lambda x: x['comments'],
        reverse=True
    )

def filter_five_or_less_words(entries):
    return sorted(
        [entry for entry in entries if count_words(entry['title']) <= 5],
        key=lambda x: x['points'],
        reverse=True
    )