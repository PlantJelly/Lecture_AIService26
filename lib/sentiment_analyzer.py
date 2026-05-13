import joblib
from konlpy.tag import Okt
def korean_tokenizer(text):
    my_tags = ['Noun', 'Adjective', 'Verb']
    my_stopwords = []
    return [word for word, tag in Okt().pos(text) if tag in my_tags and word not in my_stopwords]

class SentimentAnalyzer:
    def __init__(self, tokenizer,vectorizer_file, predict_model_file):
        self.__vectorizer = joblib.load(vectorizer_file)
        self.__predict_model = joblib.load(predict_model_file)
        self.__tokenizer = tokenizer
    
    def analyze_sentiment(self, review):
        # 특징 벡터 추출
        review_fv = self.__vectorizer.transform([review])

        # 학습된 모델로 예측
        pred = self.__predict_model.predict(review_fv)

        # 예측값에 따라 결과를 생성하여 반환
        result = '긍정' if pred[0] >= 0.5 else '부정'
        return result, pred[0]