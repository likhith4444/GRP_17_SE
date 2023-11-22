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

    def create_pie_chart(self, sizes, labels, chart_title):
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

        # Adding title
        plt.title(chart_title)

        # Show the pie chart
        plt.show()

    def analyze_and_visualize_pie(self, chart_title):
        avg_prompts = self.calculate_avg_prompts()
        sizes = avg_prompts.values
        labels = avg_prompts.index

        self.create_pie_chart(sizes, labels, chart_title)


# Example usage
json_file_path_pr = '/content/DevGPT/snapshot_20230831/20230831_060603_pr_sharings.json'
json_file_path_issue = '/content/DevGPT/snapshot_20230831/20230831_061759_issue_sharings.json'

analyzer_pr = ChatGPTAnalyzer(json_file_path_pr)
analyzer_issue = ChatGPTAnalyzer(json_file_path_issue)

analyzer_pr.analyze_and_visualize_pie('Pull Request')
analyzer_issue.analyze_and_visualize_pie('Issue')
