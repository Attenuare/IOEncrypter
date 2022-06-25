import datetime


# Transform text into a numeric code
def transform_into_code(text: str) -> int:
    joined_code = '20'
    all_joined = []
    for caracter in text:
        joined_code += f'{ord(caracter)}20'
        if joined_code.count('20') == 4:
            all_joined.append(joined_code)
            joined_code = '20'
    final_code = ''
    for joined_code in all_joined:
        occurrence_count = 0
        while int(joined_code) % 2 == 0:
            joined_code = int(joined_code)/2
            occurrence_count += 1
        final_code += f'{int(joined_code)}f{occurrence_count}x'
    return final_code


# Get a code and transform into a text
def decrypto_code(code: str) -> str:
    all_joined = code.split('x')
    decrypted_code = ''
    for part_code in all_joined:
        separated_parts = part_code.split('f')
        if separated_parts != ['']:
            for occurrence in range(int(separated_parts[1])):
                separated_parts[0] = int(separated_parts[0]) * 2
            decrypted_code += str(separated_parts[0])
    separated_letter = decrypted_code.split('20')
    return ''.join(chr(int(letter)) for letter in separated_letter if letter != '')


# Get a file with the text that is going to be used
def manipulating_data(final_code: str or None = None, typing: str = 'r', file_name: str = '', mode: str = None) -> str:
    if typing == 'w' and mode == 'e':
        file_name = f'{file_name}_encryted_{datetime.datetime.now().date()}'
    elif typing == 'w' and mode == 'd':
        file_name = f'{file_name}_decryted_{datetime.datetime.now().date()}'
    else:
        file_name = str(input('Enter the name of the file without the txt extension: ')).strip()
    with open(f'{file_name}.txt', typing, encoding='utf8') as txt_file:
        if final_code:
            txt_file.write(final_code)
            return
        else:
            reader = txt_file.read()
            return [reader, file_name]


# Main function that set the order of the script
def main():
    print(10 * '-', 'IOEncrypter', 10 * '-')
    continuation = ''
    while continuation != 'n':
        option = int(input('Encrypt a text: Option [0]\nDecrypt a text: Option [1]\nEnter your choice: '))
        if option != 1 and option != 0:
            print('Invalid choice, try again!')
            continue
        else:
            if option == 0:
                print('Reading file...')
                text = manipulating_data()
                if text[0] == '':
                    print("The file isn't readable!")
                    continue
                print('Tranforming into a code...')
                final_code = transform_into_code(text[0])
                print('Generating the output file!')
                manipulating_data(final_code, 'w', text[1], 'e')
                print('Output file is ready!')
            elif option == 1:
                print('Reading file...')
                final_code = manipulating_data()
                if final_code[0] == '':
                    print("The file isn't readable!")
                    continue
                print('Decrypting code...')
                final_words = decrypto_code(final_code[0])
                manipulating_data(final_words, 'w', final_code[1], 'd')
                print('Output file is ready!')
        while continuation != 'n' and continuation != 'y':
            continuation = str(input('Do you want to keep encrypting or decrypting texts? Yes[y] or No[n]\nChoise: ')).strip().lower()
            if continuation != 'n' and continuation != 'y':
                print('Invalid choice, try again!')
    print(8 * '-', 'Thanks for using IOEncrypter!', 8 * '-')


if __name__ == '__main__':
    main()
