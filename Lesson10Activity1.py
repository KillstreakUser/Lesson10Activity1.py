import os

print("-Science Notes")
with open("C:\\Users\\ajayk\\OneDrive\\Documents\\Codingul Codes\\Codingal Activities\\Module.8\\ScienceNotes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("-Word Count")
with open("C:\\Users\\ajayk\\OneDrive\\Documents\\Codingul Codes\\Codingal Activities\\Module.8\\ClassNotes.txt") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
print()

print("-Merging Notes")
if os.path.exists("All-Notes.txt"):
    print("All-Notes.txt already exists - overwritting")
else:
    print("All-Notes.txt not found - creating")

content = ""
with open("C:\\Users\\ajayk\\OneDrive\\Documents\\Codingul Codes\\Codingal Activities\\Module.8\\ScienceNotes.txt", "r") as f:
    content += "-ScienceNotes.txt\n"
    content += f.read() +"\n"
with open("C:\\Users\\ajayk\\OneDrive\\Documents\\Codingul Codes\\Codingal Activities\\Module.8\\ClassNotes.txt", "r") as f:
    content += "-ClassNotes.txt\n"
    content += f.read() +"\n"
with open("All-Notes.txt", "w") as out:
    out.write(content)
print("Saved to All-Notes.txt")
print()

if os.path.exists("All-Notes.txt"):
    os.remove("All-Notes.txt")
    print("All-Notes.txt Deleted.")
else:
    print("All-Notes.txt Does Not Exist.. 404")

