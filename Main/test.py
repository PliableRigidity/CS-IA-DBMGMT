from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def hello_world():
   return render_template('index.html')
if __name__ == '__main__':
   app.run(debug = True)

# import pandas as pd
# import os
# from IPython.display import Image, display
# min = 104
# max = 107
# df = pd.read_csv('Doggo_Dataset.csv')
# # dd = df.to_dict(orient = 'records')
# filter = df[(df['ID']>= min) & (df['ID']<=max)]
# # print(filter['Breed'])
# names = filter['Breed']

# folder = 'Doggo_Pics'

# for name in names:
#     image_path=os.path.join(folder, f'{name}.jpeg')
#     display(Image(filename=image_path))
# %%
