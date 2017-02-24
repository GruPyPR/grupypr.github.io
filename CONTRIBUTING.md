# Como contribuir


## Baixando e instalando o projeto

1. Faça um [Fork](https://github.com/GruPyPR/grupypr.github.io/fork) do projeto.
2. Clone o fork criado utilizando a opção *--recursive*.
```
git clone git@github.com:SEU_USER/grupypr.github.io.git -—recursive
```
3. Acesse o diretório do projeto.
```
cd grupypr.github.io
```
4. Crie uma *virtualenv* para o projeto.
```
python -m venv .grupyprblog
```
5. Ative a *virtualenv*.
```
source .grupyprblog/bin/activate
```
6. Instale as dependências do projeto.
```
pip install -r requirements.txt
```

## Rodando o projeto
1. Acesse o diretório do projeto.
```
cd grupypr.github.io
```
2. Ative a *virtualenv*.
```
source .grupyprblog/bin/activate
```
3. Execute o Pelican
```
make up
```
4. Abra o navegador e acesse o endereço http://127.0.0.1:8000/

## Pull Requests
1. Crie uma branch para as contribuições que deseja fazer.
```
git checkout -b NOMEDABRANCH
```
2. Realize as contruibuições. :)
3. Adicione as contribuições para o commit.
```
git add .
```
4. Realize o commit. Seja explícito na mensagem de commit.
```
git commit -m "Mensagem bem explicadinha sobre o commit"
```
5. Salve as alterações no repositório remoto.
```
git push NOMEDABRANCH
```


## Mantendo o Fork atualizado
Para manter seu fork atualizado, basta seguir os passos:

1. Acesse o diretório do projeto.
```
cd grupypr.github.io
```
2. Adicione um remote que aponte para o repositório de origem.
```
git remote add upstream https://github.com/GruPyPR/grupypr.github.io.git
```
3. Baixe as alterações do remote upstream.
```
git fetch upstream
```
4. Acesse a branch src local.
```
git checkout src
```
5. Faça o merge da branch src do upstream com o seu repositório local.
```
git rebase upstream/src
```
6. E finalmente, salve as alterações no seu repositório remoto
```
git push
```
