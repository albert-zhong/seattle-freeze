import csv
import geo_streaming


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


def get_word_frequency(location):
        data_path = geo_streaming.get_path(location[1])

        all_text = ""  # String that contains all tweet texts

        with open(data_path, mode="r") as data_file:
                csv_reader = csv.reader(data_file)
                for row in csv_reader:
                        all_text += " " + row[2].lower()

        word_list = all_text.split()         
        word_frequency = [word_list.count(word) for word in word_list]  # a list comprehension
        pairs = zip(word_list, word_frequency)  # tuple for word and corresponding frequency

        # Now creating CSV file for word frequency mappings
        words_path = geo_streaming.get_path(location[1] + "_words")

        with open(words_path, mode="w+") as words_file:
                writer = csv.writer(words_file)
                writer.writerow(["word", "frequency"])
                for pair in pairs:
                        writer.writerow([pair[0], pair[1]])
        
