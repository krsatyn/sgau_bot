from transformers import pipeline

with open(r"D:\project\sgau_LLM\models\context.txt", "r", encoding="utf8") as file:
        context = file.read()


def get_model_request(request):
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
    context = context
    question = request
    qa_model(question = question, context = context)

    return(qa_model['answer'])
    
# print(qa_model)