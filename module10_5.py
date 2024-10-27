from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            if line != '\n':
                all_data.append(line)
            else:
                break


if __name__ == '__main__':
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]

    start = datetime.now()
    for filename in filenames:
        read_info(filename)
    print(f'Time: {datetime.now() - start} (линейный)')

    start = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'Time: {end - start} (многопроцессный)')
