from transformers import AutoTokenizer, AutoModelForCausalLM
class Model:
    def __init__(self) -> None:
        pass 
    def load_model():
        model = AutoModelForCausalLM.from_pretrained("./models/llama_sql")
        return model 
    def load_tokenizer():
        tokenizer = AutoTokenizer.from_pretrained("./models/llama_sql")

