
aapl_file = open("aapl.csv", "r")

aapl_string = aapl_file.readlines()

aapl_list = []



for data in aapl_string:
    aapl_list.append(data.split(","))
    print type(aapl_list[0][0])

aapl_file.close()
