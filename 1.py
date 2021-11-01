import csv

def read_csv(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines

 def write_csv(file_name, data_list):
     with open(file_name, "w", newline="") as f:
        csv.writer(f).writerows(data_list)

def deal_data(arr)
    dic = {}
    for i in range(1, len(arr))
    _, label, chinese, english = arr[i].strip().split(",")
    if label not in dic:
        dic[label] =[]
    dic[label]. append