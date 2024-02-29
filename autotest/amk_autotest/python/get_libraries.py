import os

def print_allowed_libraries():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    ALLOWED_LIBRARIES_FILE = os.path.join(script_directory, 'allowed_libraries.txt')
    file = os.path.basename(ALLOWED_LIBRARIES_FILE)
    if os.path.exists(ALLOWED_LIBRARIES_FILE):
        print(f"File {file} exists")
        with open(ALLOWED_LIBRARIES_FILE, 'r') as f:
            lines = f.readlines()
    else:
        print(f"File {file} does not exist")
    
    print('*'*32)
    print('These libraries are allowed: ')
    print('-'*32)
    for line in lines:
        line.strip()
        print(line,end='')
    print()
    print('-'*32)
    #with open(ALLOWED_LIBRARIES_FILE, 'r') as f:
     #   print(f.readlines())