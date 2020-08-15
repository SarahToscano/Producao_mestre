# Plano Mestre de Produção

# Pesquisa Operacional - Projeto Final
## Especificação do Projeto

  Uma fábrica produz o produto final p1. A demanda por p1 para as próximas T
semanas é conhecida e dada por dt, t=1,...,T. 
  A fábrica dispõe de 800 horas semanais de mão-de-obra. A produção de 1 unidade 
de p1 exige 2 unidades do produto intermediário p2 e 3 do produto c1. 
  Por sua vez, a produção de 1 unidade do produto p2 exige 1 unidade do produto c1 
e 2 do produto c2. Os produtos p1 e p2 são produzidos na própria fábrica, 
cada unidade de p1 ou p2 produzida consome 1 hora de mão-de-obra. 
  Os produtos c1 e c2 são comprados externamente. Os custos de aquisição são de cc1 
e cc2 reais por unidade. Entretanto, cada pedido de compr a (que pode ser dos dois
produtos) tem um custo fixo de CF reais. 
   Todos os 4 tipos de produtos podem ser mantidos em estoque de uma semana para outra,
entretanto existe um custo de ep1, ep2, ec1, ec2 reais por unidade de estoque. O objetivo é
decidir para as T semanas o quanto vai ser produzido de cada produto p1 e p2 e quanto se 
vai comprar de c1 e de c2 de forma a atender todas as demandas e minimizar o custo
total com compras e estoques. Assuma que o estoque inicial de todos os produtos é zero.
   O programa deve fornecer a resposta completa: quanto vai ser produzido ou
comprado de cada produto em cada semana, qual o estoque de cada produto ao final
de cada semana e qual é o custo desse estoque.


### Instruções para arquivo de instância
    Os dados do arquivo de instância devem ser ordenados da seguinte forma:
    1. Número de Semanas;
    2. Cc1 (Custo de aquisição do produto C1);
    3. Cc2 (Custo de aquisição do produto C2);
    4. CF (Custo Fixo);
    5. ep1 (Custo para manter P1 no estoque);
    6. ep2 (Custo para manter P2 no estoque);
    7. ec1 (Custo para manter C1 no estoque);
    8. ec2 (Custo para manter  C2 no estoque);
    9. Demandas de P1 de acordo com as semanas;
    10. Horas semanais para mão-de-obra.
