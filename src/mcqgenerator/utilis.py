import os 
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.pdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        
        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif file.name.endswith(".txt"):
        try:
            return file.read().decode("utf-8")
        except UnicodeDecodeError as e:
            # Handle the decoding error
            print(f"Error decoding file: {e}")
            # Return an empty string or handle the error as needed
            return ""
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file supported"
        )


import json

def get_table_data(quiz_str):
    try:
        # Convert the quiz from a str to dict
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = "||".join(
                [f"{option}-> {option_value}" for option, option_value in value["options"].items()]
            )

            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "correct": correct})

        return quiz_table_data

    except Exception as e:
        print(f"Error processing quiz data: {e}")
        return []


