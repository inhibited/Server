#Backdated server
import os


def main():
    print(os.getcwd())
    fl = ['..']
    print(fl)
    x = os.listdir(path='C:\\Users\\almah\Desktop\Server\\')
    for i in range(len(x)):
        print(x[i])

if __name__ == '__main__':
    main()
