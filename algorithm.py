import re
from math import exp

class Algorithm:

    def __init__(self):
        self.bug_words_words = ["bug", "not working"]
        self.feature_request_words = ["it would be great if", "can you add", "could you add", "is it possible to", "do you consider adding"]
        self.sales_question_words = ["sell", "buy", "question"]
        self.how_to_words = ["how"]
        self.technical_issue_words = ["problem", "issue"]
        self.cancellation_words = ["cancel", "order"]

    def preprocess(self, text):
        return text.lower()
    def predict(self, text):
        preprocessed_data = self.preprocess(text)
        words = re.findall(r"[\w']+", preprocessed_data)
        term_count = len(words)

        bug = 0.0
        feature_request = 0.0
        sales_question = 0.0
        how_to = 0.0
        technical_issue = 0.0
        cancellation= 0.0

        for word in words:
            if word in self.bug_words_words:
                bug+=1
            if word in self.feature_request_words:
                feature_request += 1
            if word in self.sales_question_words:
                sales_question += 1
            if word in self.how_to_words:
                how_to += 1
            if word in self.technical_issue_words:
                technical_issue += 1
            if word in self.cancellation_words:
                cancellation += 1
        exponentials = [exp(bug), exp(feature_request), exp(sales_question), exp(how_to), exp(technical_issue), exp(cancellation)]
        exp_sum = sum(exponentials)
        try:
            softmax = [x / (exp_sum) for x in exponentials]
        except:
            softmax = [1.0/6.0] * 6
        return { 
            'bug': softmax[0], 
            'feature_request': softmax[1],
            'sales_question': softmax[2],
            'how_to': softmax[3],
            'technical_issue': softmax[4],
            'cancellation': softmax[5],
            }
