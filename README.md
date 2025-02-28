# Robot Framework Requirement Coverage

- [🇺🇸 English](#English)
- [🇧🇷 Português](#Português)
- [📹 Vídeo](#video)

# Video

Veja o vídeo abaixo para mais informações / See the video below for more information:

# English
## Introduction

This listening library generates reports on requirements coverage for automated tests in the Robot Framework. The report includes:

## Features

- Identification of tested requirements through Tags
- Generation of an HTML report coverage_report.html.
- Addition of a summary in the console with analysis information
- Support for light and dark mode (Dark Mode).
- Visual progress bar indicating test coverage.
- Test execution failure if the minimum coverage (if informed) is not reached.  - Indication of tested and untested requirements and number of tests per requirement

## Installation

With pip:
```bash
pip install robotframework-reqcov
```

With poetry:
```bash
poetry add robotframework-reqcov
```

## How to Use
1 - Create a CSV file with the requirements, as shown in the example below:

``` csv
ID,Description
REQ-001,User can create account
REQ-002,User can log in
```

2 - Add tags to the tests to track the requirements

The `id` of each requirement reported in the csv file should be used as a TAG in the related tests.

 - Example 1:
```
*** Test Cases ***
Create Account Successfully
[Tags] REQ-001
Create Account user=test@test.com 
```

- Example 2:
```
*** Settings ***
Test Tag REQ-001

*** Test Cases ***
Create Account Successfully
Create Account user=test@test.com 
```

3 - Run the tests and generate the coverage report

3.1 - Without minimum coverage
``` bash
robot -d reports --listener RobotRequirementsCovarege:""requirements.csv" .
```

3.2 - With minimum coverage

``` bash
robot -d reports --listener RobotRequirementsCovarege:""requirements.csv":60 .  
```

By default, the report file `coverage_report.html` will be added in the same directory where the Robot Framework files will be added.

## Compatibility

- [Robot Framework 7.0](https://pypi.org/project/robotframework/7.0/)
- [Python 3](https://www.python.org/)



# Português
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

## Compatibilidade

-  [Robot Framework 7.0](https://pypi.org/project/robotframework/7.0/)
-  [Python 3](https://www.python.org/)
