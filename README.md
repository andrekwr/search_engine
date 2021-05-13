# Uma máquina de busca para fins didáticos.

André Weber

Matheus Pellizzon

## Conceitos atigindos
- [x] Limpeza dos dados
    - Arquivo: normalize.py **→** remove_punctuation, stemmer, punctuationCorrection, Clean_text
    - Remover URLs (foi utilizado o regex da fonte: https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url).
    - Remover algumas pontuações e caracteres especiais, exceto os símbolos "@" e "#".  
- [x] Normalização. Obs: Apenas aplicada no index e nas queries de busca para manter os tweets em sua forma original.
    - Stemming dos termos e das palavras dos documentos.
    - Lowercase em todas palavras.
- [x] Queries booleanas
    - Arquivo: query.py **→** parse_raw_query_or, parse_raw_query, parse_json_query, build_query
    - Parseamento de query user-friendly para mais baixo nível. Ex.: "not and safe" **→** ["and",  ["term", "not"], ["term", "safe"]]
- [x] Retrieval booleano
    - Arquivo: query.py **→** método Evaluate das classes.
- [x] Ranking tf-idf
    - Arquivo: rank.py **→** rank_documents, score_document_tf_idf, score_document
    - Classe Index utilizada para evitar erros no caso de não localizar uma palavra no index. 
- [x] Avançado: Enriquecimento de queries
    - Arquivo: query.py **→** parse_raw_query_or, parse_raw_query
    - A partir da query passada foi gerada uma nova com os sinônimos de cada termo. Ex.: "not and safe" **→** ["and", [or, ["term", "non"], ["term", not]], [or, ["term", "saf"], ["term", "good"]]]
    


## Instruções

- Faça um *fork* deste repositório para poder receber atualizações eventuais. Para saber como fazer um *fork*, veja https://docs.github.com/en/github/getting-started-with-github/fork-a-repo.

- Abra um terminal e vá para o diretório deste repositório.

- Rode `config.bat` (no Windows) ou `config.sh` (Linux/Mac) para colocar este diretório no `PYTHONPATH`.

- Abra seu ambiente de desenvolvimento (seu editor favorito, ou jupyter notebook, etc) a partir deste terminal para fazer uso da variável de ambiente `PYTHONPATH` atualizada.

Para gerar o corpo de documentos a partir do banco de dados utilizamos o comando:
```
python scripts/make_archive_from_elon_tweets.py data/elon.csv data/archive.json
```

Para gerar os índices de cada palavra:
```
python scripts/make_index_from_archive.py data/archive.json data/index.json
```

Para prosseguir com a procura dos termos nos documentos:
```
python scripts/search.py data/archive.json data/index.json queryDesejada
```


### Referência do banco de dados utilizado:
Tweets obtidos de https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021
