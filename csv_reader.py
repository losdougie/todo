import csv


def read_csv(file):
    csv_data = []
    with open(file, "r") as f:
        while f:
            reader = csv.DictReader(f)
            if "policyID" in reader.fieldnames:
                break
        header = reader.fieldnames
        for row in reader:
            csv_data.append(row)
    return csv_data

def main():
    count = 0
    for row in read_csv("example.csv"):
        print(",".join([row["county"], row["fr_site_deductible"]]))
        count += 1
        if count > 20:
            break


if __name__== "__main__":
    main()