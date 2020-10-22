# NeuralDoc

Download trained model from https://drive.google.com/drive/folders/1V2wFX3pf9SGuN9YRQxNOCnebS3hI6PHz?usp=sharing and place it in ```/tmp``` folder.

Create python virtual environment, inside that

```
pip install -r requirements.txt

python setup.py develop

streamlit run app.py
```
should automatically open browser at localhost:8501

The ```tmp/code2jdoc.json``` contains code examples, predictions, ground truth references and bleu scores obtained during validation and testing.

You can give these on the website to check.
