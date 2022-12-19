# Modelos e API - Lyric Classification

Este projeto é parte do projeto de classificação do gênero de música através de sua letra.

Para acessar o Web Client, acessar o repositório pelo link: [Web Client](https://github.com/luccapuru/web_client_finch).

O projeto foi feito utilizando Python 3.10. Para instalar as bibliotecas utilizadas, executar

### `pip install -r requirements.txt`

As principais bibliotecas utilizadas são:

1. Pandas - manipulação do dataset e de arquivos .csv

2. scikit-learn - treinamento e avaliação dos modelos 

3. NLTK - tratamento de texto

4. Pickle - armazenamento dos modelos em .pkl 

5. Flask - construção da API 

No notebook [EDA.ipynb](https://github.com/luccapuru/lyric_classification_finch/blob/master/EDA.ipynb), tem-se a análise exploratória do dataset que pode ser encontrado nos arquivos .csv dentro da pasta [data](https://github.com/luccapuru/lyric_classification_finch/tree/master/data).

No notebook [Model.ipynb](https://github.com/luccapuru/lyric_classification_finch/blob/master/Model.ipynb), tem-se a extração de características, limpeza do dataset, treinamento e avaliação dos modelos, que são salvos em arquivos pickle (.pkl).

No script [pred_utils.py](https://github.com/luccapuru/lyric_classification_finch/blob/master/pred_utils.py), encontram-se as funções de extração de caraterísticas (extract_features), fazer predições (make_predicitions), abrir o modelo .pkl (open_model). 

No script [server.py](https://github.com/luccapuru/lyric_classification_finch/blob/master/server.py), é onde se encontra a API, que é hosteada localmente. 

## Modelos

Os modelos treinados foram armazenados em arquivos .pkl, porém devido ao seu tamanho, eles não puderam ser colocados neste repositório. Para acessá-los, entrar no link do [Google Drive](https://drive.google.com/file/d/1gHWTviIxHivjKidKffPqvA0V2Llg8JqC/view?usp=sharing)

## Instruções para executar o projeto

1. Para executar o projeto, executar o script server.py com:

### `python server.py`

2. E executar o [web client](https://github.com/luccapuru/web_client_finch) com:

### `npm start`

O endpoint só funciona com a API rodando localmente. 
