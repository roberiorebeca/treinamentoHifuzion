# Utilizando o pipenv

## Instalação

Para instalar o pipenv utilize o comando

```bash
pip install pipenv
echo 'export PIPENV_VENV_IN_PROJECT=1' >> ~/.bashrc
source ~/.bashrc
```

## Utilização

Entre na pasta do projeto e inicie com o seguinte comando.

```bash
pipenv run
```

Agora, instale as libs com os seguintes comandos

```bash
pipenv install django
```

Para instalar a dependencia como desenvolvimento, utilize

```bash
pipenv install sqlformatter -d
```

Para instalar as dependencias de um projeto já existente (PipFile), utilize

```bash
pipenv sync
```

Caso queira instalar as dependencias de desenvolvimento também

```bash
pipenv sync -d
```
