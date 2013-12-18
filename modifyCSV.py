import csv

with open('results.csv','r') as csvinput:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('user')
        all.append(row)

        for row in reader:
            row.append(row[9][:5]+row[10])
            all.append(row)

        writer.writerows(all)