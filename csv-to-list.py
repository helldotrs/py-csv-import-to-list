import csv
def import_csv_as_list(file_name = file.csv)

    with open(f'{file_name}', mode='r') as file:
        # create csv reader
        csv_reader = csv.DictReader(file)

        data_list = []

        for row in csv_reader:
            data_list.append(row)

    return data_list