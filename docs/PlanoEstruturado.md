# Documento de Análise para Expansão dos Laboratórios

## Índice

- [Documento de Análise para Expansão dos Laboratórios](#documento-de-análise-para-expansão-dos-laboratórios)
  - [Índice](#índice)
  - [1. Plano Estruturado para Análise](#1-plano-estruturado-para-análise)
      - [Entendimento da Dor e Lógica de Negócio](#entendimento-da-dor-e-lógica-de-negócio)
      - [Formulação do Problema](#formulação-do-problema)
      - [Revisão de Descobertas Anteriores](#revisão-de-descobertas-anteriores)
      - [Planejamento](#planejamento)
      - [Sanity Check dos Dados](#sanity-check-dos-dados)
      - [Definição de Premissas](#definição-de-premissas)
      - [Alinhamento de Hipóteses](#alinhamento-de-hipóteses)
      - [Entendimento Geral dos Dados](#entendimento-geral-dos-dados)
      - [Análise Guiada pelas Hipóteses](#análise-guiada-pelas-hipóteses)
      - [Sumarização dos Resultados](#sumarização-dos-resultados)
      - [Criação de Script Python](#criação-de-script-python)
      - [Apresentação Clara e Objetiva](#apresentação-clara-e-objetiva)
  - [2. Lógica de Negócio e Árvore de Problemas](#2-lógica-de-negócio-e-árvore-de-problemas)
      - [Pesquisa e Revisão de Descobertas Anteriores](#pesquisa-e-revisão-de-descobertas-anteriores)
      - [Árvore de Problemas](#árvore-de-problemas)
      - [Hipóteses para Validação](#hipóteses-para-validação)


---

## 1. Plano Estruturado para Análise

#### Entendimento da Dor e Lógica de Negócio
- O desafio central é identificar oportunidades estratégicas para expansão da rede laboratorial com foco em fidelização dos clientes, dado que gerar demanda nova é difícil.
- Entender a relevância do mercado de medicina diagnóstica, que é amplo e competitivo nos EUA.

#### Formulação do Problema
- **Objetivo:** Recomendar três áreas (ZCTAs) para instalação de novos laboratórios com base em potencial econômico, demográfico e de mercado (volume de exames e performance financeira).

#### Revisão de Descobertas Anteriores
- Pesquisa breve sobre fatores que tradicionalmente influenciam expansão e fidelização em serviços de saúde.
- Identificar benchmarks ou estudos similares anteriores relacionados ao mercado diagnóstico nos EUA.

#### Planejamento
- Definir quais dados serão necessários para atingir os objetivos.
- Estabelecer etapas e estratégias para validação e tratamento de dados.
- Decidir quais técnicas analíticas serão usadas.

#### Sanity Check dos Dados
- Analisar e validar formatos, tipos, valores ausentes e inconsistências (dados econômicos, demográficos, financeiros, e volumes de exames).
- Resumir problemas encontrados em uma tabela ou relatório claro.

#### Definição de Premissas
- Clientes fidelizados aumentam rentabilidade da rede.
- Características demográficas e econômicas têm forte relação com performance financeira dos laboratórios.
- Volumes históricos de exames refletem oportunidades futuras.

#### Alinhamento de Hipóteses
- Validar hipóteses relacionadas ao comportamento dos clientes (idade, frequência, recorrência).
- Explorar dados de desempenho financeiro e volume de exames relacionados a variáveis demográficas e econômicas.

#### Entendimento Geral dos Dados
- Realizar análise estatística descritiva (distribuições, correlações).
- Visualizar os dados por ZCTA para identificar padrões geográficos.

#### Análise Guiada pelas Hipóteses
- Relacionar variáveis demográficas e econômicas com dados financeiros e volumes de exames.
- Analisar segmentação clara por perfil regional e econômico.

#### Sumarização dos Resultados
- Preparar resumo claro e objetivo dos insights encontrados.
- Identificar claramente os padrões que suportem a recomendação das três ZCTAs escolhidas.

#### Criação de Script Python
- Construir código modular e documentado para automatizar as análises.
- Garantir que novos dados possam ser rapidamente incorporados e analisados sem esforço adicional significativo.

#### Apresentação Clara e Objetiva
- Expor claramente metodologia, justificativa para escolha das ZCTAs e suas limitações.
- Propor ações concretas para implementação da expansão com base na análise.
- Destacar claramente insights e decisões orientadas a dados.

---

## 2. Lógica de Negócio e Árvore de Problemas
Neste capítulo será aprofundado o entendimento sobre a lógica de negócios do mercado diagnóstico e o contexto de expansão e fidelização.

#### Pesquisa e Revisão de Descobertas Anteriores
- **Crescimento do Mercado de Diagnóstico por Imagem:** Estima-se que o mercado de diagnóstico por imagem nos EUA registre um crescimento anual composto (CAGR) de aproximadamente 6,0% durante o período de previsão. Esse crescimento é impulsionado por avanços tecnológicos e pelo aumento da conscientização sobre cuidados preventivos.
- **Tendências em Diagnósticos Clínicos:** O mercado de diagnósticos clínicos nos EUA está projetado para atingir US$ 84,18 bilhões em 2024, com um crescimento contínuo impulsionado pela demanda por diagnósticos precisos e rápidos.
Fonte: [Mordor Intelligence](https://www.mordorintelligence.com/pt/industry-reports/clinical-diagnostic-market)

#### Árvore de Problemas

**Problema Principal:** Escolha das melhores 3 ZCTAs para expansão dos laboratórios  
│  
├── **Potencial Econômico/Demográfico**
│   ├── Alta densidade populacional  
│   ├── População com perfil etário propenso a exames frequentes (idosos, portadores de doenças crônicas)  
│   └── Alto poder aquisitivo da população  
│  
├── **Performance e Demanda Atual de Exames**
│   ├── Histórico elevado no volume de exames diagnósticos na região  
│   ├── Forte tendência de crescimento na procura por exames laboratoriais  
│   └── Região subatendida (baixa concorrência local, mas alta demanda percebida)  
│  
├── **Concorrência Local**
│   ├── Baixa concorrência direta de outros laboratórios  
│   └── Pouca fidelização de clientes em relação aos concorrentes atuais (oportunidade de entrada)  
│  
├── **Logística e Acessibilidade**
│   ├── Fácil acesso físico à região (vias rápidas, transporte público, estacionamento disponível)  
│   └── Facilidade logística para transporte de materiais biológicos e resultados  
│  
└── **Aspectos Estratégicos**
    ├── Oportunidades de parceria com médicos e clínicas locais  
    ├── Possibilidade de fidelização rápida dos clientes (estratégias digitais e CRM)  
    └── Região estratégica para presença e reconhecimento da marca

#### Hipóteses para Validação
Baseado na árvore de problemas levantada, essas são as hipóteses para serem validadas.

**H1 – Potencial Econômico e Demográfico**
- **H1a:** ZCTAs com maior densidade populacional têm maior volume de exames realizados

- **H1b:** ZCTAs com maior renda média têm maior gasto médio por paciente

- **H1c:** ZCTAs com maior proporção de população idosa (acima de 65 anos) têm maior frequência de utilização dos serviços laboratoriais

- **H1d:** ZCTAs com maior proporção de mulheres têm maior frequência de utilização dos serviços laboratoriais

**H2 – Performance Atual de Exames**
- **H2a:** ZCTAs com maior número de exames realizados nos últimos anos indicam maior potencial futuro.

- **H2b:** Exames com maior custo operacional têm relação direta com receita e lucro mais altos para a rede.

- **H2c:** *(Consequencia da exporação dos dados)* ZCTAs com alta proporção de mulheres podem ser estratégicos para expansão, especialmente considerando que os exames mais rentáveis da rede são voltados à saúde feminina.

**H3 – Concorrência e Saturação de Mercado**
- **H3a:** ZCTAs com menos laboratórios concorrentes têm maior potencial para expansão da rede.

- **H3b:** ZCTAs com alto volume de exames realizados em relação à quantidade de laboratórios existentes representam uma oportunidade estratégica de expansão.

> Obs: Hipóteses que poderiam ser consideradas prém avaliando os dados presentes, não foi possível tirar conclusões

**H4 – Logística e Acessibilidade**
- **H4a:** Laboratórios localizados em ZCTAs com melhores índices de acessibilidade (ex.: proximidade de vias principais, transporte público) possuem maior volume médio de exames realizados.

- **H4b:** ZCTAs com maior concentração urbana têm maior potencial de fidelização devido à facilidade logística para clientes.

> Obs: Mesmo caso das hipóteses em H3

**H5 – Aspectos Estratégicos e de Fidelização**
- **H5a:** ZCTAs que apresentam maior diversidade de exames realizados demonstram maior fidelização dos pacientes.

- **H5b:** Pacientes em ZCTAs com maior recorrência anual de exames indicam maior fidelização e retorno financeiro previsível.

**Metodologia para validação das hipóteses:**
- Análise exploratória com visualizações.

- Análise estatística descritiva e inferencial para validar diferenças significativas entre grupos.

- Aplicação de modelos preditivos simples para relacionar variáveis demográficas/econômicas com volume e receita gerada.
