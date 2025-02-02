import ollama
from datasets import load_dataset

# # Load the dataset (ensure it is correctly named)
# dataset = load_dataset("datasets/test1")
with open('datasets/test1', 'r') as file:
    data = file.read()

# Define the message to send to the Ollama model (PROMPT GOES HERE)
response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"""
            Given a transcript where a teacher is working with a child with disabilities, please identify key moments that show the child engaging with support, struggling, or engaging spontaneously. 
            {data},

            First, number each moment clearly. 
            Then, for each moment, please format clearly and provide the following:

            1. Time Stamp and Location (if provided): Provide the exact time (e.g., 02:03 - 03:16) and location (if mentioned).


            2. Type of Challenge and Why: Red Stories: Struggling to engage, Blue Stories: Engaging with support, Green Stories: Doing it independently or spontaneously


            3. A Vignette or a summary of what is happening: e.g.
            "Child JG and adult are pretending to be mountain climbers. They are climbing to the top of the play structure, putting on their pretend skis, and then sliding down together. JG and adult are at the top of the play structure and JG slides down without the adult.  adult shouts after him ""Oh no JG! I only have one of my skis. One of them slid down without me! Can you bring it back up to me?"" JG returns to adult, and they pretend to find the lost ski together. 


            4. Daily Realities: What specific issue or behavior is being observed? e.g.
            "Child leaves the play without telling peers where they are going"


            5. Milestone and Bucket: given knowledge gotten from {{knowledge_base_results}}, relate the moment to a developmental milestone (e.g., "Imagining - Pretend Play") and explain how it connects to the child’s current skills or abilities. Refer to knowledge from the provided dataset for context.


            6. Conclude on short tip for an educator like "Tip: Slow down the end of the play"

                        "<div class="container">
                <h2>Moment 1</h2>

                <h3>Time Stamp and Location:</h3>
                <p>01:18 - 01:36, <span class="highlight">Sandbox</span></p>

                <h3>Type of Challenge and Why:</h3>
                <p><span class="highlight">Red Stories: Struggling to engage</span></p>
                <p>Liam is observed being inactive and ignoring the teacher's attempts to engage him in conversation about his project. The teacher intervenes by giving Liam verbal options to express his desire to leave the interaction.</p>

                <h3>Daily Realities:</h3>
                <p>Child leaves the play without telling peers or adults where they are going.</p>

                <h3>Milestone and Bucket most similar:</h3>
                <div class="milestone">
                <strong>Milestone:</strong> INTERACTIONS - Transactions
                </div>
                <div class="bucket">
                <strong>Bucket:</strong> Child will effectively request help when needed, using gestures or words to communicate personal needs and gain attention from peers or teachers.
                </div>
                <div class="explanation">
                <strong>Explanation:</strong> Liam struggles with verbal communication and needs support to express his intentions, which is crucial for effective interaction and engagement.
                </div>

                <h3>Tip:</h3>
                <p class="tip">Encourage verbal communication by providing simple choices to express needs or intentions.</p>
            </div>"
            
            """,
        },
    ],
)

# Print the response from the Ollama model
print(response["message"]["content"])
