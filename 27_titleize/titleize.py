def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lowered = phrase.lower()
    list_of_words = lowered.split(' ')
    capitalized_list_of_words = []
    for word in list_of_words:
        capitalized_list_of_words.append(word.capitalize())
    return ' '.join(capitalized_list_of_words)