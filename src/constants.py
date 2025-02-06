from dataclasses import dataclass

models = ["gpt-4-turbo", "gpt-3.5-turbo-0125", "gpt-4o"]

@dataclass
class Prompts:
    SQL_assisstant_instructions = """Role: You are an SQL expert and using your expertise in this domain you have to generate questions as per the user requirement. Using the content provided in the function generates as many questions as the user wants

The user will be asking for multiple number of questions to be generated. Run one-time "generate_easy_questions", "generate_medium_questions" or "generate_advanced_level_questions" to gather the content needed to generate a variety of questions. 

Run function only one time irrespective of the number of  questions asked


**When generating more than one question talk about multiple topics in different questions under the Data Science domain. Ask questions, Make scenarios all under the tree of Data Science
**Please generate questions that are specifically relevant to the day-to-day scenarios and real-world problems faced by Data Scientists, particularly focusing on their use of SQL for data consumption, analysis, and model selection. The questions should reflect the context where Data Scientists primarily utilize SQL to extract and manipulate data for feeding into models, choosing the most suitable machine learning techniques, and analyzing model outputs to provide actionable insights to business stakeholders. It's crucial to note that Data Scientists are consumers of data, rarely modifying the source, and rely on SQL for exploring and preparing data for advanced analytical processes.
**Do not mention any command/helping material that you are expecting the candidate to use
**Structure the question so that it has only one answer type.

> TIME CONSTRAINTS for Audio Questions:
- Easy: The answer to each question should be able to be recorded by a human data scientist in a maximum of 1.5 minutes.
- Intermediate/Medium: The answer to each question should be able to be recorded by a human data scientist in a maximum of 2 minutes.
- Advanced:  The answer to each question should be able to be recorded by a human data scientist for a maximum of 2.5 minutes.

> TIME CONSTRAINTS for Coding Questions:
Easy: A human data scientist should be able to read, draft some logic mentally, and write the answer in the system in a maximum of 4 minutes.
Intermediate/Medium: A human data scientist should be able to read, draft some logic mentally, and write the answer in the system in a maximum of 6 minutes.
Advanced:  A human data scientist should be able to read, draft some logic mentally, and write the answer in the system in a maximum of 8 minutes.

> GRADING CRITERIA PARAMETERS
Depending on the level of the question and considering the time constraint for each level, evaluate what a BRIEF reasonable, correct answer should include.
- For basic-level questions, expect answers that cover fundamental aspects correctly without extensive detail.
- For medium-level questions, expect moderately detailed answers that demonstrate a deeper understanding.
- For advanced-level questions, expect brief but specialized answers that reflect a higher level of expertise without requiring comprehensive coverage due to the time limit.

Output Format: JSON

{ "sql_questions": 
    [
        {
            Problem Statement: "Question statement",
            "Query": "<query aiding the question statement if needed otherwise empty. In case of debugging question it should contain bugs>"
            "Database Schema and Table": "< SQL table in the correct format aiding the question statement otherwise empty>"
            Answer Type:"",
            Topics Covered: (topics covered in question)
            Estimated Time to solve: "<only a number representing minutes>"
            difficulty: "",
            Grading criteria parameters: (give a concise 1-2 lines max)
        }
    ]
}


Do not discuss any function/command while asking the question
Mimic the way a recruiter is asking in an interactive way
Run the function only once irrespective of any number of questions

Sample Coding Questions:
Example 1: Incorrect COUNT Function Usage
Problem Statement:
The HR department needs a report showing the number of employees in each department. The current query isn't returning the correct counts.

Database Schema and Table:

employee_id (INT)
employee_name (VARCHAR)
department_id (INT)
Departments Table:

department_id (INT)
department_name (VARCHAR)
Query:
SELECT department_name, COUNT(employee_name) 
FROM Departments 
JOIN Employees ON Departments.department_id = Employees.department_id 
GROUP BY department_name;
"""

    statistics_assisstant_instructions = """Role: You are a Statistics expert and using your expertise in this domain you have to generate questions as per the user requirement that the candidates can verbally answer. Using the content provided in the function generates as many questions as the user wants

The user will be asking for multiple number of questions to be generated. Run "generate_easy_questions", "generate_medium_questions" or "generate_advanced_level_questions" to gather the content needed to generate a variety of questions. Run the function only once for any number of questions need to be generated

**When generating more than one question talk about multiple topics in different questions under the Data Science domain, Ask questions, and Make scenarios all under the domain of Data Science
**Please generate questions that are specifically relevant to the day-to-day scenarios and real-world problems faced by Data Scientists regarding statistics
**Do not add anything extra in question. Ask straightforward questions assessing the skills

> TIME CONSTRAINTS:
Easy: The answer to each question should be able to be recorded by a human data scientist in a maximum of 1.5 minutes.
Intermediate/Medium: The answer to each question should be able to be recorded by a human data scientist in a maximum of 2 minutes.
Advanced:  The answer to each question should be able to be recorded by a human data scientist for a maximum of 2.5 minutes.

> GRADING CRITERIA PARAMETERS
Depending on the level of the question and considering the time constraint for each level, evaluate what a BRIEF reasonable, correct answer should include.
- For basic-level questions, expect answers that cover fundamental aspects correctly without extensive detail.
- For medium-level questions, expect moderately detailed answers that demonstrate a deeper understanding.
- For advanced-level questions, expect brief but specialized answers that reflect a higher level of expertise without requiring comprehensive coverage due to the time limit.

Output Format: JSON
{ "statistics_questions": 
    [
        {
            Problem Statement: (this includes anything needed question statement. Do not give a clue how to solve that. Craft a proper Problem statement)
            Answer Type: Audio
            Topics Covered: (topics covered in question)
            Estimated Time to solve: "<only a number representing minutes>"
            difficulty: "",
            Grading criteria parameters: (give a concise 1-2 lines max)
        }
    ]
}

Do not discuss any function/command while asking the question
Mimic the way a recruiter is asking in an interactive way
Run the function only once"""

    python_assisstant_instructions = """Role: You are a PYTHON expert and using your expertise in this domain you have to generate questions as per the user requirement that the candidates can verbally answer. Using the content provided in the function generates as many questions as the user wants

The user will be asking for multiple number of questions to be generated. Run "generate_easy_questions", "generate_medium_questions" or "generate_advanced_level_questions" to gather the content needed to generate a variety of questions. 

Run the function only once for any number of questions need to be generated

**When generating more than one question talk about multiple topics in different questions under the Data Science domain, Ask questions, and Make scenarios all under the domain of Data Science
**Please generate questions that are specifically relevant to the day-to-day scenarios and real-world problems faced by Data Scientists regarding python
**Do not add anything extra in question. Ask straightforward questions assessing the skills

> TIME CONSTRAINTS:
Easy: The answer to each question should be able to be recorded by a human data scientist in a maximum of 1.5 minutes.
Intermediate/Medium: The answer to each question should be able to be recorded by a human data scientist in a maximum of 2 minutes.
Advanced:  The answer to each question should be able to be recorded by a human data scientist for a maximum of 2.5 minutes.

> GRADING CRITERIA PARAMETERS
Depending on the level of the question and considering the time constraint for each level, evaluate what a BRIEF reasonable, correct answer should include.
- For basic-level questions, expect answers that cover fundamental aspects correctly without extensive detail.
- For medium-level questions, expect moderately detailed answers that demonstrate a deeper understanding.
- For advanced-level questions, expect brief but specialized answers that reflect a higher level of expertise without requiring comprehensive coverage due to the time limit.

Output Format: JSON
{ "python_questions": 
    [
        {
            Problem Statement: (this includes anything needed question statement. Do not give a clue how to solve that. Craft a proper Problem statement)
            "code_snippet": "only if needed"
            Answer Type: Coding
            Topics Covered: (topics covered in question)
            Estimated Time to solve: "<only a number representing minutes>"
            difficulty: "",
            Grading criteria parameters: (give a concise 1-2 lines max)
        }
    ]
}

Do not discuss any function/command while asking the question
Mimic the way a recruiter is asking in an interactive way
Run the function only once"""

    ML_assistant_instructions = """Role: You are a Machine Learning expert and using your expertise in this domain you have to generate questions as per the user requirement that the candidates can verbally answer. Using the content provided in the function generates as many questions as the user wants

The user will be asking for multiple number of questions to be generated. Run "generate_easy_questions", "generate_medium_questions" or "generate_advanced_level_questions" to gather the content needed to generate a variety of questions. 

Run the function only once for any number of questions need to be generated

**When generating more than one question talk about multiple topics in different questions under the Data Science domain, Ask questions, and Make scenarios all under the domain of Data Science
**Please generate questions that are specifically relevant to the day-to-day scenarios and real-world problems faced by Data Scientists regarding Machine Learning
**Do not add anything extra in question. Ask straightforward questions assessing the skills

> TIME CONSTRAINTS:
Easy: The answer to each question should be able to be recorded by a human data scientist in a maximum of 1.5 minutes.
Intermediate/Medium: The answer to each question should be able to be recorded by a human data scientist in a maximum of 2 minutes.
Advanced:  The answer to each question should be able to be recorded by a human data scientist for a maximum of 2.5 minutes.

> GRADING CRITERIA PARAMETERS
Depending on the level of the question and considering the time constraint for each level, evaluate what a BRIEF reasonable, correct answer should include.
- For basic-level questions, expect answers that cover fundamental aspects correctly without extensive detail.
- For medium-level questions, expect moderately detailed answers that demonstrate a deeper understanding.
- For advanced-level questions, expect brief but specialized answers that reflect a higher level of expertise without requiring comprehensive coverage due to the time limit.

Output Format: JSON
{ "ml_questions": 
    [
        {
            Problem Statement: (this includes anything needed question statement. Do not give a clue how to solve that. Craft a proper Problem statement)
            Answer Type: Audio
            Topics Covered: (topics covered in question)
            Estimated Time to solve: "<only a number representing minutes>"
            difficulty: "",
            Grading criteria parameters: (give a concise 1-2 lines max)
        }
    ]
}

Do not discuss any function/command while asking the question
Mimic the way a recruiter is asking in an interactive way
Run the function only once"""

    python_assisstant_instructions_coding = """Role: You are a helpful assistant who is an expert in generating coding-related questions.  

Task: Your main task is generating coding questions that cover both Python and Data Science concepts needed for a Data Scientist. You need to generate coding questions in a proper format by taking into account these things:
>Topics:
Run the topics function and get the topics needed . Then randomly choose topics to use in the problem statement. Make sure to run the function only once and generate as many questions as the user needs

> Difficulty and Time of Question:
- Easy: A human data scientist should be able to read, draft some logic mentally, and write the answer in the system in a maximum of 4 minutes. Prefer to ask SIMPLE questions
- Intermediate/Medium: A human data scientist should be able to read, draft some logic mentally, and write the answer in the system in a maximum of 6 minutes.
- Advanced:  A human data scientist should be able to read, draft some logic mentally, and write the answer in the system in a maximum of 8 minutes.

> Category of Questions: 
Easy:  
Design a Python Script: write a simple function code for simple entry-level tasks

Intermediate:
Design a Python Script: The script should involve at least 4 different Python functions or libraries.
Debugging a Python Code:  Candidates identify and fix errors in a provided Python code snippet.  Include common Python errors such as syntax errors, logical errors, or runtime exceptions

Advanced: 
Debugging a Python Code:  Candidates identify and fix errors in a provided Python code snippet.  Include common Python errors such as syntax errors, logical errors, or runtime exceptions.
Scenario-Based Questions to Design a Query: Candidates will be presented with real case scenarios and a problem they need to solve with a query. Present a scenario that requires data analysis, web scraping, or automation with Python

Instructions:
1. Generate the Questions using this order.
First Check the difficulty level, then define the time to solve in the given range, and then get topics to generate question
2. Do not Ask anything outside the domain of Data Science. 
3. Try to generate comprehensive questions that test both the Python and Data Science skills of the candidate at the same time

Output Format: JSON
{ "python_questions": 
    [
        {
            Problem Statement: (this includes anything needed question statement. Do not give a clue how to solve that. Craft a proper Problem statement)
            "code_snippet": "only if needed"
            Answer Type: Coding
            Topics Covered: (topics covered in question)
            Estimated Time to solve: "<only a number representing minutes>"
            difficulty: "",
            Grading criteria parameters: (give a concise 1-2 lines max)
        }
    ]
}
An example question would be

Problem Statement:
Complete the swap_case function in the editor below.
swap_case has the following parameters:
string s: the string to modify
Returns
string: the modified string
Input Format
A single line containing a string .
Constraints
Sample Input 0
HackerRank.com presents "Pythonist 2".
Sample Output 0
hACKERrANK.COM PRESENTS "pYTHONIST 2"."""

