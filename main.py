import csv

def read_csv(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines

def write_csv(file_name, data_list):
     with open(file_name, "w", newline="") as f:
        csv.writer(f).writerows(data_list)

# grade = [
# "Name,Grade,Chinese, English",
# "Peixiu, A, 100, 90",
# "Jan, A, 90, 80",
# "Ben, B, 80, 90",
# "Yue, B, 75, 70",
# "Oliver, C, 60, 50"
# ]

def total_score(arr):
    Total_C_E = []
    for i in range(len(arr)):
        if i == 0:
            continue
        score = arr[i].strip().split(",")[2:]
        Total_C_E.append([float(score[0])+float(score[1])])
    return Total_C_E


def main():
    data = read_csv("practice.csv")
    result = total_score(data)
    write_csv("result.csv", result)
    print("--END--")

if __name__ == '__main__':
  main()
