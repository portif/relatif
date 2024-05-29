# relestagio

Rascunho de documentação para relatório de estágio.

## Ambiente virtual

1. `python3 -m venv .venv`
2. `source ./.venv/bin/activate`
3. `pip3 install -r requirements.txt`

## Versão HTML

Para gerar a documentação no formato HTML, há duas opções de comando:

1. `mkdocs build`
2. `make html`

Se você está em fase de aprendizagem da escrita de documentação no formato Markdown, prefira o primeiro comando. Caso você já tenha mais experiência, tente o segundo comando.

Para visualizar a documentação gerada, use um dos seguintes comandos, a depender de sua escolha anterior:

1. `mkdocs serve`
2. `(cd docs/_build/html && python3 -m http.server)`

Posteriormente, acesse a URL: <http://localhost:8000>

## Versão PDF

Para gerar sua documentação no formato PDF, execute o comando:

- `make latexpdf`

E procure pelo arquivo PDF gerado[^1]. Se o comando anterior for concluído com sucesso, o arquivo estará disponível em: `docs` -> `_build` -> `latex`.

Caso ainda não tenha instalado o Latex, instale-o usando os comandos:

1. `sudo apt update`
2. `sudo apt install -y texlive-full`

[^1]: Experimente o comando `ls docs/_build/latex/*.pdf`