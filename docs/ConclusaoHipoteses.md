# ✅ Conclusões das Hipóteses para Validação

Baseado na árvore de problemas levantada, essas são as hipóteses avaliadas com base nos dados disponíveis.

---

## H1 – Potencial Econômico e Demográfico

### H1a: ZCTAs com maior densidade populacional têm maior volume de exames realizados
- ✅ **Suportada.**
- Correlação de **0.73** entre população total e volume de exames.
- Gráfico mostra clara tendência positiva.
- População total se mostra um excelente proxy de densidade.

### H1b: ZCTAs com maior renda média têm maior gasto médio por paciente
- ❌ **Não suportada.**
- Nenhuma correlação relevante encontrada.
- Gráfico mostra dispersão considerável sem padrão claro.

### H1c: ZCTAs com maior proporção de população idosa (65+) têm maior uso dos serviços laboratoriais
- 🟡 **Parcialmente suportada.**
- Correlação com número absoluto de idosos foi **0.60**, mas perdeu significância em regressão múltipla quando ajustado por população total.
- População total é melhor preditor do volume.

### H1d: ZCTAs com maior proporção de mulheres têm maior uso dos serviços laboratoriais
- ❌ **Não suportada.**
- Correlação próxima de zero.
- Dados não indicam maior volume de exames em regiões com mais mulheres.

---

## H2 – Performance Atual de Exames

### H2a: ZCTAs com maior número de exames realizados nos últimos anos indicam maior potencial futuro
- ✅ **Suportada.**
- ZCTAs como `94565`, `95823` e `30096` mantêm volumes elevados e consistentes ao longo do tempo.
- Gráficos temporais indicam estabilidade e retomada pós-pandemia.

### H2b: Exames com maior custo operacional têm relação direta com receita e lucro mais altos para a rede
- ✅ **Suportada com simulação.**
- Utilizando markup de 2.5x, observou-se que exames com custo mais alto geram maior receita estimada.
- Exames femininos dominam o ranking de rentabilidade.

### H2c: ZCTAs com alta proporção de mulheres podem ser estratégicos para expansão, dado o potencial dos exames mais rentáveis
- ✅ **Suportada como insight emergente.**
- Apesar de não haver correlação direta com volume total, ZCTAs com público majoritariamente feminino concentram a aplicação de exames rentáveis.
- Pode representar **potencial estratégico não evidente**.

---

## H3 – Concorrência e Saturação de Mercado

### H3a: ZCTAs com menos laboratórios concorrentes têm maior potencial para expansão da rede
- ⚠️ **Não avaliada.**
- Faltam dados sobre concorrência de outras redes.

### H3b: ZCTAs com alto volume de exames em relação à quantidade de laboratórios são oportunidades estratégicas
- ⚠️ **Não avaliada.**
- Apesar de termos os dados de localização da rede, não há dados completos de concorrentes.

> **Obs:** Hipóteses plausíveis, mas não foi possível tirar conclusões com os dados disponíveis.

---

## H4 – Logística e Acessibilidade

### H4a: ZCTAs com melhores índices de acessibilidade possuem maior volume médio de exames
- ⚠️ **Não avaliada.**
- Faltam dados de infraestrutura urbana, transporte público ou vias.

### H4b: ZCTAs com maior concentração urbana têm maior potencial de fidelização
- ⚠️ **Não avaliada.**
- Hipótese interessante, mas inviável com os dados atuais.

> **Obs:** Mesmo caso das hipóteses H3 — relevantes, mas requerem dados complementares.

---

## H5 – Aspectos Estratégicos e de Fidelização

### H5a: ZCTAs com maior diversidade de exames demonstram maior fidelização dos pacientes
- ✅ **Suportada.**
- Diversidade está altamente correlacionada ao volume total.
- ZCTAs com alta diversidade também concentram exames estratégicos.

### H5b: Pacientes em ZCTAs com maior recorrência anual de exames indicam maior fidelização e retorno financeiro previsível
- ❌ **Não suportada.**
- Apenas ~10% dos pacientes retornam em anos diferentes.
- ZCTAs com maior fidelização anual (ex: `19107`, `02019`) ainda têm baixa proporção de retorno.

---

