# Flat file databases
import csv
with open("hardwareStore.csv", "r") as object:
    # datasheet = csv.reader(object)
    # for row_list in datasheet:
    #     countries_cell = row_list[21]
    #     print(countries_cell)

# Headers or row 1 = dictionary got from csv.DictReader(object)
# Each corresponding cells below header is value from same row_dictionary
# key(header):value(cells below) === Row dictionary
    dict_read = csv.DictReader(object)
    counts = {}
    for row_dict in dict_read:
        value_countries = row_dict["COUNTRY_NAME"]
        if value_countries in counts:
            counts[value_countries] += 1
        else:
            counts[value_countries] = 1

# def get_value(COUNTRY_NAME):
#     return counts [COUNTRY_NAME]
# for value_countries in sorted(counts, key = get_value, reverse=True):
#     print( f"{value_countries}:{counts[value_countries]}")
# OR Instead of get_value function using once as argument , use lambda function
#  Only replace columns name and get new data every time
# Print out the data according to columns
# for value_countries in sorted(counts, key = lambda COUNTRY_NAME: counts[COUNTRY_NAME] , reverse=True):
#     print( f"{value_countries}:{counts[value_countries]}")

city = input("Enter your country : ")
if value_countries in counts:
    print(f"{value_countries}: {counts[value_countries]}")