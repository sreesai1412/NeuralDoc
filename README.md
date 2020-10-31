# NeuralDoc

Automating Source Code Documentation using Machine Learning

## Website

Our website is live at https://bit.ly/34HXMhv

## For Running Locally

Download the 2 pre-trained model files from https://drive.google.com/drive/folders/1V2wFX3pf9SGuN9YRQxNOCnebS3hI6PHz?usp=sharing and place the ```python2doc.mdl``` file in the ```/tmp_python``` folder and ```java2doc.mdl``` file in the ```/tmp_java``` folder.

Create python virtual environment and activate it
```
python3 -m venv nldoc

source nldoc/bin/activate 
```
Clone the repo
```
git clone 

cd NeuralDoc
```
Install requirements and run app
```
pip install -r requirements.txt

streamlit run app.py
```
should automatically open browser at localhost:8501

The JSON files in ```/tmp_python``` and ```/tmp_java``` folders contain code examples, predictions, ground truth references and bleu scores obtained during validation and testing.

These can be given on the website to check.
