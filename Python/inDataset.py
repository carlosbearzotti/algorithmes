import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix
from xgboost import XGBClassifier
import shap

# ===========================
# 1. Criar dataset de exemplo
# ===========================
np.random.seed(42)

n = 500  # número de clientes
df = pd.DataFrame({
    'idade': np.random.randint(18, 70, size=n),
    'renda': np.random.randint(1000, 10000, size=n),
    'historico_atraso': np.random.randint(0, 10, size=n),
    'estado_civil': np.random.choice(['solteiro', 'casado', 'divorciado'], size=n),
    'inadimplente': np.random.choice([0, 1], size=n, p=[0.8, 0.2])  # 20% inadimplentes
})

# ===========================
# 2. Separar features e target
# ===========================
X = df.drop('inadimplente', axis=1)
y = df['inadimplente']

num_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_features = X.select_dtypes(include=['object']).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ]
)

# ===========================
# 3. Divisão treino/teste
# ===========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ===========================
# 4. Pipeline com XGBoost
# ===========================
pipeline = Pipeline([
    ('preprocessor', preprocessor)
])

# ===========================
# 5. Treinar modelo
# ===========================
pipeline.fit(X_train, y_train)

# ===========================
# 6. Avaliar modelo
# ===========================
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:, 1]

print("ROC-AUC:", roc_auc_score(y_test, y_proba))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nMatriz de Confusão:\n", confusion_matrix(y_test, y_pred))

# ===========================
# 7. Interpretação com SHAP
# ===========================
model_xgb = pipeline.named_steps['classifier']
X_test_processed = pipeline.named_steps['preprocessor'].transform(X_test)
explainer = shap.TreeExplainer(model_xgb)
shap_values = explainer.shap_values(X_test_processed)
shap.summary_plot(shap_values, X_test_processed,
                  feature_names=num_features + list(pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out()))
