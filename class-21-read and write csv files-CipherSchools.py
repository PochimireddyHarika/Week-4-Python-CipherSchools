from csv import DictReader, DictWriter
with open('file.csv', 'r') as rf:
    with open('file2.csv', 'w') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['first_name', 'last','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname, lname, age = row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({
                'first_name':fname.lower(),
                'last name':lname.lower(),
                'age':age
            })