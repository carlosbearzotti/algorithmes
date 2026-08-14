# Importação das bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix
from xgboost import XGBClassifier
import shap

# ===========================
# 1. Carregar os dados
# ===========================
# Substitua 'dados.csv' pelo seu dataset
df = pd.read_csv('dados.csv')

# Exemplo de colunas
# df.columns -> ['idade', 'renda', 'historico_atraso', 'estado_civil', 'inadimplente']

# ===========================
# 2. Separar features e target
# ===========================
X = df.drop('inadimplente', axis=1)
y = df['inadimplente']

# ===========================
# 3. Identificar colunas numéricas e categóricas
# ===========================
num_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

# ===========================
# 4. Pré-processamento
# ===========================
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ]
)

# ===========================
# 5. Divisão treino/teste
# ===========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ===========================
# 6. Construir pipeline com XGBoost
# ===========================
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42))
])

# ===========================
# 7. Treinar modelo
# ===========================
pipeline.fit(X_train, y_train)

# ===========================
# 8. Avaliar modelo
# ===========================
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:,1]

print("ROC-AUC:", roc_auc_score(y_test, y_proba))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nMatriz de Confusão:\n", confusion_matrix(y_test, y_pred))

# ===========================
# 9. Interpretação com SHAP
# ===========================
# Extrair o modelo XGBoost do pipeline
model_xgb = pipeline.named_steps['classifier']

# Pré-processar dados de teste
X_test_processed = pipeline.named_steps['preprocessor'].transform(X_test)

# Explicações SHAP
explainer = shap.TreeExplainer(model_xgb)
shap_values = explainer.shap_values(X_test_processed)

# Plot resumo
shap.summary_plot(shap_values, X_test_processed, feature_names=num_features + list(pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out()))
