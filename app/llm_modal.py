from langchain_ollama import OllamaLLM


def modal_init(modal_name: str = None, url: str = None):
    name = "llama3.1"
    modal_url = "192.168.31.96:11434"

    # if url:
    #     modal_url = url
    # if modal_name:
    #     name = modal_name
    print(name, modal_url)
    return OllamaLLM(model=name, base_url=modal_url)