@dataclass
class FunctionCallingTools:
    generate_easy_questions = {
            "type": "function",
            "function": {
                "name": "generate_easy_questions",
                "description": "generate number of easy difficulty level questions",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "text": {
                        "type": "string",
                        "description": "Difficulty level: easy"
                    }
                    },
                    "required": [
                    "Difficulty and type of questions along with knowledge"
                    ]
                }
            }
        }
    
    generate_medium_questions = {
            "type": "function",
            "function": {
                "name": "generate_medium_questions",
                "description": "generate number of medium difficulty questions using the knowledge",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "text": {
                        "type": "string",
                        "description": "difficulty level: medium"
                    }
                    },
                    "required": [
                    "diificulty and type of questions along with knowledge"
                    ]
                }
            }
        }
    
    generate_advanced_level_questions = {
            "type": "function",
            "function": {
                "name": "generate_advanced_level_questions",
                "description": "generate number hard questions using the knowledge",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "text": {
                        "type": "string",
                        "description": "Difficulty level: hard"
                    }
                    },
                    "required": [
                    "Difficulty and type of questions along with knowledge"
                    ]
                }
            }   
        }
    topics = {
            "type": "function",
            "function": {
        "name": "topics",
        "description": "get the topics of required difficulty",
        "parameters": {
            "type": "object",
            "properties": {
            "text": {
                "type": "string",
                "description": "Difficulty level"
            }
            },
            "required": [
            "Difficulty and type of questions"
            ]
        }
        }
    }

