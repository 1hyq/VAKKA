# OpenAI配置
OPENAI_API_KEY = "your-api-key-here"
OPENAI_API_BASE = "https://api.openai.com/v1"  # 或您的自定义端点
GPT_MODEL = "gpt-4"

# BGE模型配置
BGE_MODEL_NAME = "BAAI/bge-large-en"  # Hugging Face模型ID
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"  # 自动检测GPU

# 路径配置
INPUT_DATA_PATH = "data/input/drug_names.csv"
OUTPUT_DESCRIPTIONS_PATH = "data/descriptions/drug_descriptions.json"
OUTPUT_EMBEDDINGS_PATH = "data/embeddings/drug_embeddings.npy"