# 등장 빈도수가 threshold회 미만인 단어들이 이 데이터에서 얼만큼의 비중을 차지하는지 확인
def word_status_below_threshold(test_tokenizer, threshold):
    total_cnt = total_freq = 0
    rare_cnt = rare_freq = 0
    for _, count in test_tokenizer.word_counts.items():
        total_cnt += 1
        total_freq += count
        if count < threshold:
            rare_cnt += 1
            rare_freq += count

    print(f'=== 빈도수가 {threshold}번 이상인 단어만 사용하는 경우 ===')
    print(f'전체 단어 : {total_cnt:,}개 {total_freq:,}번')
    print(f'희귀 단어 : {rare_cnt:,}개 ({rare_cnt/total_cnt*100:.2f}%) {rare_freq:,}번 ({rare_freq/total_freq*100:.2f}%)')
    print(f'사용할 단어 : {total_cnt - rare_cnt:,}개 ({(total_cnt - rare_cnt) / total_cnt * 100:.2f}%) {total_freq - rare_freq:,}번 ({(total_freq - rare_freq) / total_freq * 100:.2f}%)')

#텍스트의 길이가 설정한 max_len 이하인 비율 계산

def text_len_status_below_maxlen(tokened_texts, max_len):
    below_text = 0
    for text in tokened_texts:
        if len(text) <= max_len:
            below_text += 1

    print(f'텍스트의 토큰 수가 {max_len} 이하인 텍스트 : {below_text:,}개 ({below_text / len(tokened_texts) * 100:.2f}%)')