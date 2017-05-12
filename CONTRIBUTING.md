# Como contribuir

Caso você não tenha conhecimentos sobre [git](https://git-scm.com/),
[virtualenv](https://virtualenv.pypa.io/),
[pelican](http://docs.getpelican.com/), [markdown](http://commonmark.org/) e
outras ferramentas que utilizamos no site, você ainda assim poderá contribuir
com publicações em nosso blog da seguinte forma:

- Crie uma conta no [GitHub](https://github.com/)
- [Crie uma issue no repositório do
  projeto](https://github.com/GruPyPR/grupypr.github.io/issues/new) contendo em
  sua descrição o texto da nova publicação e quaisquer outros arquivos em anexo
  (como fotos).
- Espere que algum membro do projeto revise sua publicação e a inclua no
  projeto.

Caso você já conheça essas ferramentas (ou queira aprender a usá-las), continue
lendo.


## Baixando e instalando o projeto

Você precisa ter Python 3, git e make instalados em seu sistema. Os comandos
abaixo funcionarão em sistemas UNIX-like (GNU/Linux, MAC OS X, FreeBSD etc.) -
caso utilize Windows, algumas alterações precisam ser feitas.

1. Faça um [fork](https://github.com/GruPyPR/grupypr.github.io/fork) do
   projeto em sua conta no GitHub.
2. Clone o fork em sua máquina:
   -  `git clone git@github.com:SEU-USARIO/grupypr.github.io.git`
3. Crie um virtualenv dentro do repositório do projeto:
   - `cd grupypr.github.io`
   - `virtualenv --python=$(which python3) .venv`
4. Ative o virtualenv:
   - `source .venv/bin/activate`
5. Instale as dependências do projeto:
   - `pip install -r requirements.txt`
6. Carregue o repositório do tema:
   - `git submodule init`
   - `git submodule update`


## Rodando o projeto

1. Acesse o diretório do projeto:
   - `cd grupypr.github.io`
2. Ative o virtualenv:
   - `source .venv/bin/activate`
3. Gere os arquivos estáticos e rode o servidor HTTP do
   [pelican](http://docs.getpelican.com/):
   - `make up`
4. Acesse [localhost:8000](http://localhost:8000/) em seu navegador.


## Criando publicações e outras contribuições

1. Crie uma branch para as contribuições que deseja fazer:
   - `git checkout -b NOME-DO-BRANCH`
2. Realize as contruibuições (caso seja uma publicação no blog, veja abaixo os
   passos). :)
3. Adicione os arquivos que você criou/alterou para o commit:
  - `git add arquivo1 arquivo2 ... arquivoN`
4. Realize o commit para gravar as alterações no histórico do repositório:
  - `git commit -m "Coloque aqui uma mensagem explícita sobre as alterações"`
5. Envie as alterações para seu repositório remoto:
  - `git push origin NOME-DO-BRANCH`
6. [Crie um pull request no repositório do GruPyPR no
   GitHub](https://github.com/GruPyPR/grupypr.github.io/compare).

Para criar uma publicação no blog:

1. Adicione o arquivo com a publicação em `content/ANO/ANO-MES-DIA-titulo.md`,
   com o conteúdo em [markdown](http://commonmark.org/). Utilize como base os
   arquivos que estão em `content/2017`;
2. Adicione fotos em `content/images/` com o nome `ANO-MES-DIA-titulo.jpg` e
   suas respectivas miniaturas (as miniaturas devem conter no máximo 600px de
   largura) em `content/images/thumbnail/`.

> Dica: caso sejam muitas alterações, divida-as em diversos commits, isso
> facilitará o trabalho de quem for revisar suas alterações. :)


## Mantendo seu fork atualizado

O repositório oficial do site (upstream) será sempre atualizado com
contribuições de diversos membros e, com isso, o repositório de seu fork pode
ficar desatualizado. É importante atualizá-lo com as últimas alteraçoes do
upstream para que você possa fazer contribuições com base no código mais novo
disponível. Siga os seguintes passos para atualizar seu fork:

1. Acesse o diretório do projeto:
   - `cd grupypr.github.io`
2. Adicione um remote que aponte para o repositório de origem:
   - `git remote add upstream https://github.com/GruPyPR/grupypr.github.io.git`
3. Baixe as alterações do remote upstream:
   - `git fetch upstream`
4. Acesse a branch src local:
   - `git checkout src`
5. Faça o merge da branch src do upstream com o seu repositório local:
   - `git rebase upstream/src`
6. E finalmente, salve as alterações no seu repositório remoto:
   - `git push`
