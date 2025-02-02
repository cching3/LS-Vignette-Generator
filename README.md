# Learning Seed's Vignette Generator
## 🎯 Usage

Once the app is set up, you can interact with the tool by inputting your transcript data into the frontend. The AI will process the input and return an automated vignette.

---

## 📦 Installation

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/cching3/LS-Vignette-Generator
   cd LS-Vignette-Generator
   ```

2. **Create a Python virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install required dependencies**:
   ```bash
   pip install flask ollama datasets
   ```

---

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. **Create a new React app** in the current directory:
   ```bash
   npx create-react-app .
   ```

---

### Testing the Application

1. **Start the Flask server** (Backend):
   ```bash
   python Gemini.py  # Alternatively, change this to app.py or whichever file you prefer
   ```

2. **Start the React development server** (Frontend):
   ```bash
   npm start
   ```

3. Open your browser and go to [http://localhost:3000](http://localhost:3000) to see the app in action.

---


### More Potential Dependencies:

<!-- # install PyTorch
pip3 install torch torchvision torchaudio

# install Hugging Face's Transformers and Datasets
pip3 install transformers datasets

# install sentencepiece for tokenizations
pip3 install sentencepiece

# Optionally, install Accelerate for efficient distributed training
pip3 install accelerate -->

<!-- pip install ollama

pip install transformers datasets torch accelerate
https://huggingface.co/welcome
huggingface-cli login -->

