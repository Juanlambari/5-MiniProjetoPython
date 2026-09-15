from bibliotecas import pd, sns, np, plt, sm, px, go
from IPython.display import display, Markdown
from extracao_dados import df_churn

# Info sobre o Df todo
print(df_churn.info())

# Estatistica para variáveis númericas
print(df_churn.describe()) # churn tem número e aparece, mas ela é uma variável categórica

print("\nEstatistica variáveis categóricas:\n",df_churn.describe(include='object'))

# Gráfico - Versão Estátistica

# Conta os valores da coluna 'Churn'
churn_counts = df_churn['Churn'].value_counts().rename(index = {1: 'Sim', 0: 'Não'})

# Define as cores equivalentes ao gráfico original
cores = ['#636EFA', '#EF553B']

# Cria o gráfico de pizza com duas casas decimais
plt.figure(figsize = (6,6))
plt.pie(
    churn_counts.values,
    labels = churn_counts.index,
    autopct = '%1.2f%%', # <-- Duas casas decimais
    startangle = 140,
    colors = cores,
    explode = [0.05 if label == 'Sim' else 0 for label in churn_counts.index]
)
plt.title('Taxa de Churn Geral', fontsize = 14)
plt.show()

# Gráfico - Versão Interativa

# Calcula a contagem por categoria
churn_counts = df_churn['Churn'].value_counts()

# Cria o gráfico
fig_pie = px.pie(values = churn_counts.values,
                 names = churn_counts.index.map({1: 'Sim', 0: 'Não'}),
                 title = 'Taxa de Churn Geral',
                 color = churn_counts.index.map({1: 'Sim', 0: 'Não'}),
                 color_discrete_map = {'Sim': '#EF553B', 'Não': '#636EFA'}
                 )
fig_pie.show()

# Calculamos a taxa de churn
churn_counts = df_churn['Churn'].value_counts()
numerador = churn_counts.get(1, churn_counts.get('Sim', churn_counts.get(True, 0)))
taxa = 100 * numerador / len(df_churn)

print(f"\nA Taxa de Churn Geral é de: {taxa:.2f}%")

# Gráfico - Versão Estática

plt.figure(figsize = (12,4))

# Cria o gráfico de barras agrupadas com Seaborn
sns.countplot(data = df_churn,
              x = 'Tipo_Contrato',
              hue = 'Churn', # 
              palette = {0: '#636EFA', 1: '#EF553B'}
              )
plt.title('Taxa de Churn Por Tipo de Contrato', fontsize = 14)
plt.xlabel('\nTipo de Contrato')
plt.ylabel('Número de Clientes')
plt.legend(title = 'Churn (0=Não, 1=Sim)')
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()

# Gráfico - Versão Interativa

# Histograma
dsa_fig_bar_contrato = px.histogram(df_churn,
                                    x = 'Tipo_Contrato',
                                    color = 'Churn',
                                    barmode = 'group',
                                    title = 'Taxa de Churn por Tipo de Contrato',
                                    labels = {'Tipo_Contrato': 'Tipo de Contrato', 'Churn': 'Churn (0=Não, 1=Sim)'})
dsa_fig_bar_contrato.show()

# Gráfico - Versão Interativa

# Análise por Fidelidade (Tenure)
dsa_fig_hist_fidelidade = px.histogram(df_churn,
                                       x = 'Fidelidade_Meses',
                                       color = 'Churn',
                                       marginal = 'box',
                                       title = 'Distribuição de Fidelidade (em Meses) Por Churn',
                                       labels = {'Fidelidade_Meses': 'Meses de Fidelidade'})
dsa_fig_hist_fidelidade.show()

# Gráfico - Versão Interativa

# Análise por Fatura Mensal
dsa_fig_hist_fatura = px.histogram(df_churn,
                                   x = 'Fatura_Mensal',
                                   color = 'Churn',
                                   marginal = 'box',
                                   title = 'Distribuição da Fatura Mensal Por Churn',
                                   labels = {'Fatura_Mensal': 'Valor de Fatura Mensal'}
)
dsa_fig_hist_fatura.show()


servicosInternet_counts = df_churn['Servico_Internet'].value_counts()

fig_servicos = px.bar(df_churn,
                      x = 'Servico_Internet',
                      title = 'Serviços mais Cotados',
                      color_discrete_map = {'Algar': '#EF553B', 'DSL': '#636EFA', 'Não': '#111111'},
                      labels = {'Servico_Internet': 'Serviços de Internet'}
                      )

fig_servicos.show() # Não sei se deu certo ;-;