# sample_text = 'hi this is a sample'
# print(sample_text)
# print('\u0336'.join(sample_text) + '\u0336')

test_dict = {'Test One': 1, 'Test Two': 2, 'Test Three': 3}
print(test_dict)
test_dict['\u0336'.join('Test One') + '\u0336'] = test_dict.pop('Test One')
print(test_dict)