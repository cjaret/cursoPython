def run():
    counter = 0
    with open('./aleph.txt', encoding="utf-8") as f:
        for line in f.readlines():
            counter += line.count('Beatriz') #count() es un método de strings

    print('Beatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()