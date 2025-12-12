<div align="center">
  <h1>☎️ Phone Calling Agents Course ☎️</h1>
  <h3>How to build an Agent Call Center using FastRTC, Superlinked, Twilio, Opik & RunPod</h3>
</div>

</br>

<p align="center">
    <img src="static/main_gh_image.png" alt="Architecture" width="600">
</p>



## Part of projects


 We're building a **real estate company**, but with a twist … the employees will be **realtime voice agents**!

By the end of this course, you'll have a system capable of:

* Receive inbound calls with Twilio
*  Make outbound calls through Twilio
*  Search live property data using Superlinked
*  Run realtime conversations powered by FastRTC
*  Transcribe speech instantly with Moonshine + Fast Whisper
*  Generate lifelike voices using Kokoro + Orpheus 3B
*  Deploy open-source models on Runpod for GPU acceleration








## Getting Started

Before diving into the lessons, make sure you have everything set up properly:

1. 📋 **Initial Setup**: Follow the instructions in [`docs/GETTINGS_STARTED.md`](docs/GETTINGS_STARTED.md) to configure your environment and install dependencies.


---


#### Option B: FastAPI Call Center (Production-Ready)

For a production-ready setup that can receive real phone calls:

**Step 1**: Start the call center application

```bash
make start-call-center
```

This starts a FastAPI application using Docker Compose on port 8000.

**Step 2**: Expose your local server to the internet

```bash
make start-ngrok-tunnel
```

Or manually:

```bash
ngrok http 8000
```

**Step 3**: Connect to Twilio

