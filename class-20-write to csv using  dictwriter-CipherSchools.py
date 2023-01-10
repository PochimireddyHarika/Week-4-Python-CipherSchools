from csv import DictWriter
with open('final.csv', 'w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'firstname':'harika'
        'lastname':'reddy'
        'age':18

    })
    csv_writer.writerow({
        'firstname':'sai'
        'lastname':'reddy'
        'age':15

    })
