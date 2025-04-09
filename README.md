# 🧪 Strategic Expansion – Case de Laboratórios

Este projeto tem como objetivo identificar regiões estratégicas (ZCTAs) nos EUA com maior potencial para expansão de uma rede de laboratórios, utilizando dados transacionais, demográficos, econômicos e geográficos.

---

## 🚀 Como rodar o projeto

Este projeto utiliza [`uv`](https://github.com/astral-sh/uv) como gerenciador de ambiente Python e [`Docker`](https://www.docker.com/) para isolar todas as operações, tanto de análise quanto execução de pipeline.

### 🔧 Pré-requisitos

- Docker instalado
- uv (já empacotado dentro do container)

### 🧪 Ambiente Jupyter Lab

Para abrir o ambiente interativo:

```bash
docker compose up
```

Isso abrirá o Jupyter Lab com o notebook principal para exploração das hipóteses.

### ⚙️ Rodar a pipeline final

Para rodar a pipeline com o conjunto atual/novo de dados, execute:

```bash
docker exec -it labs uv run main.py
```

Isso irá executar a pipeline de forma automática e gerar a tabela final consolidada com os indicadores por ZCTA.

---

## 📚 Documentação do Projeto – Strategic Expansion

Esta pasta contém os arquivos `.md` com os resultados, hipóteses validadas e documentos de apoio da análise estratégica.

---

### 📄 Arquivos disponíveis

| Arquivo                             | Descrição |
|------------------------------------|-----------|
| `RecomendacoesZCTA.md`            | Conclusões finais com os 3 ZCTAs recomendados para expansão, com base nos critérios de volume, fidelização, demografia e diversidade de exames. |
| `ConclusaoHipoteses.md`  | Documento que reúne as validações (ou não) de todas as hipóteses formuladas no plano, com base nas análises executadas. |
| `PlanoEstruturado.md`              | Estrutura geral do plano de análise, contendo as hipóteses do case e os caminhos metodológicos adotados para investigação. |
| `README.md`                        | Arquivo principal com instruções para execução do projeto, uso do Docker/uv, fontes dos dados e estrutura da aplicação. |

---

## 🌐 Dados Geográficos

Os **polígonos geográficos dos ZCTAs** foram obtidos a partir do arquivo oficial:

> `tl_2024_us_zcta520.zip`

[Dados Originais](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2024&layergroup=ZIP+Code+Tabulation+Areas)

Devido ao tamanho elevado do arquivo original (1.5GB), foi realizado um pré-processamento no arquivo geojson para:

- Manter apenas os ZCTAs presentes no dataset transacional (com população > 10 mil)
- Reduzir drasticamente o tamanho final para ~20MB
- Gerar um arquivo leve: `zcta_subset.geojson`

Este arquivo é utilizado no módulo de visualização com **Folium** e permite geração de mapas interativos e rápidos.

---

## 📁 Estrutura

```
├── data/                  # Dados brutos e processados
├── docs/                  # Documentação detalhada dos processos
├── notebooks/             # Notebooks de análise por hipótese (H1, H2, ...)
├── src/                   # Módulos reutilizáveis e pipeline
│   └── zcta_pipeline.py   # Funções para construir a análise consolidada
├── reports/               # Mapas, gráficos e markdowns gerados
├── Dockerfile
├── docker-compose.yml
├── README.md
└── main.py                # Script final para executar a pipeline
```

---

## ✏️ Observações finais

- O projeto foi mantido 100% sob controle de ambiente via `uv` e `Docker`
- Todo o código é modularizado para reutilização em novos conjuntos de dados
- Os arquivos `.md` gerados podem ser usados em apresentações, relatórios e reuniões de negócio

