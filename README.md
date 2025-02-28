# Robot Framework Requirement Coverage

## Introdução

Esta biblioteca ouvinte, gera relatórios sobre cobertura de requisitos para testes automatizados no Robot Framework. O relatório inclui:


## Recursos

- Identificação dos requisitos testados por meio de Tags
- Geração de um report HTML coverage_report.html.
- Adição de um sumário no console com informações da análise 
- Suporte a modo claro e escuro (Dark Mode).
- Barra de progresso visual indicando cobertura de testes.
- Falha na execução dos testes caso a cobertura mínima (caso informado) não seja atingida.
- Indicação dos requisitos testados, não testados e quantidade de testes por requisitos

## Instalação

Com pip:
```bash
pip install robotframework-reqcov
```

Com poetry:
```bash
poetry add robotframework-reqcov 
```

## Como Usar
1 - Crie um arquivo CSV com os requisitos, conforme o exemplo abaixo:

``` csv
ID,Descrição
REQ-001,Usuário pode criar conta
REQ-002,Usuário pode fazer login
```

2 - Adicionar tags nos testes para rastrear os requisitos

O `id` de cada requisito informado no arquivo csv, deverá ser utilizado como TAG nos testes relacionados.

   - Exemplo 1:
```
*** Test Cases ***
Criar Conta Com Sucesso
    [Tags]  REQ-001
    Criar Conta  usuario=teste@teste.com  
```

   - Exemplo 2:
```
*** Settings ***
Test Tag  REQ-001

*** Test Cases ***
Criar Conta Com Sucesso
    Criar Conta  usuario=teste@teste.com  
```

3 - Executar os testes e gerar o relatório de cobertura

3.1 - Sem cobertura mínima 
``` bash
robot -d reports --listener RobotRequirementsCovarege:""requirements.csv" .
```

3.2 - Com cobertura mínima 

``` bash
robot -d reports --listener RobotRequirementsCovarege:""requirements.csv":60 .
```

Por padrão, o arquivo de report `coverage_report.html` será adicionado no mesmo diretório onde os arquivos do Robot Framework serão adicionados.

## Vídeo

Veja o vídeo abaixo para mais informações:

*EM BREVE*

## Compatibilidade

-  [Robot Framework 7.0](https://pypi.org/project/robotframework/7.0/)
-  [Python 3](https://www.python.org/)


