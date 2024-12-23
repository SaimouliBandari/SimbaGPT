from langchain_ollama import OllamaLLM


def get_modal(
    modal_name: str = None, url: str = None, connect_to_remote_modal: bool = True
):
    name = "llama3.1"
    modal_url = None

    if connect_to_remote_modal:
        modal_url = "192.168.31.96:11434"
    if url:
        # sets url of remote modal.
        modal_url = url
    if modal_name:
        name = modal_name
    print(name, modal_url)
    return OllamaLLM(model=name, base_url=modal_url)
