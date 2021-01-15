from prettytable import PrettyTable

table = PrettyTable(["Student", "Class", "Section", "Roll No.", "ID"])
table.add_row(["Satyam Tripathi", "A-11", "C", "1901640100244", "26390"])
table.add_row(["Aditya Trivedi", "A-17", "C", "1901640100250", "26396"])
table.add_row(["Shashank Tripathi", "A-12", "C", "1901640100245", "26391"])
table.add_row(["Navneet Pandey", "A-13", "C", "1901640100246", "26392"])
table.add_row(["Adarsh Gupta", "A-14", "C", "1901640100247", "26393"])
table.add_row(["Achyut Tripathi", "A-15", "C", "1901640100248", "26394"])
table.add_row(["Amit Gupta", "A-16", "C", "1901640100249", "26395"])
print(table)
