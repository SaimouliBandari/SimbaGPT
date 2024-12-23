from langchain_ollama import OllamaLLM


def modal_init(modal_name:str = None, url:str = None):
    name = "llama3.1"
    modal_url = "192.168.31.96:11434"
    
    if modal_name is not None:
        name = modal_name
    if url is not None:
        modal_url = url
        
    return OllamaLLM(name=name, base_url=url)
    