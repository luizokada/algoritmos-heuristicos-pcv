# Algoritmos Heurísticos (PCV)

Algoritmos Heurísticos para obtenção de respostas viáveis ao Problema do Caixeiro Viajante.

Para executar o projeto em modo input:

`python3 ./main.py run`

Exemplo de input:


NAME : brd14051

COMMENT : BR Deutschland in den Grenzen von 1989 (Bachem/Wottawa)

TYPE : TSP

DIMENSION : 14051

EDGE_WEIGHT_TYPE : EUC_2D

NODE_COORD_SECTION

    1    2918    6528
    
    2    2925    6597
    
    3    2926    6609  
    
    4    2927    6312
    
    5    2930    6328
    
    6    2934    6545
    
EOF



As 6 primeiras linhas digitadas serao desconsideradas, pois o modelo do RUN.CODES exige esse padrão.

Os vértices devem respeitar o padrão: == indíce coordenada-x coordenada-y ==

Por fim, deve-se escrever `EOF` para terminar a leitura de inputs.

Para executar o projeto com as entradas de teste:

`python3 ./main.py tests`

