from konlpy.tag import Okt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib
import numpy as np

class SentimentAnalyzer:
    def __init__(self, model_file, tokenizer_file):
        try:
            self.model = load_model(model_file)
        except FileNotFoundError:
            print(f'모델 파일 {model_file}이 없습니다.')

        try:
            self.tokenizer = joblib.load(tokenizer_file)
        except FileNotFoundError:
            print(f'토크나이저 파일 {tokenizer_file}이 없습니다.')

        self.morphs = Okt().morphs
    def analyze_sentiment(self, text):
        # 전처리 -> 신경망에 입력 형식에 맞게 변환 : 형태소 분석 => Integer Encoding => Padding
        tokens = Okt().morphs(text)
        encoded_text = self.tokenizer.texts_to_sequences([tokens])
        X = pad_sequences(encoded_text)
        preds = self.model.predict(X, verbose=0)
        labels = ['부정', '긍정']
        result_index = np.argmax(preds[0])
        return labels[result_index], preds[0][result_index]

if __name__ == '__main__':
    sa_model_file = './_AIService26/MovieSA_LSTM/model/sa_model_movie.keras'
    sa_tokenizer_file = './_AIService26/MovieSA_LSTM/model/sa_tokenizer_movie.pkl'
    sa = SentimentAnalyzer(sa_model_file, sa_tokenizer_file)
    
    reviews = [
        '이 영화 개꿀잼 ㅋㅋㅋ',
        '하품만 나온다',
        '이 영화 핵노잼 ㅠㅠ',
        '이딴게 영화냐 ㅉㅉ',
        '와 개쩐다',
        '감독 뭐하는 놈이냐',
        '정말 세계관 최강자들의 영화다'
    ]

    for review in reviews:
        result, prob = sa.analyze_sentiment(review)
        print(f'{review} --> {result}({prob*100:.2f})')