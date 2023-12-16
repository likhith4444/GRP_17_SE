import os
import json

# Directory containing your JSON files
directory_path = "./"


# List all JSON files in the directory
json_files = [f for f in os.listdir(directory_path) if f.endswith(".json")]

# Collect "Answer" where "ListOfCode" is not empty from each file
filtered_data = []
satisfaction = []

for json_file in json_files:
    file_path = os.path.join(directory_path, json_file)

    with open(file_path, 'r') as file:
        data = json.load(file)

    for source in data['Sources']:
        for sharing in source['ChatgptSharing']:
            allPrompts = []
            if 'Conversations' in sharing:
              for conversation in sharing['Conversations']:
                  allPrompts.append(detect_tone(conversation['Prompt'][:300]))
              n = len(allPrompts)
              if n>=2:
                  index = int(n*0.9)
                  bucket =start= n
                  for i in range(index):
                    bucket+=allPrompts[i]

                  avg  = [(x+1) * allPrompts[x] for x in range(index,n)]

                  cal = sum(avg)/len(avg)

                  bucket+=cal
                  if start>bucket:
                      satisfaction.append(1)
                  else:
                      satisfaction.append(-1)


