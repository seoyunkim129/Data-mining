##1번 문제
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [26, 39, 34, 30, 27],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'Country': ['USA', 'Canada', 'UK', 'USA', 'Canada'],
    'Salary': [94732, 61284, 56265, 66850, 87194]
}

df = pd.DataFrame(data)

# 1.막대 그래프
average = df.groupby('Country')['Salary'].mean()
average.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Average Salary')
plt.show()

# 2.산점도
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()





##2번 문제
from PIL import Image

with open('list.txt', 'r') as f:
    lines = f.readlines()


directory_name = 'images/'

for line in lines:
    filename = directory_name + line.strip()
    img = Image.open(filename)

    
    image_number = int(line.split('.')[0][-1])

    # 짝수 번호라면 30도 회전
    if image_number % 2 == 0:
        rotate_img = img.rotate(30, expand=True)
        rotate_img.save(filename.replace('dog', 'rot30_dog'))
    # 홀수 번호라면 crop
    else:
        width, height = img.size
        left = int(width * 0.1)
        upper = int(height * 0.2)
        right = int(width * 0.3)
        lower = int(height * 0.5)
        crop_img = img.crop((left, upper, right, lower))
        crop_img.save(filename.replace('dog', 'crop_dog'))
