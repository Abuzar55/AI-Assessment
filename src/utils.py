import random

def sql_get_category(n):
    list_of_categories = [
        "Explain/Analyze a Query Questions",
        "Explain SQL Concepts (differences/use cases)",
        "Debugging a Query Questions",
        "Optimization Discussion",
        "Design a Query",
        "Scenario-Based Questions", 
        "Handling Specific Data Challenges(What if questions)"
    ]
    
    # Choose n number of categories randomly
    selected_categories = random.sample(list_of_categories, n)
    
    return " and ".join(selected_categories)

def statistics_get_category(n):
    list_of_categories = [
        "Explain/Analyze a Statistical Concept or Result",
        "Explain Statistical Differences/Use Cases",
        "Statistical Application Problems",
        "Optimization Discussion",
        "Scenario-Based Questions", 
        "Handling Specific Data Challenges(What if questions)"
    ]
    
    # Choose n number of categories randomly
    selected_categories = random.sample(list_of_categories, n)
    
    return " and ".join(selected_categories)

def python_get_categories(n):
    list_of_categories = [
        "Explain/Analyze a Code Snippet",
        "Explain Python Concepts (Differences/Use Cases)",
        "Debugging a Code Snippet",
        "Optimization Discussion",
        "Scenario-Based Questions", 
        "Handling Specific Data Challenges(What if questions)"
    ]
    
    # Choose n number of categories randomly
    selected_categories = random.sample(list_of_categories, n)
    
    return " and ".join(selected_categories)

def ml_categories(n):
    list_of_categories = [
        "Explaining/Analyzing a Machine Learning Algorithm",
        "Explain Machine Learning Concepts (Differences/Use Cases)",
        "Scenario-Based Machine Learning Problems", 
        "Handling Specific Data Challenges in Mahcine Learning (What if questions)"
    ]
    
    # Choose n number of categories randomly
    selected_categories = random.sample(list_of_categories, n)
    
    return " and ".join(selected_categories)

def categories(skill_name, number_of_questions):
    if "sql" in skill_name:
        return sql_get_category(n=number_of_questions)
    if "statistics" in skill_name:
        return statistics_get_category(n=number_of_questions)
    if "python" in skill_name:
        return  python_get_categories(n=number_of_questions)
    if "ml" in skill_name:
        return ml_categories(n=number_of_questions)

# def post_processing(questions):    
#     sql_questions = []
#     python_questions = []
#     statistics_questions = []
#     ml_questions = []

#     for section in questions:
#         if "sql_questions" in section:
#             sql_questions.extend(section["sql_questions"])
#         elif "python_questions" in section:
#             python_questions.extend(section["python_questions"])
#         elif "statistics_questions" in section:
#             statistics_questions.extend(section["statistics_questions"])
#         elif "ml_questions" in section:
#             ml_questions.extend(section["ml_questions"])

#     # Adding necessary fields for SQL questions if not present
#     for sql_question in sql_questions:
#         sql_question["skill"] = "sql"
#         if "Query" not in sql_question:
#             sql_question["Query"] = ""
#         if "Database Schema and Table" not in sql_question:
#             sql_question["Database Schema and Table"] = ""
#         if "Topics Covered" not in sql_question:
#             sql_question["Topics Covered"] = ""
#         if "Answer Type" not in sql_question:
#             sql_question["Answer Type"] = ""
#         if "Estimated Time to solve" not in sql_question:
#             sql_question["Estimated Time to solve"] = ""
#         if "Grading criteria parameters" not in sql_question:
#             sql_question["Grading criteria parameters"] = ""

#     # Adding necessary fields for Python questions if not present
#     for python_question in python_questions:
#         python_question["skill"] = "python"
#         if "Code Snippet" not in python_question:
#             python_question["Code Snippet"] = ""
#         if "Topics Covered" not in python_question:
#             python_question["Topics Covered"] = ""
#         if "Answer Type" not in python_question:
#             python_question["Answer Type"] = ""
#         if "Estimated Time to solve" not in python_question:
#             python_question["Estimated Time to solve"] = ""
#         if "Grading criteria parameters" not in python_question:
#             python_question["Grading criteria parameters"] = ""

