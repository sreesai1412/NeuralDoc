# NeuralDoc

## Live Website

Our website is live at https://bit.ly/34HXMhv

## For Running Locally

Download trained models from https://drive.google.com/drive/folders/1V2wFX3pf9SGuN9YRQxNOCnebS3hI6PHz?usp=sharing and place it in ```/tmp``` and ```/tmp2``` folders.

Create python virtual environment, inside that

```
pip install -r requirements.txt

python setup.py develop

streamlit run app.py
```
should automatically open browser at localhost:8501

The ```tmp/code2jdoc.json``` and ```tmp2/code2jdoc.json``` contain code examples, predictions, ground truth references and bleu scores obtained during validation and testing.

You can give these on the website to check.