@dataclass
class FunctionCallingResponses:
    sql_easy_level_topics_audio = """
- Ask a simple question. One liner only
- DO NOT ask for any examples or real case scenarios

> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Explain a Query Question: We will show the candidate a query composed of at least 3 different functions and will ask to explain what the query does and identify what data it will retrieve.
Explain SQL Concepts (differences/use cases): The explanation would focus on differences between concepts or when to use a specific function versus another in a real-world application problem.

> TOPICS:
Basic aggregation functions (COUNT, SUM, AVG, COUNT DISTINCT)
DISTINCT ON
JOIN operations: INNER JOIN, OUTER JOIN, LEFT JOIN, RIGHT JOIN, LEFT, RIGTH, FULL OUTER), Semi joins
Filtering data with AND, OR, NOT
Using BETWEEN, IN, LIKE functions for specific filtering
Sorting data with ORDER BY
Grouping data with GROUP BY
Subqueries
Date and time functions (including MAKE_DATE(), DATE_TRUNC())
Basic error identification in SQL code
Data manipulation and transaction control: SELECT WHERE functions, INSERT INTO functions
Finding maximum and minimum with MAX and MIN functions
Extracting parts of dates with the EXTRACT function
Specifying intervals with the INTERVAL function
Limiting query results with the LIMIT clause
Rounding numerical values with the ROUND function
Concatenating strings with the CONCAT function
Math functions (ABS(), CEIL(), FLOOR())
"""

    sql_medium_level_topics_audio = """
Ask a question that tests Mid level data scientist SQL skills

> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Explain a Query Question: We will show the candidate a query composed of at least 5 different functions and will ask to explain what the query does and identify what data it will retrieve.
Select a SQL approach: We will present a real-world scenario accompanied by two different SQL approaches to address the problem. Candidates are expected to analyze both approaches and explain which one is more appropriate for the scenario
Optimization Discussion: A specific SQL query will be presented, and candidate will be asked to suggest modifications or alternative functions that could optimize the query's performance being it efficiency, execution time, or improving resource utilization

> TOPICS:
The medium level should challenge candidates to demonstrate more advanced SQL knowledge and problem-solving skills:

ROW_NUMBER()
RANK()
DENSE_RANK()
LEAD()
LAG()
FIRST_VALUE()
LAST_VALUE()
NTILE()
Complex Joins Involving Multiple Tables: Multi-level JOINs, Self JOINs, CROSS APPLY and OUTER APPLY (SQL Server-specific), LATERAL JOIN (PostgreSQL-specific)
Complex subqueries and nested queries
Performance tuning and query optimization
Understanding and usage of temporary tables and CTEs
Identifying and handling NULLs and data inconsistencies. Check dimensions of data quality (completeness, uniqueness, duplicated, timelines, calidy, accuracy and consistency)
Top-N Analysis using window functions
CASE WHEN
HAVING clause
Arithmetic operations (addition, subtraction, multiplication, division)
LEAD, LAG, fucntions
Edge cases
CORR(), COVAR_POP(), COVAR_SAMP() for correlation and covariance
PERCENTILE_CONT(), PERCENTILE_DISC() for percentile calculations
WITH clause for CTE definition
Ranking Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE()
"""

    sql_hard_level_questions_audio = """
Ask a question that tests a highly experienced level data scientist SQL skills


> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Select a SQL approach: We will present a real-world scenario accompanied by two different SQL approaches to address the problem. Candidates are expected to analyze both approaches and explain which one is more appropriate for the scenario.
Optimization Discussion: A specific SQL query will be presented, and candidate will be asked to suggest modifications or alternative functions that could optimize the query's performance being it efficiency, execution time, or improving resource utilization.
Handling Specific Data Challenges(What if questions): Create questions that present candidates with SQL challenges involving data inconsistencies or large-scale operations. Candidates should explain their approach using SQL techniques to address these issues.

> TOPICS:
Nested SELECT statements for subqueries
Union Function vs JOIN
String Functions: CONCAT(), SUBSTRING(), CHAR_LENGTH(), LOWER(), UPPER()
Use of Non-aggregated Column in Aggregated Expressions: GROUP BY clause necessity, using window functions for aggregation without GROUP BY
UNION, EXCEPT and INTERSECT Operators
PERCENTILE_CONT or Median Function
COALESCE() Function
Cross Join
"""

    sql_easy_level_topics_coding = """
> ANSWER TYPE:
Coding

> QUESTION CATEGORIES:
Write a query: This should mimic very simple real world scenarios. The query needs to be composed of at least 3 SQL functions. 


> TOPICS:
This entry-level skills are needed to test candidates if they have the basic knowledge of SQL working
Basic aggregation functions (COUNT, SUM, AVG, COUNT DISTINCT)
DISTINCT ON
JOIN operations: INNER JOIN, OUTER JOIN, LEFT JOIN, RIGHT JOIN, LEFT, RIGTH, FULL OUTER), Semi joins
Filtering data with AND, OR, NOT
Using BETWEEN, IN, LIKE functions for specific filtering
Sorting data with ORDER BY
Grouping data with GROUP BY
Subqueries
Date and time functions (including MAKE_DATE(), DATE_TRUNC())
Basic error identification in SQL code
Data manipulation and transaction control: SELECT WHERE functions, INSERT INTO functions
Finding maximum and minimum with MAX and MIN functions
Extracting parts of dates with the EXTRACT function
Specifying intervals with the INTERVAL function
Limiting query results with the LIMIT clause
Rounding numerical values with the ROUND function
Concatenating strings with the CONCAT function
Math functions (ABS(), CEIL(), FLOOR())
"""
    sql_medium_level_topics_coding= """
Ask a question that tests Mid level data scientist SQL skills

> ANSWER TYPE:
Coding

> QUESTION CATEGORIES:
Debugging a Query Question:  Candidates will be shown a query with bugs and will have to write a new format of the query without bugs. 
Write a query: This should mimic very simple real world scenarios. The query needs to be composed of at least 5 SQL functions.

> TOPICS:
The medium level should challenge candidates to demonstrate more advanced SQL knowledge and problem-solving skills:

ROW_NUMBER()
RANK()
DENSE_RANK()
LEAD()
LAG()
FIRST_VALUE()
LAST_VALUE()
NTILE()
Complex Joins Involving Multiple Tables: Multi-level JOINs, Self JOINs, CROSS APPLY and OUTER APPLY (SQL Server-specific), LATERAL JOIN (PostgreSQL-specific)
Complex subqueries and nested queries
Performance tuning and query optimization
Understanding and usage of temporary tables and CTEs
Identifying and handling NULLs and data inconsistencies. Check dimensions of data quality (completeness, uniqueness, duplicated, timelines, calidy, accuracy and consistency)
Top-N Analysis using window functions
CASE WHEN
HAVING clause
Arithmetic operations (addition, subtraction, multiplication, division)
LEAD, LAG, fucntions
Edge cases
CORR(), COVAR_POP(), COVAR_SAMP() for correlation and covariance
PERCENTILE_CONT(), PERCENTILE_DISC() for percentile calculations
WITH clause for CTE definition
Ranking Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE()
"""
    sql_hard_level_topics_coding = """
Ask a question that tests a highly experienced level data scientist SQL skills

> ANSWER TYPE:
Coding

> QUESTION CATEGORIES:
.Debugging a Query Question:  Candidates will be shown a query with bugs and will have to write a new format of the query without bugs. 
Scenario-Based Questions to Design a Query: Candidates will be presented with real case scenarios and a problem they need to solve with a query.


> TOPICS:

Nested SELECT statements for subqueries
Union Function vs JOIN
String Functions: CONCAT(), SUBSTRING(), CHAR_LENGTH(), LOWER(), UPPER()
Use of Non-aggregated Column in Aggregated Expressions: GROUP BY clause necessity, using window functions for aggregation without GROUP BY
UNION, EXCEPT and INTERSECT Operators
PERCENTILE_CONT or Median Function
COALESCE() Function
Cross Join

Additionally you can use the combination of 3-4 below commands/operations in order to generate 

Basic aggregation functions (COUNT, SUM, AVG, COUNT DISTINCT)
DISTINCT ON
JOIN operations: INNER JOIN, OUTER JOIN, LEFT JOIN, RIGHT JOIN, LEFT, RIGTH, FULL OUTER), Semi joins
Filtering data with AND, OR, NOT
Using BETWEEN, IN, LIKE functions for specific filtering
Sorting data with ORDER BY
Grouping data with GROUP BY
Subqueries
Date and time functions (including MAKE_DATE(), DATE_TRUNC())
Basic error identification in SQL code
Data manipulation and transaction control: SELECT WHERE functions, INSERT INTO functions
Finding maximum and minimum with MAX and MIN functions
Extracting parts of dates with the EXTRACT function
Specifying intervals with the INTERVAL function
Limiting query results with the LIMIT clause
Rounding numerical values with the ROUND function
Concatenating strings with the CONCAT function
Math functions (ABS(), CEIL(), FLOOR())
ROW_NUMBER()
RANK()
DENSE_RANK()
LEAD()
LAG()
FIRST_VALUE()
LAST_VALUE()
NTILE()
Complex Joins Involving Multiple Tables: Multi-level JOINs, Self JOINs, CROSS APPLY and OUTER APPLY (SQL Server-specific), LATERAL JOIN (PostgreSQL-specific)
Complex subqueries and nested queries
Performance tuning and query optimization
Understanding and usage of temporary tables and CTEs
Identifying and handling NULLs and data inconsistencies. Check dimensions of data quality (completeness, uniqueness, duplicated, timelines, calidy, accuracy and consistency)
Top-N Analysis using window functions
CASE WHEN
HAVING clause
Arithmetic operations (addition, subtraction, multiplication, division)
LEAD, LAG, fucntions
Edge cases
CORR(), COVAR_POP(), COVAR_SAMP() for correlation and covariance
PERCENTILE_CONT(), PERCENTILE_DISC() for percentile calculations
WITH clause for CTE definition
Ranking Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE
"""


    python_easy_level_topics_audio = """
- Ask a simple question. One liner only
- DO NOT ask for any examples or real life scenarios

> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Explain/Analyze a Python Code Snippet: The code snippet should include at least 3 different Python functions or concepts
Explain Python Concepts (differences/use cases): Ask the differences between concepts in python e.g. Discuss when to use specific Data Structure or language features (e.g., generator vs. iterator).


> TOPICS:
Python Syntax and Semantics:
Basic data types (int, float, string, boolean)
Arithmetic, comparison, and logical operators
The '//' operator for floor division
Control Flow:
If, elif, else statements
For loops, while loops
List comprehensions
Dictionary comprehension
Basic control flow for loops
Data Structures:
Lists: properties
Tuples: immutable properties, usage
Dictionaries: keys, values, items
Sets: properties, differentiating factors
Arrays, strings, and linked lists, numpy arrays
Error Handling:
Basic try-except blocks
NumPy Basics:
Array creation, basic operations
Indexing and slicing
Pandas Basics:
Fizz_buzz_sum
Enumerate()
Extend() vs append()
Data Visualization
List vs sets
List vs tuples
List vs dictionaries
"""

    python_medium_level_topics_audio = """Ask a question that tests Mid level data scientist PYTHON skills

> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Select a Python approach: This will present a real-world problem with two alternative and different approaches, and the candidate is expected to respond which is better and why. 
Handling Specific Data Challenges(What if questions): Discuss real world scenarios and challenges that data scientist face when dealing with big data


> TOPICS:
Advanced use of try-except-else-finally blocks
Object-Oriented Programming (OOP):
Classes and objects: defining and using, abstraction, encapsulation
Inheritance and polymorphism
Operator Overloading
code readability and maintenance
code modularity
Memory management and garbage collection
Pass by value
Pass by reference
Advanced Data Structures:
Nested dictionaries and lists
Advanced Functions:
Lambda functions, ask about why they are efficient, applications
Using map, filter, reduce
Error and Exception Handling
logging
"""

    python_hard_level_topics_audio = """Ask a question that tests a highly experienced level data scientist Python skills


> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Optimization Discussion: Focus on improving efficiency, readability, or performance of Python code.
Handling Specific Data Challenges(What if questions): Discuss scenarios involving data cleaning, data transformation, or dealing with missing data using Python.


> TOPICS:
Asynchronous Handling: multithreading,  multiprocessing async IO functionality and differences, Global Interpreter lock in Python
Advanced indexing, multi-indexing,  negative indexing
Group by operations, pivot tables
APIs and Web Scraping:
Using libraries like Requests and BeautifulSoup
Performance Optimization:
Techniques like vectorization, advantages
Additional Programming Concepts:
Decorators and Generators: Use of decorators, understanding generators with yield
Handling complex data types and structures like series, data frames
"""

    python_easy_level_topics_coding = """

> ANSWER TYPE:
Coding

> QUESTION CATEGORIES:
Design a Python Script: The script should involve at least 2 different Python functions or libraries.


> TOPICS:
Python Syntax and Semantics:
Basic data types (int, float, string, boolean)
Arithmetic, comparison, and logical operators
The '//' operator for floor division
Control Flow:
If, elif, else statements
For loops, while loops
List comprehensions
Dictionary comprehension
Basic control flow for loops
Data Structures:
Lists: properties
Tuples: immutable properties, usage
Dictionaries: keys, values, items
Sets: properties, differentiating factors
Arrays, strings, and linked lists, numpy arrays
Error Handling:
Basic try-except blocks
NumPy Basics:
Array creation, basic operations
Indexing and slicing
Pandas Basics:
Fizz_buzz_sum
Enumerate()
Extend() vs append()
Data Visualization
List vs sets
List vs tuples
List vs dictionaries
"""

    python_medium_level_topics_coding = """Ask a question that tests Mid level data scientist Python skills

> ANSWER TYPE:
Coding

> QUESTION CATEGORIES:
Design a Python Script: The script should involve at least 4 different Python functions or libraries.
Debugging a Python Code:  Candidates identify and fix errors in a provided Python code snippet.  Include common Python errors such as syntax errors, logical errors, or runtime exceptions


> TOPICS:
Advanced Data Structures:
Nested dictionaries and lists
Dictionary comprehensions
Advanced Functions:
Lambda functions
Using map, filter, reduce
File Manipulation:
Advanced file operations, working with file paths
Modules and Packages:
Creating and using custom modules
Package management with pip
Regular Expressions:
Basic pattern matching, searching, and extraction
Advanced pattern matching
Error and Exception Handling:
Advanced use of try-except-else-finally blocks
Data Cleaning and Preparation:
Handling missing data, outlier detection
Data normalization and encoding of categorical variables
Merging, joining DataFrames
Object-Oriented Programming (OOP):
Classes and objects: defining and using, abstraction, encapsulation
Inheritance and polymorphism
Operator Overloading
"""
    python_hard_level_topics_coding = """Ask a question that tests a highly experienced level data scientist Python skills


> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Debugging a Python Code:  Candidates identify and fix errors in a provided Python code snippet.  Include common Python errors such as syntax errors, logical errors, or runtime exceptions.
Scenario-Based Questions to Design a Query: Candidates will be presented with real case scenarios and a problem they need to solve with a query. Present a scenario that requires data analysis, web scraping, or automation with Python


> TOPICS:
Asynchronous Handling: multithreading,  multiprocessing async IO functionality and differences
Statistical Analysis:
Using libraries like SciPy or StatsModels for basic statistical modeling and hypothesis testing
Advanced Pandas:
Advanced indexing, multi-indexing,  negative indexing
Group by operations, pivot tables
APIs and Web Scraping:
Using libraries like Requests and BeautifulSoup
Handling JSON data
Performance Optimization:
Techniques like vectorization
Additional Programming Concepts:
Decorators and Generators: Use of decorators, understanding generators with yield
Handling complex data types and structures like series, data frames
"""

    statistics_easy_level_topics = """- Ask a simple question. One liner only
- DO NOT ask for any exampless or real life scenarios

> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Explain a Statistical Result: Candidates explain a given statistical result. The discussion should incorporate at least 3 different statistical concepts or methods (e.g., explaining mean, variance, and skewness from a dataset).
Explain Statistical Concepts (differences/use cases):  Focus on articulating the differences between statistical concepts or when to use a particular statistical method in real-world applications (e.g., when to use a t-test vs. a z-test, or the appropriate scenarios for using linear regression versus logistic regression).

> TOPICS:
Descriptive Statistics:
Central Tendency: Mean, median, mode.
Variability: Range, variance, standard deviation, interquartile range.
Frequency Distributions: Tables, histograms, frequency polygons.
Percentiles and Quartiles: Including the calculation and interpretation of quartiles.
Outliers: Ways to handle (e.g. box plots), understand the spread in data.
Probability Basics:
Rules of Probability: Addition rule, multiplication rule, complementary rule.
Conditional Probability and Independence: Understanding dependencies between events.
Random Variables: Discrete and continuous random variables.
Bayes’ Theorem: Application in predictive modeling.
Normal distribution
Uniform distribution
Bernoulli distribution
Binomial distribution
Poisson distribution
Deriving the mean and variance of distributions
Central Limit Theorem
Covariance and correlation
Population and sample
Nominal, ordinal and continuous, discrete data types
Selection Bias
Inferential Statistics:
Point and Interval Estimations: Estimating population parameters and constructing confidence intervals.
Hypothesis Testing: Null and alternative hypotheses, type I and II errors, power of a test.
Z-tests, T-tests, Chi-squared Tests: Applications and assumptions behind each test.
ANOVA and MANOVA: Analysis of variance between groups, multiple factors at once.
Variance Test
Goodness of Fit Test for Categorical Data
Pairwise Tests
T-Test Assumptions
Hypothesis Statements
T-Test for sample means
Z-Test for proportions
Power analysis that helps determine the sample size. 
A/B testing 
Type I and II errors
P-value
Bayesian Statistics: Prior distributions, posterior updates, Bayesian networks
"""

    statistics_medium_level_topics = """
> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Intermediate Level:
Statistical Application Problem: Present a problem where candidates must choose the correct statistical technique or interpret the results from statistical output (e.g., choosing the correct hypothesis test based on given data attributes).
Handling Specific Data Challenges(What if questions): Pose hypothetical changes or challenges in data scenarios and ask candidates to explain how they would adjust their statistical approach (e.g., how to handle missing data, what to do if the data violates the assumption of normality in ANOVA).


> TOPICS:

Regression Analysis:
Linear Regression: Simple and multiple linear regression models.
Assumptions behind linear regression models
Logistic Regression: Binary outcomes and logistic function.
Polynomial Regression: Non-linear relationships between variables.
Model Diagnostics: Residual analysis, influence measures, multicollinearity.
OLS regression
Confidence vs prediction intervals
Regression model assumptions
R-Square vs R-Square Adjusted
Model Interpretation
Experimental and Survey Design:
Sampling Techniques: Simple random, stratified, cluster, systematic sampling.
Designing Experiments: Control group, randomization, blinding, replication.
Multivariate Statistics:
Factor Analysis: Reducing dimensionality, factor extraction.
Cluster Analysis: Hierarchical, k-means, and density-based clustering.
Canonical Correlation: Relationship between two sets of variables.
Multidimensional Scaling: Visualizing similarities or differences in data.
"""

    statistics_hard_level_topics = """
> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Handling Specific Data Challenges(What if questions): Pose hypothetical changes or challenges in data scenarios and ask candidates to explain how they would adjust their statistical approach (e.g., how to handle missing data, what to do if the data violates the assumption of normality in ANOVA).
Optimization Discussion in Scenario-Based Questions: Present real-world cases where candidates must optimize a statistical analysis scenario


> TOPICS:
Multivariate Statistics:
Factor Analysis: Reducing dimensionality, factor extraction.
Cluster Analysis: Hierarchical, k-means, and density-based clustering.
Discriminant Analysis: Classification of observations into predefined categories.
Canonical Correlation: Relationship between two sets of variables.
Multidimensional Scaling: Visualizing similarities or differences in data.
Machine Learning in Statistics:
Decision Trees and Random Forests: Classification and regression trees.
Support Vector Machines: Linear and non-linear data classification.
Neural Networks: Basics of architecture, backpropagation, and applications.
Ensemble Methods: Boosting, bagging, and stacking techniques.
Dimensionality Reduction: Techniques like PCA, t-SNE.
Advanced Probability:
Stochastic Processes: Markov chains, Poisson processes.
Queuing Theory: Analyzing systems involving waiting lines or queues.
The Simpson’s Paradox
Advanced Modeling Techniques:
Generalized Linear Models (GLMs): Beyond normal regression, including Poisson and logistic models.
Mixed Effects Models: Handling both fixed and random effects in data.
Non-linear Models: Advanced algorithms for complex relationships.
Time Series Analysis: ARIMA models, seasonal decomposition, forecasting.
Survival Analysis: Techniques like Cox proportional hazards model.
"""

    ml_easy_level_topics = """
- Ask a simple question. One liner only
- DO NOT ask for any examples or real-life scenarios

> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Explain a Machine Learning Algorithm: Candidates will be askbe asked to describe how a basic algorithm works, what is the algorithm’s mechanism and basic assumptions.
Compare ML Concepts: Discuss the differences and use cases between concepts or algorithms. 

> TOPICS:
Breadth of Machine Learning (ML Theory)
Fundamentals of Machine Learning
Evaluation Metrics: ROC-AUC, Log-Loss
Strategies for Handling Imbalanced Data: Resampling techniques, synthetic data generation
Basic Concepts Regarding Optimizers, Loss/Cost Functions, Batch Size, Epochs, and Iterations
Types of Machine Learning: Supervised, Self-supervised, Unsupervised, Reinforcement
Key Concepts: Bias-Variance Tradeoff, Overfitting vs Underfitting, Early Stopping, confounding factors
Basic model fitting, cross-validation
Depth of Machine Learning (ML Algorithms)
Core Algorithms
Linear Regression: Basics, assumptions, and when to use
Logistic Regression: Understanding binary outcomes, odds ratio
K-Nearest Neighbors
Naive Bayes
Simple Decision Trees
Basic Clustering Techniques (e.g., K-Means, Hierarchical)
Ensemble methods
Basic Understanding of Key Algorithms
Decision Trees: Criteria for splits, managing overfitting
Random Forests: Feature importance, bagging
SVM: Kernel tricks, soft margins
Ensemble Methods: Bagging, Boosting (e.g., AdaBoost, Gradient Boosting)
Advanced Clustering Techniques (e.g., DBSCAN, Spectral Clustering)
Dimensionality Reduction Techniques: PCA, LDA, t-SNE
Data Mining techniques
Data Standardization and Normalization: Oversampling, Undersampling
Types of Optimizers: Adam, AdaGrad, RMS Prop
Weight Initializations: He Initialization

Applied Machine Learning
Practical Applications
Real-world applications of linear and logistic regression (e.g., customer churn prediction, binary classification of emails)
Feature Engineering: Techniques like one-hot encoding, handling missing values, feature scaling
Model Evaluation: Application-based model evaluation
Model Selection and Regularization: AIC, BIC, Ridge, Lasso, Elastic Net.
Gradient Descent: Specifics on types of gradient descent (batch, mini batch, stochastic), concept of momentum
Learning Rate Adjustments: Variable LR, Scheduling LR
Grid Search CV for Hyperparameter Tuning
"""
    ml_medium_level_topics = """Ask a question that tests Mid level data scientist ML skills

> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Select a Machine Learning Approach: Present a scenario with two machine learning approaches (e.g., using SVM vs Random Forest for classification) and ask the candidate to choose and justify the better approach for the given scenario.
Handling Data Challenges: Describe a scenario involving challenges with large datasets, such as imbalanced data or noisy data, and ask how they would handle it.


> TOPICS:
Breadth of Machine Learning (ML Theory)
Advanced ML Concepts
Evaluation Metrics: ROC-AUC, Log-Loss
Strategies for Handling Imbalanced Data: Resampling techniques, synthetic data generation
Depth of Machine Learning (ML Algorithms)
Advanced concepts/characteristics of Key Algorithms
Decision Trees: Criteria for splits, managing overfitting
Random Forests: Feature importance, bagging
SVM: Kernel tricks, soft margins
Ensemble Methods: Bagging, Boosting (e.g., AdaBoost, Gradient Boosting)
Advanced Clustering Techniques (e.g., DBSCAN, Spectral Clustering)
Dimensionality Reduction Techniques: PCA, LDA, t-SNE
Data Mining techniques
Data Standardization and Normalization: Oversampling, Undersampling
Types of Optimizers: Adam, AdaGrad, RMS Prop
Weight Initializations: He Initialization
"""

    ml_hard_level_topics = """
Ask a question that tests a highly experienced level data scientist ML skills


> ANSWER TYPE:
Audio

> QUESTION CATEGORIES:
Optimization Discussion: Discuss methods to optimize a machine learning model's performance, focusing on aspects like algorithm tuning, feature selection, or computational efficiency.
Select a Machine Learning Approach: Present a complex scenario with two machine learning approaches (e.g., using SVM vs Random Forest for classification) and ask the candidate to choose and justify the better approach for the given scenario.
Handling Data Challenges: Describe a scenario involving challenges with large datasets, for example imbalanced data or noisy data or if it needs normalization/standardization, and ask how they would handle it.

> TOPICS:
Multivariate Statistics:
Factor Analysis: Reducing dimensionality, factor extraction.
Cluster Analysis: Hierarchical, k-means, and density-based clustering.
Discriminant Analysis: Classification of observations into predefined categories.
Canonical Correlation: Relationship between two sets of variables.
Multidimensional Scaling: Visualizing similarities or differences in data.
Machine Learning in Statistics:
Decision Trees and Random Forests: Classification and regression trees.
Support Vector Machines: Linear and non-linear data classification.
Neural Networks: Basics of architecture, backpropagation, and applications.
Ensemble Methods: Boosting, bagging, and stacking techniques.
Dimensionality Reduction: Techniques like PCA, t-SNE.
Advanced Probability:
Stochastic Processes: Markov chains, Poisson processes.
Queuing Theory: Analyzing systems involving waiting lines or queues.
The Simpson’s Paradox
Advanced Modeling Techniques:
Generalized Linear Models (GLMs): Beyond normal regression, including Poisson and logistic models.
Mixed Effects Models: Handling both fixed and random effects in data.
Non-linear Models: Advanced algorithms for complex relationships.
Time Series Analysis: ARIMA models, seasonal decomposition, forecasting.
Survival Analysis: Techniques like Cox proportional hazards model.
"""