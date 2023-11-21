import json
import matplotlib.pyplot as plt

def AvgPromptCount(json_file_path,Chart_title):

  with open(json_file_path, 'r') as file:
      data = json.load(file)
  i=0;
  opened = [];
  closed=[];
  for source in data['Sources']:
      i=i+1;
      if source['State']=="CLOSED":
          for y in source['ChatgptSharing']:
              if 'NumberOfPrompts' in y:
                  #print(y['NumberOfPrompts'])
                  opened.append(y['NumberOfPrompts'])
      else:
          for y in source['ChatgptSharing']:
              if 'NumberOfPrompts' in y:
                  #print(y['NumberOfPrompts'])
                  closed.append(y['NumberOfPrompts'])


  AverageOpened=round(sum(opened)/len(opened));
  AverageClosed=round(sum(closed)/len(closed));
  #print(i);
  #print('opened:',AverageOpened);
  #print('closed:',AverageClosed);

  #categories
  categories = [];
  categories.append('Open')
  categories.append('Closed')
  values = [];
  values.append(AverageOpened);
  values.append(AverageClosed);


  plt.bar(categories, values)

  # Adding labels and title
  plt.xlabel('Issue State')
  plt.ylabel('Count')
  plt.title(Chart_title)

  # Show the bar chart
  plt.show()


json_file_path = 'C:\Users\yaram\Downloads\DevGPT\snapshot_20230831\20230831_060603_pr_sharings.json'

AvgPromptCount('C:\Users\yaram\Downloads\DevGPT\snapshot_20230831\20230831_060603_pr_sharings.json','Pull Request')
AvgPromptCount('C:\Users\yaram\Downloads\DevGPT\snapshot_20230831\20230831_061759_issue_sharings.json','Issue')