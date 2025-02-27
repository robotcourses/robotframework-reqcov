# Robot Framework Requirement Coverage

O **Robot Framework Requirement Coverage** é uma biblioteca Ouvinte para realização de analise de cobertura de requisito para automações de testes criados com Robot Framework 7.x.

## Compatibilidade

-  [Robot Framework 7.0](https://pypi.org/project/robotframework/7.0/)
-  [Python 3](https://www.python.org/)


# Analise de Cobertura de Requisito
Por se tratar de um ouvinte, e não uma biblioteca de keywords, não é necessário instancia-la no seu projeto. De forma automatica e baseada nas tags presentes nos Test Cases e em uma CSV com os requisitos, o relatório será gerada.


Para que isso seja possível, é necessário incluir em um arquivo `*.csv` os requisitos que serão analisados.

```  csv
Requisito,Descrição
REQ-001,Requirement 1
```

Para facilitar a identificação dos requisitos/funcionalidades, no CSV os identificadores precisam começar com o prefixo "REQ-" seguido de uma numeração única entre requisitos/funcionalidades.

Após a criação do arquivo CSV, basta usar o identificador do requisitos/funcionalidades como TAG. Idealmente, sendo utilizado na configuração `Test Tag`, conforme abaixo.


``` robotframework
*** Settings ***
Test Tag  REQ-001
```

A biblioteca possui dois modos:

**MODO 1** - Realiza a analise e exibe a quantidade de requisitos cobertos de modo percentual e quantitativo

``` bash
robot -d reports --listener RobotRequirementsCovarege:".\example\requirements\requirements.csv" .\example\test\
```
![](docs/without_coverage_analysis.JPG)

**MODO 2** - Realiza, além da analise, a avaliação de um percentual mínimo de cobertura de testes, falhando a execução caso a cobertura não seja alcançada.

``` bash
robot -d reports --listener RobotRequirementsCovarege:".\example\requirements\requirements.csv":60.00 .\example\test\
```
![](docs/with_coverage_analysis_pass.JPG)

![](docs/with_coverage_analysis_fail.JPG)

Um arquivo CSV também será gerado e adicionado na pasta de Logs do Robot Framework

![](docs/covergae_csv_report.JPG)


**ATENÇÃO**: MANTENHA OS REQUISITOS ATUALIZADOS PARA QUE A ANALISE SE MANTENHA COESA.