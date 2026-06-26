# 📈 Pipeline ETL de Dados Financeiros da B3

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Prefect](https://img.shields.io/badge/Orquestração-Prefect-brightgreen)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)
![Tests](https://img.shields.io/badge/Testes-5%20passed-brightgreen)

## 📖 Sobre o Projeto

Este projeto consiste na construção de um pipeline ETL para extração, transformação e armazenamento de dados financeiros obtidos por meio da API Alpha Vantage.

O pipeline coleta dados diários de ações selecionadas da B3, como PETR4 e VALE3, atualizando automaticamente a base de dados com informações de mercado. Após a extração, os dados passam por etapas de limpeza, padronização e organização em uma arquitetura de camadas (Raw, Trusted e Refined), garantindo rastreabilidade, qualidade e disponibilidade para análises, visualizações e futuras aplicações em Ciência e Engenharia de Dados.

---

## 🎯 Problema de Negócio

Instituições financeiras, analistas e empresas precisam de dados de mercado confiáveis e organizados para apoiar análises e tomadas de decisão. No entanto, consumir dados diretamente de APIs pode gerar desafios relacionados à padronização, qualidade e histórico das informações.

Este projeto automatiza o processo de ingestão e tratamento dos dados financeiros, preservando os dados originais, aplicando regras de qualidade e disponibilizando conjuntos de dados prontos para consumo analítico.

---

## 🛠️ Stack Utilizada

| Camada         | Tecnologia        |
| -------------- | ----------------- |
| Fonte de Dados | Alpha Vantage API |
| Linguagem      | Python 3.10+      |
| Orquestração   | Prefect           |
| Transformação  | Pandas            |
| Armazenamento  | Parquet e CSV     |
| Ambiente       | venv              |
| Versionamento  | Git e GitHub      |

---

## 🏗️ Arquitetura

O pipeline segue uma arquitetura em camadas, amplamente utilizada em projetos de Engenharia de Dados.

### 📂 Raw

Armazena os dados exatamente como foram retornados pela API, preservando a informação original sem qualquer modificação.

### 📂 Trusted

Contém os dados tratados, validados e padronizados, corrigindo tipos de dados, removendo inconsistências e preparando as informações para uso.

### 📂 Refined

Disponibiliza dados enriquecidos e agregados, prontos para análises, dashboards e aplicações de Ciência de Dados.

---

## 📂 Estrutura do Projeto

```text
pipeline-etl-b3/
│
├── data/
│   ├── raw/                 # Dados brutos extraídos da API
│   ├── trusted/             # Dados limpos e padronizados
│   └── refined/             # Dados prontos para análise
│
├── src/
│   ├── extract.py           # Extração dos dados
│   ├── transform.py         # Transformações
│   ├── load.py              # Escrita dos arquivos
│   └── utils.py             # Funções auxiliares
│
├── flows/                   # Fluxos de orquestração (Prefect)
├── notebooks/               # Exploração dos dados
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Fluxo do Pipeline

```text
Alpha Vantage API
        │
        ▼
Extração (Python)
        │
        ▼
Raw
        │
        ▼
Transformação (Pandas)
        │
        ▼
Trusted
        │
        ▼
Enriquecimento
        │
        ▼
Refined
        │
        ▼
Análises • Dashboards • Machine Learning
```

---

## ⚙️ Como Executar

> 🚧 Em construção.

---

## 📌 Funcionalidades

* Extração automática de dados financeiros da Alpha Vantage.
* Organização dos dados em arquitetura de camadas.
* Armazenamento em formatos CSV e Parquet.
* Limpeza e padronização dos dados.
* Estrutura preparada para automação com Prefect.
* Base pronta para análises e visualizações.

---

## 🚀 Próximas Melhorias

* Implementar agendamento automático com Prefect.
* Adicionar testes automatizados.
* Integrar armazenamento em banco de dados.
* Criar dashboard para visualização dos indicadores.
* Disponibilizar métricas de qualidade dos dados.

---

## 📊 Status

🚧 **Em desenvolvimento**

Novas funcionalidades serão adicionadas conforme a evolução do projeto.

---

## 👩‍💻 Autora

**Luiza Valéria dos Santos**

* Bacharela em Ciência da Computação
* Pós-graduanda em Ciência de Dados
* Interessada em Engenharia de Dados, Inteligência Artificial e Automação

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e composição de portfólio.
