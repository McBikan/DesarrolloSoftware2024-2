from count_words import CountWords


def test_two_words_ending_with_s():
    words = CountWords().count("dogs cats")
    assert words == 2

def test_no_words_at_all():
    words = CountWords().count("dog cat")
    assert words == 0