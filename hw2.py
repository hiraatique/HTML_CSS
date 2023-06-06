#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.


def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0


    if length % 2:
        add = 1

    left = s[:half + add]
    right = s[half + add:]


    print(f'left = {left}')
    print(f'right = {right}')

    return right + left


test_data_even = 'bbbbbcaaaaa'
test_data_odd = '‘aaaaabbbbbc’'
split_in_half(test_data_odd)
split_in_half(test_data_even)



#Unique characters
#abcde -> True
#abcdd -> Flase

def unique_character(s):
   return len(set(s)) == len(s)

test_data_unique = 'abcde'
test_data_duplicate = 'abcdd'

print(unique_character(test_data_unique))
print(unique_character(test_data_duplicate))





