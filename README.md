# DESAFIO DIGESTO WEBSCRAPPING PYTHON

## Introdução

I desafio proposto pela empresa Digesto, consistiu em criar um crawler capaz de extrair as informações de dois sites, sendo eles da Vultr no 
com o site: https://www.vultr.com/products/cloud-compute/#pricing e o site da Digital Ocean, https://www.digitalocean.com/pricing. O principal 
objetivo do crawler, era retirar as informações das tabelas contidas no html disponibilizadas em seus sites, e tendo 3 opções de divulgação, sendo 
imprimir os dados obtidos, pondendo salvar em formato CSV, e no formato JSON.<br>

<br> No site da Vultr era extrair a informações da tabela abaixo:

![image](https://user-images.githubusercontent.com/48772900/120903966-be10f400-c61f-11eb-93e7-d95dedc924af.png)

Asinformações de interesse para o desafio era retirar os dados das colunas Storage, CPU, Memory, Bandwith e Price


<br> No site da Digital Ocean o objetivo era extrair as informações da tabela abaixo:

![image](https://user-images.githubusercontent.com/48772900/120904007-ff090880-c61f-11eb-8d2d-42a27cd5808a.png)

As informações de interesse para o desafio eram retirar os dados das colunas vCPU, Memory, SSD Disk, Transfer e Price.

## Requisitos básicos

O programa foi desenvolvido no sistema Linux Mint 19.1, com Python na versão 2.7.17, e foram utilizadas as seguintes bibliotecas:

+**pandas (0.24.2)**  - permite converter o data frame em dicionário<br>
+**lxml-4.6.3** - permite selecionar os elementos desejados pelo xpath e extrair os textos dentros deles<br>
+**requests-2.25.1** - para se conectar com as páginas e extrair o conteúdo html delas<br>
+ **json** - biblioteca padrão da linguagem
+ **os** - biblioteca padrão da linguagem
+ **sys** - biblioteca padrão da linguagem

## Modo de Execução do Crawler

Primeiro verifique se na sua máquina tenha o Python na versão especificada ou superior, e se foi instaladas as bibliotecas acima. 
Para instalação das bibliotecas no sistema Linux Mint 19.1 através dos seguintes comandos:
```
sudo pip install pandas
sudo pip install lxml
sudo pip install requests
```
Após instalado todas as bibliotecas, só executar o programa Desafio.py

![image](https://user-images.githubusercontent.com/48772900/120907109-59f92a80-c635-11eb-9e22-9e2965379bb8.png)


Após escolher a opção que deseja, deverá escolher qual dos sites deverá executar a extração

![image](https://user-images.githubusercontent.com/48772900/120907125-801eca80-c635-11eb-9021-d3b1373a2958.png)