#     for stat_question in statistics_questions:
#         stat_question["skill"] = "statistics"
#         if "Topics Covered" not in stat_question:
#             stat_question["Topics Covered"] = ""
#         if "Answer Type" not in stat_question:
#             stat_question["Answer Type"] = ""
#         if "Estimated Time to solve" not in stat_question:
#             stat_question["Estimated Time to solve"] = ""
#         if "Grading criteria parameters" not in stat_question:
#             stat_question["Grading criteria parameters"] = ""

#     for ml_question in ml_questions:
#         stat_question["skill"] = "Machine Learning"
#         if "Topics Covered" not in ml_question:
#             ml_question["Topics Covered"] = ""
#         if "Answer Type" not in ml_question:
#             ml_question["Answer Type"] = ""
#         if "Estimated Time to solve" not in ml_question:
#             ml_question["Estimated Time to solve"] = ""
#         if "Grading criteria parameters" not in ml_question:
#             ml_question["Grading criteria parameters"] = ""

#     # Creating separate dictionaries for SQL, Python, and Statistics questions
#     processed_questions = {}
#     if sql_questions:
#         processed_questions["sql_questions"] = sql_questions
#     if python_questions:
#         processed_questions["python_questions"] = python_questions
#     if statistics_questions:
#         processed_questions["statistics_questions"] = statistics_questions
#     if ml_questions:
#         processed_questions["ml_questions"] = ml_questions
    
#     return processed_questions


# def post_processing(questions):    
#     processed_questions = []

#     for section in questions:
#         if "sql_questions" in section:
#             for sql_question in section["sql_questions"]:
#                 sql_question["skill"] = "sql"
#                 processed_questions.append(sql_question)
#         elif "python_questions" in section:
#             for python_question in section["python_questions"]:
#                 python_question["skill"] = "python"
#                 processed_questions.append(python_question)
#         elif "statistics_questions" in section:
#             for stat_question in section["statistics_questions"]:
#                 stat_question["skill"] = "statistics"
#                 processed_questions.append(stat_question)
#         elif "ml_questions" in section:
#             for ml_question in section["ml_questions"]:
#                 ml_question["skill"] = "Machine Learning"
#                 processed_questions.append(ml_question)

#     return processed_questions

def post_processing(questions):    
    processed_questions = []

    for section in questions:
        if "sql_questions" in section:
            for sql_question in section["sql_questions"]:
                sql_question["skill"] = "sql"
                add_missing_keys(sql_question, ["Query", "Database Schema and Table", "Topics Covered", "Answer Type", "Estimated Time to solve", "Grading criteria parameters"])
                processed_questions.append(sql_question)
        elif "python_questions" in section:
            for python_question in section["python_questions"]:
                python_question["skill"] = "python"
                add_missing_keys(python_question, ["code_snippet", "Topics Covered", "Answer Type", "Estimated Time to solve", "Grading criteria parameters"])
                processed_questions.append(python_question)
        elif "statistics_questions" in section:
            for stat_question in section["statistics_questions"]:
                stat_question["skill"] = "statistics"
                add_missing_keys(stat_question, ["Topics Covered", "Answer Type", "Estimated Time to solve", "Grading criteria parameters"])
                processed_questions.append(stat_question)
        elif "ml_questions" in section:
            for ml_question in section["ml_questions"]:
                ml_question["skill"] = "ml"
                add_missing_keys(ml_question, ["Topics Covered", "Answer Type", "Estimated Time to solve", "Grading criteria parameters"])
                processed_questions.append(ml_question)

        for question in processed_questions:    
            question['difficulty'] = normalize_difficulty(question['difficulty'])

    return processed_questions

def add_missing_keys(question, keys):
    for key in keys:
        if key not in question:
            question[key] = ""

def normalize_difficulty(difficulty):
    if difficulty.lower() in ['easy', "entry"]:
        return 'easy'
    elif difficulty.lower() in ['medium', 'intermediate', "mid"]:
        return 'medium'
    elif difficulty.lower() in ['hard', 'advanced']:
        return 'hard'
    else:
        return difficulty  # In case there are unexpected values