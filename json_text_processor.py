import os
import json

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

# 중복 단어 제거
unique_texts = list(set(texts))

with open('unique_texts.txt', 'w', encoding='utf-8') as f:
    for text in unique_texts:
        f.write(text + '\n')  # 각 단어를 새 줄에 저장

print(len(unique_texts))