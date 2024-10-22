import json

# 1. Open a new file, open() .close()
file = open("example.txt", "w")  # Open a new file for writing
file.write("Hello, World!\n")
file.close()  # Close the file

# 2. .readlines(), .read()
file = open("example.txt", "r")  # Open the file for reading
content = file.read()  # Read the entire content
print("Content using read():")
print(content)

file.seek(0)  # Move the cursor back to the beginning
lines = file.readlines()  # Read content as a list of lines
print("Content using readlines():")
print(lines)
file.close()

# 3. write, encoding=utf-8
with open("unicode.txt", "w", encoding="utf-8") as f:
    f.write("Hejsan världen!")  # Med utf-8 kan vi använda åäö

with open("unicode.txt", "r", encoding="utf-8") as f:
    print("UTF-8 encoded content:")
    print(f.read())

# 4. json.load()
# Create a JSON file to load
data = {"name": "Alice", "age": 25, "city": "Wonderland"}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Now load the JSON data from the file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("Loaded JSON data:")
    print(loaded_data)

# 5. json.dump()
# Modify the data and dump it back to the file
data["age"] = 26  # Update age
with open("data.json", "w") as json_file:
    json.dump(data, json_file)
    print("Updated data has been dumped to data.json")

"""
1. Open a new file, open() .close()
2. .readlines(), .read()
3. write, encoding=utf-8
4. json.load()
5. json.dump()
"""
