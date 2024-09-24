# Explicação Desafio 02

## O que foi passado 
1) Tem uma imagem com 3 letras apontando para outras  letras 
2) também tem um texto provavelmente criptografado.
3) Também são dadas algumas dicas


## Resolução 

Imagino que o texto inicial esteja criptografado... testo inicial : 

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

### Tentativa 01: 
como ele passa as letras vou tentar trocar essas letras para ver se forma alguma palavra 

Resultado: 
G FMNC WMS BGBLR RPYLQJYRC GR ZW FYLB. RFYRQ UFYR AMMNSRCPQ YPC DMP. BMGLG GR GL ZW FYLB GQ GLCDDGAGCLR YLB RFYR'Q UFW RFGQ RCVR GQ QM JMLG. SQGLG QRPGLG.MYICRPYLQ() GQ PCAMMMCLBCB. LMU YNNJW ML RFC SPJ.

Nenhuma menssagem passou ou seja não funcionou 

### Tentativa 02: 
Vou tentar ver a incidência que as letras aparecem na frase e identificar qual letra poderia er uma vogal para ajudar a identificar outras possíveis letras

Obtive o seguinte resultado: {"'": 1,
 'V': 1,
 'I': 1,
 '(': 1,
 ')': 1,
 '\n': 2,
 'Z': 2,
 'U': 3,
 'A': 3,
 'D': 3,
 'N': 4,
 'S': 4,
 'J': 4,
 'W': 5,
 '.': 6,
 'B': 8,
 'P': 8,
 'F': 9,
 'C': 12,
 'Y': 12,
 'Q': 12,
 'M': 14,
 'L': 16,
 'R': 18,
 'G': 19,
 ' ': 36}

 A Letra que mais aparece é a letra G... Baseado na  lingua ingles provavelmente pode ser uma vocal como I ou E 

 ### Tentativa numero 03 
 Após perceber que a Letra G é uma das que mais aparece pensei em fazer a associação dela com a Letra I 

 Então veio a luz ... 

 G = I = G + 2 letras 
 |G|H|I|
 |-|-|-|
 |0|1|2| 

 K = M 
 |K|L|M|
 |-|-|-|
 |0|1|2| 

 O = Q
 E = G 

Sendo assim e se eu trocar todas as letras para as próximas duas letras 

Resultado = 
I"HOPE"YOU"DIDNT"TR[NSL[TE"IT"\Y"H[ND0"TH[TS"WH[T"COOPUTERS"[RE"FOR0"DOINI"IT"IN"\Y"H[ND"IS"INEFFICIENT"[ND"TH[T)S"WHY"THIS"TEXT"IS"SO"LONI0"USINI"STRINI0O[KETR[NS*+"IS"RECOOOENDED0"NOW"[PPLY"ON"THE"URL0

Apesar de já ser possível ler uma mensagem ainda precisa de ajustes 

### Tentativa numero  04 
Refazer a logica de pular duas casas mas agora somente se o carácter for uma letra 


Resultado : I HOPE YOU DIDNT TRANSLATE IT BY HAND. THATS WHAT COOPUTERS ARE FOR. DOINI IT IN BY HAND IS INEFFICIENT AND THAT'S WHY THIS TEXT IS SO LONI. USINI STRINI.OAKETRANS() IS RECOOOENDED. NOW APPLY ON THE URL.

Aqui pegou um pouco o fim do alfabeto... Por exemplo a Letra Y na Tabela Asc é a 89 o problema é que se eu somar + 2 ele iria pra 91 e o alfabeto só vai até os 90 

Então pra garantir que sempre seria uma letra apliquei a seguinte logica: 

A = 65 
Z = 90 

Tirar 65 por ser o menor numero ( equivalente ao A) 
assim 90 - 65 = 25 ( quantidade de letras ) 
assim 0 representa A,  representa B e assim por diante ...

Independente do valor eu aplico a soma de + 2 ou seja se o valor for 1 elevai pra 3 

Depois aplico novamente os valores de 65 ... porem antes tiro a sobra ... assim se uma letra for Y ou Z que são os finais ele aplica um reset na contagem e voltaria para 01 