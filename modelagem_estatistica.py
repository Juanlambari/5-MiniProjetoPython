from bibliotecas import pd, sns, np, plt, sm, px, go
from IPython.display import display, Markdown
from extracao_dados import df_churn

# Dados originais
print(df_churn.head())

# Categorias da variável
print("\n",df_churn.Tipo_Contrato.value_counts())

# Categorias da variável
print("\n", df_churn.Servico_Internet.value_counts())

# Preparação dos dados
# Converter variáveis categóricas em variáveis dummy (0 ou 1)
# Adicionando o parâmetro dtype=int para garantir que as novas colunas sejam númericas
df_model = pd.get_dummies(df_churn, columns = ['Tipo_Contrato', 'Servico_Internet'], drop_first = True, dtype = int)

# Dados processados
print("\n",df_model.head())

# Resumo dos dados
print("\n", df_model.info())

# Definiir as variáveis
# Variável dependente (o que queremos prever)
y = df_model['Churn']

# Variáveis independentes (as que usamos para prever)
# Excluímos a ID do cliente e a variável alvo original
X = df_model.drop(['ID_Cliente', 'Churn'], axis = 1)

# Adicionar uma constante (intercepto) ao modelo, exigido pela biblioteca statsmodels
X = sm.add_constant(X)

# Criamos o modelo
modelo = sm.Logit(y, X)
print(type(modelo))

# Treinamento do modelo
modelo_treinado = modelo.fit() # Precisasse de matematica para treinar esse modelos (alem de uma função framework)

# Exibir o resumo completo do modelo
print(modelo_treinado.summary())

"""
--- INTERPRETAÇAO ---
1. Coeficientes (coef) -> Mostra a direção do impacto,
Um coeficiente positivo aumenta a chance de churn(cancelamento), enquanto um negativo a diminui

2.Valor-p ( P>|z| ) -> Indica a significância estaatística de cada variável. Um valor-p baixo 
(geralmente < 0.05) significa que o efeito da variável é real e não apenas uma coincidência na amostra.

3. Pseudo R-squ -> Similar ao R² na regressão linear, indica a proporção da "variância" da variável dependente
que é explicada pelo modelo. Um valor de 0.645 (ou 65%)
é considerado um bom ajuste para este tipo de modelo.

--- ANOTAÇÃO ---
Razão de Chances (ou Odds Ratio) é uma medida usada para comparar a probalidade de um evento ocorrer entre dois grupos.
Ela é muito comum em estatísticas e modelos como a regressão logística.

De forma simples, a "chance" (odds) de um evento é a razão entre a probalidade de ele acontecer e a probabilidade de não acontecer.
Por exemplo, se a probabilidade de um cliente comprar um produto é 0,8 (80%), então a chance é 0,8 / 0,2 = 4.
Isso quer dizer que a chance de compra é 4 vezes maior do que a de não compra.
"""

# Calcular e exibir as razões de chance (Odds Ratios)
params = modelo_treinado.params
conf = modelo_treinado.conf_int()
conf['Odds Ratio'] = params
conf.colums = ['2.5%', '97.5%', 'Odds Ratio']
conf = np.exp(conf)
print(conf)

"""
--- INTERPRETAÇÃO ---

"""