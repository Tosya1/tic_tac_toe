from datetime import datetime as dt


def log (msg):
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open ('log.csv', 'a', encoding="utf8") as file:
        file.write(f'{time}; {msg}\n')