Follow the instructions in the [article](https://theneuralmaze.substack.com/p/building-realtime-voice-agents-with) to:
- Configure your Twilio account
- Connect your ngrok URL to Twilio
- Start receiving real phone calls!

---

## Lesson 2: The Missing Layer in Modern AI Retrieval

<p align="center">
    <img src="static/diagrams/diagram_lesson_2.png" alt="Lesson 2 Diagram" width="800">
</p>

**Goal**: Learn how to implement advanced search capabilities for realtime voice agents using Superlinked to handle complex, multi-attribute queries.





1. 📓 **Work Through the Notebook**: Open and run through [`notebooks/lesson_2_superlinked_property_search.ipynb`](notebooks/lesson_2_superlinked_property_search.ipynb) to learn:
   - How to define different Space types (TextSimilaritySpace, NumberSpace, CategoricalSimilaritySpace)
   - How to combine spaces into a single searchable index
   - How to dynamically adjust weights at query time

2. 💻 **Explore the Code**: Dive into the repository to see how Superlinked integrates with our voice agent:
   - Check out `src/realtime_phone_agents/infrastructure/superlinked/` for the implementation
   - Review `src/realtime_phone_agents/agent/tools/property_search.py` to see how the search tool is exposed to the agent
   
   _We'll explore the code in detail during the Live Session!_

3. 🚀 **Test the Complete System**: Now it's time to see everything work together!

   **Step 1**: Start the call center application

   ```bash
   make start-call-center
   ```

   **Step 2**: Expose your local server (if not already running)

   ```bash
   make start-ngrok-tunnel
   ```

   **Step 3**: Call your Twilio number and test the property search

   Try asking the agent:
   
   > _"Do you have apartments in Barrio de Salamanca of at most 900,000 euros?"_

   Wait for the response. The agent should find and return information about the only apartment in the dataset ([`data/properties.csv`](data/properties.csv)) that meets these criteria!

   This demonstrates how the voice agent can now handle complex queries combining location (Barrio de Salamanca) and price constraints (≤ €900,000) in real-time.

---

 Improving STT and TTS Systems

<p align="center">
    <img src="static/diagrams/diagram_lesson_3.png" alt="Lesson 3 Diagram" width="800">
</p>

**Goal**: Improve the quality of STT and TTS systems used in the voice agent.

### Steps:

1. 📖 **Read the Article**: Start with the [Substack article](https://theneuralmaze.substack.com/p/how-to-deploy-stt-and-tts-systems) to understand the fundamentals of STT and TTS systems, and how to deploy them on Runpod.

2. 📓 **Work Through the Notebook**: Open and run through [`notebooks/lesson_3_stt_tts.ipynb`](notebooks/lesson_3_stt_tts.ipynb) to experience how the new `faster-whisper` and `Orpheus 3B` deployments look like.

3. 💻 **Explore the Code**: It's time to see the additions for `week 3`. Check out the new `stt/` and `tts/` modules in `src/realtime_phone_agents/`:

   - **STT (Speech-to-Text)**:
     - `local/`: Implementation using **Moonshine** for local inference.
     - `groq/`: Integration with **Groq's** fast inference API.
     - `runpod/`: Self-hosted **Faster Whisper** implementation.

   - **TTS (Text-to-Speech)**:
     - `local/`: Implementation using **Kokoro** for high-quality local synthesis.
     - `togetherai/`: Integration with **Together AI**.
     - `runpod/`: Self-hosted **Orpheus 3B** implementation.

4. 🐳 **New Docker Images**: We've added two new Dockerfiles to deploy our custom models on RunPod:

   - **`Dockerfile.faster_whisper`**: Builds a container for the **Faster Whisper** model (large-v3). It uses the `speaches-ai/speaches` base image and pre-downloads the model for faster startup.
   - **`Dockerfile.orpheus`**: Builds a container for the **Orpheus 3B** model using `llama.cpp` server with CUDA support, optimized for real-time speech generation.

5. 🚀 **Deploy & Interact**: Ready to test these models? Follow these steps:

   > ⚠️ **IMPORTANT**: Before proceeding, ensure you have completed the setup in [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md). This includes setting up your API keys and environment variables (especially for RunPod).

   **Step 1: Deploy to RunPod**
   
   Use the Makefile commands to spin up your GPU pods:
   
   ```bash
   # Deploy Faster Whisper
   make create-faster-whisper-pod
   
   # Deploy Orpheus 3B
   make create-orpheus-pod
   ```
   
   *Note: These scripts will automatically print the endpoint URLs once the pods are ready. Make sure to update your `.env` file with these URLs!*

   **Step 2: Start the Gradio App**
   
   Launch the interactive interface to test different combinations:
   
   ```bash
   make start-gradio-application
   ```

   **Step 3: Experiment!**
   
   In the Gradio interface, you can mix and match different implementations:
   
   - **STT Options**:
     - `Moonshine` (Local)
     - `Whisper` (Groq API)
     - `Faster Whisper` (RunPod - *requires Step 1*)
     
   - **TTS Options**:
     - `Kokoro` (Local)
     - `Orpheus` (Together AI API)
     - `Orpheus` (RunPod - *requires Step 1*)

---

## The tech stack

<table>
  <tr>
    <th>Technology</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><img src="static/fastrtc_logo.png" width="100" alt="FastRTC Logo"/></td>
    <td>The python library for real-time communication.
</td>
  </tr>
  <tr>
    <td><img src="static/superlinked_logo.png" width="100" alt="Superlinked Logo"/></td>
    <td>SSuperlinked is a Python framework for AI Engineers building high-performance search & recommendation applications that combine structured and unstructured data.

</td>
  </tr>
  <tr>
    <td><img src="static/runpod_logo.png" width="100" alt="Runpod Logo"/></td>
    <td>The end-to-end AI cloud that simplifies building and deploying models.</td>
  </tr>
  <tr>
    <td><img src="static/opik_logo.svg" width="100" alt="Opik Logo"/></td>
    <td>Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards.</td>
  </tr>
  <tr>
    <td><img src="static/twilio_logo.png" width="100" alt="Twilio Logo"/></td>
    <td>Twilio is a cloud communications platform that enables developers to build, manage, and automate voice, text, video, and other communication services through APIs.</td>
  </tr>
</table>


## Contributors

<table>
  <tr>
    <td align="center"><img src="https://github.com/MichaelisTrofficus.png" width="100" style="border-radius:50%;"/></td>
    <td>
      <strong>Miguel Otero Pedrido | Senior ML / AI Engineer </strong><br />
      <i>Founder of The Neural Maze. Rick and Morty fan.</i><br /><br />
      <a href="https://www.linkedin.com/in/migueloteropedrido/">LinkedIn</a><br />
      <a href="https://www.youtube.com/@TheNeuralMaze">YouTube</a><br />
      <a href="https://theneuralmaze.substack.com/">The Neural Maze Newsletter</a>
    </td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/jesuscopado.png" width="100" style="border-radius:50%;"/></td>
    <td>
      <strong>Jesús Copado | Senior ML / AI Engineer </strong><br />
      <i>Equal parts cinema fan and AI enthusiast.</i><br /><br />
      <a href="https://www.youtube.com/@jesuscopado-en">YouTube</a><br />
      <a href="https://www.linkedin.com/in/copadojesus/">LinkedIn</a><br />
    </td>
  </tr>
</table>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
