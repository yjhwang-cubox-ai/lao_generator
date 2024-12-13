import os
import json
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

# 각 원소의 개수를 세기
text_counts = Counter(texts)

# 히스토그램 그리기
plt.bar(text_counts.keys(), text_counts.values())
plt.xlabel('Text')
plt.ylabel('Count')
plt.title('Histogram of Text Occurrences')
plt.xticks(rotation=45, ha='right')

plt.savefig('histogram.png')  # 파일 이름을 지정하여 저장
plt.show()