import os
import json
import pandas as pd
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

# 데이터프레임 생성
df = pd.DataFrame(word_counts.items(), columns=["단어", "갯수"])

# 갯수를 기준으로 내림차순 정렬
df = df.sort_values(by="갯수", ascending=False)

# .csv 파일로 저장
output_path = "word_counts.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"단어 빈도 데이터가 '{output_path}' 파일로 저장되었습니다.")
