# Review-Sentiment-Analyzer
An ML-based sentiment classifier for restaurant reviews using logistic regression, providing real-time feedback to users
# Restaurant Review Sentiment Analyzer

This project implements a machine learning-based sentiment analysis tool that classifies restaurant reviews as **positive** or **negative**. The model uses **Logistic Regression** to predict the sentiment of user-provided reviews.

## Features
- Classifies user reviews as positive or negative.
- Uses Logistic Regression to perform sentiment analysis.
- Displays real-time feedback based on the analysis.
- Can be easily extended to work with other types of reviews or text data.

## Installation

To run the project, you'll need Python and the following dependencies:

1. Clone the repository:
   ```bash
 git clone https://github.com/HanieAkrami/Review-Sentiment-Analyzer.git
   cd REPO_NAME
2.Install the required libraries:
pip install -r requirements.txt


## Usage

1.After installing the dependencies, you can run the sentiment analysis model by executing:
python model.py
2.The model will process a review, predict its sentiment, and output feedback (positive/negative)


## Example

Here is an example of how the model works:
review = "The food was amazing, and the service was excellent!"
prediction = model.predict(review)
print(prediction)

## Contributing

Feel free to open an issue or submit a pull request if you'd like to contribute. Contributions are always welcome!
