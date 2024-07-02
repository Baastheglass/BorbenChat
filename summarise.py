import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
# Ensure you have the necessary NLTK data files
nltk.download('punkt')
# Load the CSV file
file_path = './train.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)
# Define the maximum length for the responses
max_length = 5000
# Function to summarize responses
def summarize_response(response):
    if len(str(response)) <= max_length:
        return response
    sentences = sent_tokenize(response)
    summary = ''
    for sentence in sentences:
        if len(summary) + len(sentence) + 1 > max_length:
            break
        summary += sentence + ' '
    return summary.strip()
# Apply the summarization function to the 'Response' column
data['Response'] = data['Response'].apply(summarize_response)
# Save the modified dataframe to a new CSV file
output_file_path = './summarized_train.csv'  # Replace with your desired output path
data.to_csv(output_file_path, index=False)
print(f"Summarized CSV file saved to {output_file_path}")







