# eicar testvirus generator
# create eicar_n.txt files in an endless loop
import time

def main():
    eicar = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
    i = 0
    while True:
        filename = 'eicar_' + str(i) + '.txt'
        with open(filename, 'w') as file:
            file.write(eicar)
        i+=1

if __name__ == '__main__':
    main()
