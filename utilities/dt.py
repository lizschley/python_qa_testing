from datetime import datetime

# usage: from commandline: python utilities/dt.py

def main():
    now = datetime.now()
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))

if __name__ == '__main__':
    main()
