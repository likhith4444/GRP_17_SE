# GRP_17_SE

The Research questions we have chosen are:
1)What is the typical structure of conversations between developers and ChatGPT? How many turns does it take on average to reach a conclusion?
2)How accurately does ChatGPT respond when compared with code blocks and conversation blocks?
3)How does ChatGPT's ability to provide instant feedback impact the iterative development and debugging process for developers?

Methodology:
        For the first question, our primary objective is to determine the average number of turns in conversations between developers and ChatGPT for resolved issues. We plan to source 
datasets from the GitHub repository, ensuring data cleaning to remove any irrelevant entries or duplicates. Through data mining techniques, we aim to compute both the accuracy and average 
prompt count. We will employ visualization approaches to show the distribution of prompt numbers by importing matplotlib.

        For the second question, we will take the “ChatGPT Sharing” object from discussion in every object of the dataset, separate the code and conversation blocks using “NumPy” (python
library) and save them in different files, using “pandas” library in python. After filtering, wemanually analyze the conversation and search for keywords like ‘apologize’ and ‘sorry for 
confusion’ to get a grasp of how it is not efficient. We use a trained model like ‘regular expression’ with the key words specified and compare them between code block and conversational block 
to see how far the ChatGPT was able to grasp the intentions of the developer and how many prompts it took to resolve a single question. Then we will use the “seaborn” library to graphically 
represent the comparison between code and conversational blocks.

For the third question, we'll explore how ChatGPT's instantaneous feedback feature influences developers' iterative development and debugging cycles. Our goal is to comprehend 
the efficiency gains or potential problems that developers may face by utilizing quick reaction times. Using visualization tools like pandas, numpy and seaborn, we will chart the correlation 
between instant feedback and accelerated development phases. Furthermore, we want to find patterns, abnormalities, or possible locations where the instant feedback mechanism performs 
well or poorly by examining feedback patterns. Furthermore, machine learning models could be used to forecast the efficacy of real-time input depending on various development scenarios, 
providing insights into the factors that lead to improved development cycles or potential slowdown.
