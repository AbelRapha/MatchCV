# Match CV

## Ideia do projeto
Basicamente é uma forma de agilizar a leitura de currículos.
Por meio do processamento de linguagem natural (NLP) é encontrar as palavras chaves que estão dentro do currículo de cada cadidato, e dessa forma facilita o recrutamento, pois cada cadidato recebe um tipo de  __score__ para cada vaga. 
Sendo assim, agiliza o Match do CV para a vaga.
![Match_cv](Match%20CV.gif)

## Como utilizar esse projeto?
* Clone este repositório
* Baixe as bibliotecas necessárias em um ambiente virtual
* Crie um arquivo xlsx (Tipo excel) e em seguida uma tabela

palavras chave | pesos
:----------- | ----:
python | 2
power bi | 1
machine learning | 2
SQL | 2
Estatística | 2
conhecimento do negócio | 1

Isso para cada vaga, sendo assim, para cada tipo de vaga crie uma planilha nova dentro da planilha existente. Geralmente fica no canto inferior esquerdo do excel, libre office ou google sheets. O nome que irá aparecer na coluna será aquele que você nomeou na planilha.
### cria a virtual env
~~~~~python
python -m venv env
~~~~~
### ativa a virtual env
~~~~~python
.\env\scripts\activate 
~~~~~
### instala as bibliotecas
~~~~~python
pip install requirements 
~~~~~
### roda o programa em localhost
~~~~~python
streamlit run app.py 
~~~~~
## Tecnologias
* Python 3.9.7
* Nltk
* Streamlit 
* Pdfplumber
* numpy
* pandas

## Ideia do Projeto
[Imersão Flai DS](https://www.youtube.com/channel/UCbX5jWHGu-6_4CRhLmRuxcQ) 
