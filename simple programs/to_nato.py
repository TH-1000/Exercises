# This is a codewars exercise that can be found here: https://www.codewars.com/kata/586538146b56991861000293
# The challenge is to encrypt messages ito a Nato format (Nato Phonetic alpabet): https://en.wikipedia.org/wiki/NATO_phonetic_alphabet

# Example: Input: If, you can read? /// Output: India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

def to_nato(words):
    nato = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel','I': 'India', 'J': 'Juliett', 'K': 'Kilo',
        'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'W': 'Whiskey',
        'V': 'Victor', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}
    word_list = []

    for i in words:
        if i == ' ' :
            continue
        if not i.isalpha():
            word_list.append(i)
            continue
        word_list.append(nato[i.upper()])

    result = ' '.join(word_list)
    return result

### Example:
print(to_nato('I would like to order two apples and a martini'))

### Output:
India Whiskey Oscar Uniform Lima Delta Lima India Kilo Echo Tango Oscar Oscar Romeo Delta Echo Romeo Tango Whiskey Oscar Alfa Papa Papa Lima Echo Sierra Alfa November Delta Alfa Mike Alfa Romeo Tango India November India
