from langchain.chat_models import init_chat_model

def get_answer(msg: str) -> str:
    model = init_chat_model(model='gpt-4o-mini', model_provider='openai')
    response = model.invoke(msg)
    print(response)
    return response.content