import db

d = db.Database()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def prompt(msg):
    return input(bcolors.HEADER + msg + bcolors.ENDC)

def print_results(rows):
    for row in rows:
        print(row[0])

def add_note():
    title = prompt("  document title: ")
    desc = prompt("  content description: ")
    d.add_note(title, desc, 'path/to/file.pdf')

def search_notes():
    kw = prompt('  keywords: ')
    d.search_notes(kw)

def main():
    while True:
        cmd = input('appnote > ')

        if cmd == 'add':
            add_note()

        elif cmd == 'search':
            search_notes()

        elif cmd == 'dump':
            print(d.print_all())

        elif cmd == 'exit':
            exit(0)

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()
        exit(0)