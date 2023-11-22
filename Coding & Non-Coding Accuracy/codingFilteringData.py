import os
import json

# Directory containing your JSON files
directory_path = "/content/DevGPT/snapshot_20230727/"


# List all JSON files in the directory
json_files = [f for f in os.listdir(directory_path) if f.endswith(".json")]

# Collect "Answer" where "ListOfCode" is not empty from each file
filtered_data = []
for json_file in json_files:
    file_path = os.path.join(directory_path, json_file)
   
    with open(file_path, 'r') as file:
        data = json.load(file)

    for source in data.get("Sources", []):
        for conversation in source.get("ChatgptSharing", []):
            if "Conversations" in conversation:
                for prompt_answer in conversation["Conversations"]:
                    if prompt_answer.get("ListOfCode"):
                        filtered_data.append({"Answer": prompt_answer["Answer"]})

# Save the filtered data to a new JSON file
output_file_path = "/content/drive/MyDrive/codingQuestionsFilteredData.json"
with open(output_file_path, 'w') as json_file:
    json.dump(filtered_data, json_file, indent=4)

print("Filtered data saved to codingQuestionsFilteredData.json")


