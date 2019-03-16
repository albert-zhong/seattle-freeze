import csv


def get_means(path):

    mean_polarity = 0
    mean_subjectivity = 0
    row_counter = 0

    with open(path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skips header
        for row in reader:
            mean_polarity += float(row[3])
            mean_subjectivity += float(row[4])
            row_counter += 1
    
    return (mean_polarity/row_counter, mean_subjectivity/row_counter)


def get_mean_polarity(path):

    mean_polarity = 0
    row_counter = 0

    with open(path, "r") as f:
        reader = csv.reader(f)
        next(reader) # Skips header
        for row in reader:
            mean_polarity += float(row[3])
            row_counter += 1
    
    return (mean_polarity/row_counter)


def get_mean_subjectivity(path):

    mean_subjectivity = 0
    row_counter = 0

    with open(path, "r") as f:
        reader = csv.reader(f)
        next(reader) # Skips header
        for row in reader:
            mean_subjectivity += float(row[4])
            row_counter += 1
    
    return (mean_subjectivity/row_counter)
