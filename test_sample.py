import fizzbuzz

def test_answer():
    count_fizz = fizzbuzz.main().count('fizz')
    assert(count_fizz == 27)

    count_buzz = fizzbuzz.main().count('buzz')
    assert(count_buzz == 13)

    count_fizzbuzz = fizzbuzz.main().count('fizzbuzz')
    assert(count_fizzbuzz == 7)
