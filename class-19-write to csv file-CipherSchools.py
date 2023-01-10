from csv import writer
with open('file3.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['harika','india'])
    csv_writer.writerow(['sai','india'])

