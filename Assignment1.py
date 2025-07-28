import csv

def check_divisibility(a, b):
    try:
        print(a/b)
    except:
        print("Error: Cannot divide by zero")

# check_divisibility(10, 3)


def writeArray(array_2d, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(array_2d)
    print(f"Array written to {filename}")

def readArray(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        array_2d = [row for row in reader]
    return array_2d


arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

writeArray(arr, "array_data.csv")
loaded_arr = readArray("array_data.csv")
print("Loaded array:", loaded_arr)


