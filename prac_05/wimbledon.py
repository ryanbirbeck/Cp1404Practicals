"""
Word Occurences
Estimate: 30
Actual: 40
"""

FILENAME = "wimbledon.csv"


def main():
    records =get_records(FILENAME)
    winner_to_count, countries = process_records(records)
    display_results(winner_to_count, countries)


def display_results(winner_to_count, countries):
    """Display summary of winners and countries"""
    print("Wimbledon Champs: ")
    for name, count in winner_to_count.items():
        print(f"{name:20} : {count}")   # arbitrary value for spacing
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def process_records(records):
    winner_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            winner_to_count[record[2]] += 1
        except KeyError:
            winner_to_count[record[2]] = 1
    return winner_to_count, countries


def get_records(FILENAME):
    """Retrieve the values in the csv file"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
