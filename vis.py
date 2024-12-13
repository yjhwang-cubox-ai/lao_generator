import os
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

def read_json_files(directory):
    json_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                data = json.load(file)
                json_data += data['data_list']
    return json_data

# 사용 예
directory_path = 'anno_file'
all_json_data = read_json_files(directory_path)

texts = []
for json_data in all_json_data:
    text = json_data['instances'][0]['text']
    texts.append(text)
# 단어 빈도 계산
word_counts = Counter(texts)

# WordCloud 생성
wordcloud = WordCloud(font_path='saysettha.ttf', background_color="white").generate_from_frequencies(word_counts)

# 시각화 및 저장
output_path = "wordcloud.png"
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig(output_path, dpi=300)  # dpi 설정으로 해상도 조절
plt.close()  # 플롯 창 닫기