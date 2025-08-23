# Passo 1: Configurar o acesso ao Azure Blob Storage

storage_account_name = "storagenamehere"
container_name = "containernamehere"
sas_token = "?sastokenhere"
file_name = "student-mat.csv"

# Definir o caminho para o arquivo no Azure
file_path = f"wasbs://containernamehere@storagenamehere.blob.core.windows.net/student-mat.csv"

# Configurar as credenciais do Azure Blob Storage para o Spark
spark.conf.set(
  f"fs.azure.sas.containernamehere@storagenamehere.blob.core.windows.net",
  sas_token
)

print("Credenciais do Azure Blob Storage configuradas com sucesso!")

# Passo 2: Importar as bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("Bibliotecas importadas com sucesso!")

# Passo 3: Carregar o conjunto de dados usando o Spark (Solução do problema)
# Usar o conector nativo do Spark para ler o arquivo
try:
    spark_df = spark.read.csv(file_path, header=True, sep=';', inferSchema=True)
    print("\nDados carregados com sucesso usando Spark!")
    
    # Converter o Spark DataFrame para um Pandas DataFrame
    df = spark_df.toPandas()
    print("Dados convertidos para Pandas DataFrame.")
    print("Visão geral dos dados:")
    print(df.head())
except Exception as e:
    print(f"\nErro ao carregar os dados: {e}")

# O resto do código só será executado se o passo 3 for bem-sucedido
if 'df' in locals():
    # Passo 4: Preparar os dados para o modelo de ML
    features = ['age', 'studytime', 'failures', 'absences', 'G1', 'G2']
    target = 'G3'
    X = df[features]
    y = df[target]

    # Passo 5: Dividir os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(f"\nDados divididos: {len(X_train)} amostras para treino, {len(X_test)} para teste.")

    # Passo 6: Construir e treinar o modelo de Regressão Linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    print("\nModelo de Regressão Linear treinado com sucesso!")

    # Passo 7: Fazer previsões e avaliar o modelo
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"\nDesempenho do Modelo:")
    print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
    print(f"Coeficiente de Determinação (R2): {r2:.2f}")

    # Passo 8: Exemplo de previsão para um novo aluno
    # Crie um DataFrame com os dados de um novo aluno (as colunas devem ser as mesmas usadas no treino)
    novo_aluno = pd.DataFrame([[17, 2, 0, 5, 10, 11]], columns=features)
    previsao_nota = model.predict(novo_aluno)

    # Aplicar o limite: garantir que a previsão esteja entre 0 e 20
    nota_final_corrigida = max(0, min(20, previsao_nota[0]))

    print(f"\nA previsão da nota final para o novo aluno é: {nota_final_corrigida:.2f}")

