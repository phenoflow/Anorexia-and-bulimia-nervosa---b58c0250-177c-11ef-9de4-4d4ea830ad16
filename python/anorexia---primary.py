# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"1467.00","system":"readv2"},{"code":"E271.00","system":"readv2"},{"code":"Eu50000","system":"readv2"},{"code":"9581.0","system":"readv2"},{"code":"4377.0","system":"readv2"},{"code":"34929.0","system":"readv2"},{"code":"33863.0","system":"readv2"},{"code":"6583.0","system":"readv2"},{"code":"30570.0","system":"readv2"},{"code":"2135.0","system":"readv2"},{"code":"605.0","system":"readv2"},{"code":"F50.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anorexia-and-bulimia-nervosa-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anorexia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anorexia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anorexia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
