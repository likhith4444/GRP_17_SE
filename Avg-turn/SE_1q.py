import json
import matplotlib.pyplot as plt
import pandas as pd

class ChatGPTAnalyzer:
    def __init__(self, json_file_path):
        self.data = self.load_json(json_file_path)
        self.prompts_data = self.extract_prompts_data()

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def extract_prompts_data(self):
        return [{'State': source['State'], 'NumberOfPrompts': y.get('NumberOfPrompts', 0)}
                for source in self.data.get('Sources', [])
                for y in source.get('ChatgptSharing', [])]

    def calculate_avg_prompts(self):
        df = pd.DataFrame(self.prompts_data)
        return df.groupby('State')['NumberOfPrompts'].mean().round().reindex(['OPEN', 'CLOSED'], fill_value=0)

    def create_bar_chart(self, data, chart_title, ax):
        data.plot(kind='bar', ax=ax)
        ax.set_title(chart_title)
        ax.set_ylabel('Average Number of Turns')
        ax.set_xlabel('State')

    def analyze_and_visualize_bar(self):
        avg_prompts = self.calculate_avg_prompts()
        return avg_prompts

# Initialize the analyzers
analyzer_pr = ChatGPTAnalyzer('/content/20230831_060603_pr_sharings.json')
analyzer_issue = ChatGPTAnalyzer('/content/20230831_061759_issue_sharings.json')

# Get the data
data_pr = analyzer_pr.analyze_and_visualize_bar()
data_issue = analyzer_issue.analyze_and_visualize_bar()

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Create the bar charts
analyzer_pr.create_bar_chart(data_pr, 'Pull Request', ax1)
analyzer_issue.create_bar_chart(data_issue, 'Issue', ax2)

plt.tight_layout()
plt.show()
