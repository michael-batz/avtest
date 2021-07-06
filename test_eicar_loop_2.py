# eicar testvirus generator
# create eicar.txt files in an endless loop
import time

def main():
    eicar = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
    while True:
        filename = 'eicar.txt'
        try:
            with open(filename, 'w') as file:
                file.write(eicar)
        except:
            pass

if __name__ == '__main__':
    main()
