#import necessary libraries
from flask import Flask, render_template, request, jsonify,send_from_directory
import matplotlib
import openai
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import numpy as np
app = Flask(__name__)
# Set your OpenAI API key
openai.api_key = "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"
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #Get the data in JSON format from the Client Request
        data = request.get_json()
        user_message = data.get("user_message")
        #Check if User Message is received
        if user_message:
            #Call the function to handle the user's message and generate a bot response
            bot_response = handle_user_message(user_message)
        else:
            #Handle the case where there is no user message 
            bot_response = handle_user_message(user_message)
        #Return the bot's response in JSON format to the Client    
        return jsonify({"bot_response": bot_response})
    #If the request methos id GET , render the HTML Template
    return render_template("index.html")
@app.route('/static/<path:filename>')
def static_files(filename):
    #Server static files (e.g., CSS, Javascript) from Static Directory
    return send_from_directory('static', filename)
#Calling of function as per the User Choice
def handle_user_message(user_message):
    if "1" in user_message:
        return find_research_papers_on_topic(user_message)
    elif "2" in user_message:
        return summary_on_the_topic(user_message)
    elif "3" in user_message:
        return find_research_gaps(user_message)
    elif "4" in user_message:
        return find_leading_expert(user_message)
    elif "5" in user_message:
        return state_of_arts(user_message)
    elif "6" in user_message:
        return generate_research_graph(user_message)
    elif "7" in user_message:
        return interactive_compiling_of_reports(user_message)
    elif "8" in user_message:
        return cross_disciplinary_Idea_Generator(user_message)
    elif "9" in user_message:
        return Identify_dataset(user_message)
    else:
        return "I didn't understand your request. Please choose from the options."
# Define OpenAI functions here
def generate_ideas(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=350,
        temperature=0.8
    )
    return response.choices[0].text.strip()
def find_research_papers_on_topic(message):
    # Extract the topic from the message
    topic = message.split('-')[1].strip()
    prompt = f"Find Top research papers on topic '{topic}' with its link"
    return generate_ideas(prompt)
def summary_on_the_topic(message):
    topic = message.split('-')[1].strip()
    prompt = f"Generate the summary of the research results on the topic of '{topic}' from several published research papers"
    return generate_ideas(prompt)
def find_research_gaps(message):
    topic = message.split('-')[1].strip()
    prompt = f"Generate the research gaps on the topic of '{topic}'which should say about current state with statistics provided, desired future state with statistics,identifies gap and action plan to be taken"
    return generate_ideas(prompt)
def find_leading_expert(message):
    topic = message.split('-')[1].strip()
    prompt = f"Generate Top leading experts in the area of '{topic}'"
    return generate_ideas(prompt)
def state_of_arts(message):
    topic = message.split('-')[1].strip()
    prompt = f"Generate comprehensive up to date summary of the current status or the most advanced and innovative developments in a '{topic}'field by conducting a thorough analysis of existing literature, research findings, technologies, methodologies,"
    return generate_ideas(prompt)
def interactive_compiling_of_reports(message):
    topic = message.split('-')[1].strip()
    prompt = f"Generate creating a comprehensive and informative report that summarizes the existing body of research literature within '{topic}'. It should be characterized by active engagement and collaboration, often involving multiple individuals or stakeholders."
    return generate_ideas(prompt)
def cross_disciplinary_Idea_Generator(message):
    topic = message.split('-')[1].strip()
    prompt = f"Generate Innovative Research topics or ideas by combining concepts and insights from different academic disciplines and research literature on the topic of '{topic}'"
    return generate_ideas(prompt)
def Identify_dataset(message):
    topic = message.split('-')[1].strip()
    prompt = f"Search 10 dataset name with a link for the given topic '{topic}'"
    return generate_ideas(prompt)

def generate_research_graph(message, graph_type="bar"):
    topic = message.split('-')[1].strip()
    prompt = f"Explain the trend summary of the '{topic}' from past data and as well as present data and also provide some statistics"
    return generate_ideas(prompt)


if __name__ == "__main__":
    app.run(debug=True, threaded=False)
