import json
import matplotlib.pyplot as plt

def AvgPromptCount(json_file_path, Chart_title):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    i = 0
    opened = []
    closed = []

    for source in data['Sources']:
        i = i + 1
        if source['State'] == "CLOSED":
            for y in source['ChatgptSharing']:
                if 'NumberOfPrompts' in y:
                    opened.append(y['NumberOfPrompts'])
        else:
            for y in source['ChatgptSharing']:
                if 'NumberOfPrompts' in y:
                    closed.append(y['NumberOfPrompts'])

    AverageOpened = round(sum(opened) / len(opened))
    AverageClosed = round(sum(closed) / len(closed))

    # categories
    categories = ['Open', 'Closed']
    values = [AverageOpened, AverageClosed]

    plt.plot(categories, values, marker='o', linestyle='-', color='b')

    # Adding labels and title
    plt.xlabel('Issue State')
    plt.ylabel('Count')
    plt.title(Chart_title)

    # Show the line plot
    plt.show()

json_file_path_pr = '/content/DevGPT/snapshot_20230831/20230831_060603_pr_sharings.json'
json_file_path_issue = '/content/DevGPT/snapshot_20230831/20230831_061759_issue_sharings.json'
AvgPromptCount(json_file_path_pr, 'Pull Request')
AvgPromptCount(json_file_path_issue, 'Issue')
