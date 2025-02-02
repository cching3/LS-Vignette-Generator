from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)

# Enable CORS for your React app (localhost:3000)
CORS(app, origins=["http://localhost:3000"])

@app.route('/api/process', methods=['POST'])
def process_data():
    # Get the user input from the POST request
    data = request.json.get('transcriptText', '')
    
    # Load the dataset (test1.txt)
    try:
        with open('datasets/test1', 'r') as file:
            dataset = file.read()
    except FileNotFoundError:
        return jsonify({'error': 'Dataset not found'}), 404
    
    # Combine the dataset with the input data for Ollama processing
    prompt = f"""
    Given a transcript where a teacher is working with a child with disabilities, analyze key moments and categorize them by behavior. These categories should include moments where the child is:
    - Struggling to engage with support
    - Willingly engaging with support
    - Acting independently or spontaneously

    {data},

    For each moment, summarize the key interaction without repeating any specific wording or phrasing from the transcript. Use the following format for each moment, but focus on **analysis** and **insight** rather than quoting or paraphrasing the original transcript text.

    **Output Structure for each moment (Provide insights in this HTML template):**
    <div class="moment">
        <h2>Moment 1</h2>

        <h3>Time Stamp</h3>
        <p>Provide timestamp in format: XX:XX-YY:YY</p>

        <h3>Location</h3>
        <p><span class="highlight">Provide location if mentioned in the transcript</span></p>

        <h3>Vignette</h3>
        <p>Provide a detailed description of the moment. What happened with who.</p>


        <h3>Type of Challenge and Why:</h3>
        <p>Which of the 3 types of COLOR of stories: Red Stories: Struggling to engage, Blue Stories: Willingly engaging with support, or Green Stories: Doing it independently or spontaneously.</p>
        <p>Provide a detailed description of the moment. Then explaining why it fits into this category (struggling, supported, or independent).</p>

        <h3>Daily Realities:</h3>
        <p>Describe the specific issue or behavior observed in this moment. How does the child react in everyday interactions or situations?</p>

        <h3>Milestone and Bucket most similar:</h3>
        <div class="milestone">
            <strong>Milestone:</strong> Identify the developmental milestone the child is working on (e.g., Pretend Play, Social Interaction, ).
        </div>
        <div class="bucket">
            <strong>Bucket:</strong> Describe how this moment fits within the child's growth or developmental stage. For example, the child might be developing the ability to communicate needs effectively or engage in pretend play.
        </div>
        <div class="explanation">
            <strong>Explanation:</strong> Provide context for how this moment fits into the child’s broader developmental progress and needs.
        </div>

        <h3>Tip for Educators:</h3>
        <p class="tip">Give a short, actionable piece of advice for educators based on the moment. For example: "Encourage more spontaneous interactions by allowing the child to take the lead in play." </p>
    </div>

    RETURN an HTML version of output
    """


    # Call Ollama model
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return jsonify({'response': response["message"]["content"]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
