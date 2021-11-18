import streamlit as st
import pdfplumber
import nltk
import numpy as np
import pandas as pd
import altair as alt


st.set_page_config(page_title = 'MatchCV - Powered by FLAI',  
				   layout = 'centered', 
				   initial_sidebar_state = 'auto')

def MatchCV(textoCRU, vaga, limite = 3):
    '''
    textoCRU: texto extraido de um PDF
    vaga: dicionario de palavras-chave e pesos
    '''
    lista_de_palavras = nltk.tokenize.word_tokenize(textoCRU)  # transforma o texto cru em uma lista de termos
    lista_de_palavras = [palavra.lower() for palavra in lista_de_palavras]  # deixando tudo minusculo

    keywords = [palavra for palavra in lista_de_palavras if not palavra in stop_words and not palavra in pontuacao]  # tira as pontuacoes e stopwords 
    textocv = " ".join(s for s in keywords)  # junta tudo em um texto só novamente. 

    pesos = list(vaga['pesos'])
    palavras_chaves = list(vaga['palavras-chave'])

    cont = [textocv.count(pc) for pc in palavras_chaves]  # conta quantas vezes cada termo da vaga aparece no texto do cv

    def aux(x, limite):
        return x if x <= limite else limite

    cont = [aux(i, limite) for i in cont]   # coloca o limite na contagem de palavras

    pmax = np.sum(np.array(pesos) * limite) 

    score = ((np.array(cont) * pesos).sum()/pmax).round(4)

    return score


nltk.download('punkt')
nltk.download('stopwords')
pontuacao = ['(', ')', ';', ':', '[', ']', ',']
stop_words = nltk.corpus.stopwords.words('portuguese')
 
c1,c2 = st.columns((0.75,1))
c1.markdown('# **MatchCV FLAI**')
c2.image('https://www.flai.com.br/wp-content/uploads/2020/12/Its-time-to-flai_011.png', width=130)

st.markdown('## Otimizando a eficiência de RHs')
st.markdown('---')
st.markdown('## Carregue o PDF de um CV que você deseja analizar')

PDFs = st.file_uploader('O arquivo deve ter no máximo 10mb e ter a extenção ".pdf"',
				 type = ['pdf'],
				 accept_multiple_files = True)

st.markdown('## Carregue a planilha de requesitos principais da vaga')

vagasxlsx = st.file_uploader('O arquivo deve ter no máximo 10mb e ter a extenção ".xlsx"',
                 type = ['xlsx'],
                 accept_multiple_files = False)

if st.button('Carregar'):


    vagas = pd.read_excel(vagasxlsx, sheet_name = None)
    n_vagas = len(vagas.keys())
    nome_vagas = list(vagas.keys())
    vagas = [vagas[nome_vagas[i]] for i in range(n_vagas)]

    lista_de_cvs = []
    for arquivoPDF in PDFs:
        if arquivoPDF is not None:
            cv = pdfplumber.load(arquivoPDF)
            primeira_pagina = cv.pages[0]
            textoCRU = primeira_pagina.extract_text()
            lista_de_cvs.append(textoCRU)


    # Lista de Listas, cada lista interna é score de uma pessoa nas vagas
    
    pessoas = [[MatchCV(cv, vaga) for vaga in vagas] for cv in lista_de_cvs] 
    matchs = pd.DataFrame(pessoas, columns = nome_vagas)
    st.dataframe(matchs)
    #Mostrando o gráfico
    st.subheader("Gráfico do Score por tipo de vaga")
    st.bar_chart(matchs)

 