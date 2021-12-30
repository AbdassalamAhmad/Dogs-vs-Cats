# Dogs-vs-Cats (validation accuracy 96%)

Predicting Dogs and Cats images using Xception pre-trained model from Keras library. It is reimplemented version from [HomeWork 8-deep learning](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/08-deep-learning) held by [DataTalksClub](https://datatalks.club/).

## Model Demo
![Model Demo](https://github.com/AbdassalamAhmad/Dogs-vs-Cats/blob/main/Dogs_VS_Cats.gif)

## About the Dataset
#### Data Source
I used the dataset from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats/data)

## Short Description of the Files
1. [dogs-vs-cats.ipynb](https://github.com/AbdassalamAhmad/Dogs-vs-Cats/blob/main/dogs-vs-cats.ipynb) - it's where the training happened (all the magic is here).
* used transfer learning to get Xception model pretrained on Imagnet.
* freeze its CNN layers and train the dense layers.
* used callbacks to save the best model over multiple epochs.
* did some data augmentation and dropout to prevent overfitting and generalize our model.
* Evalutaing the model, Aciheved 96% accuracy.

2. [dogs-vs-cats_app.py](https://github.com/AbdassalamAhmad/Dogs-vs-Cats/blob/main/dogs-vs-cats_app.py) It deploy the trained model to streamlit cloud.
3. [xception_v9_03_0.965.h5](https://github.com/AbdassalamAhmad/Dogs-vs-Cats/blob/main/xception_v9_03_0.965.h5) - Best model from training saved in this binary format to load it easily.
4. [Pipfile](https://github.com/AbdassalamAhmad/Dogs-vs-Cats/blob/main/Pipfile) and [Pipfile.lock](https://github.com/AbdassalamAhmad/Dogs-vs-Cats/blob/main/Pipfile.lock) - Python package dependencies, in the pipfile you can find all necessary librares and packages to be able to run the scripts with no problem.
5. [Homework8.ipynb]() - building a CNN from scatch and train it with data augmentation and solving the [homework](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/08-deep-learning/homework8.md).

## How to run this model and try it yourself
1. open this [link](https://share.streamlit.io/abdassalamahmad/dogs-vs-cats/main/dogs-vs-cats_app.py)
2. Upload an image from test dataset or any image from your device that has dog/s or cat/s.
Note: watch this [video](https://vimeo.com/661221067/11c9c1fc72) to see the model in action

## How to reproduce this model
1. Clone this repo to get all the code.
2. Download the dataset from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats/data)
3. Install pipenv -which is a packaging tool that will help installing all dependencies- , use this command on your terminal.
```py
pip install pipenv
```
4. Install all dependencies using pipenv by typing this command in your terminal **inside your cloned repo folder** 
```py
pipenv install
```
5. Deploying the app locally or on the web<br>
5.1. Locally: open the terminal and use this command
```py
streamlit run dogs_vs_cats_app.py.py
```
5.2. on the web: check the [documentation](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app) from official website.  


## Note
If you like my project, I appreciate you starring this repo. Please feel free to fork the content and contact me if you have any questions.

[my linkedIn account](https://www.linkedin.com/in/abdassalam-ahmad/)