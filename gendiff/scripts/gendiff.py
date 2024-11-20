import argparse

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='First configuration file')
    parser.add_argument('second_file', type=str, help='Second configuration file')
    parser.add_argument(
        '-f', '--format',
        dest='format',
        help='set format of output',
        default='plain'
    )
    args = parser.parse_args()

if __name__ == "__main__":
    main()
