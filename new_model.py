from transformers import pipeline



def get_model_request(request):
    
    # старая версия
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
    with open(r"models\new_context.txt", "r", encoding="utf8") as file:
        context = file.read()

    print("подаю контекст")
    context = context
    question = request.lower()
    print("Обрабатываю запрос")
    answer = qa_model(question = question, context = context)
    
    return(answer['answer'])


 
if __name__ == '__main__':
    test_answer = get_model_request('гойда')
    print(test_answer)