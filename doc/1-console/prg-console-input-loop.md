#Первая программа с циклом.'

![if loop]({path-to-subject}/images/2.png)  
                
    print("Начало программы")
    lst = ["Как вас зовут?",
    "Какой ваш вес?",
    "Какой ваш рост?"]

    answers = []

    for i in lst: 
        print(i)
        answer = input()
        answers.append(answer)
        
    print("Конец программы")
    print(answers)            
                
![if loop]({path-to-subject}/images/3.png)                
                
                    
    print("Начало программы")
    lst = ["Как вас зовут?",
    "Какой ваш вес?",
    "Какой ваш рост?"]

    answers = []

    data = {'answers': answers, 'questions': lst}

    #data['answers'] = answers
    #data['questions'] = lst

    for i in data['questions']: 
        print(i)
        answer = input()
        data['answers'].append(answer)
        
    print("Конец программы")
    print(data)                
                    
                    
                    
                    
                
                
                
                
                
            
      
