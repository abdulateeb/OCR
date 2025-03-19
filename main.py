{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNw1jq/z8BL1eNpCmmbuW/s",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/abdulateeb/OCR/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import subprocess\n",
        "import sys\n",
        "\n",
        "def install_package(package):\n",
        "    subprocess.check_call([sys.executable, \"-m\", \"pip\", \"install\", package])\n",
        "\n",
        "# List of required packages\n",
        "packages = [\"streamlit\", \"ollama\", \"pillow\"]\n",
        "\n",
        "# Install each package if not already installed\n",
        "for package in packages:\n",
        "    try:\n",
        "        __import__(package if package != \"pillow\" else \"PIL\")\n",
        "    except ImportError:\n",
        "        print(f\"Installing {package}...\")\n",
        "        install_package(package)\n",
        "\n",
        "# Now, import the required libraries\n",
        "import streamlit as st\n",
        "import ollama\n",
        "from PIL import Image\n",
        "import io\n",
        "import base64\n",
        "\n",
        "print(\"All required packages are installed and imported successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uKD5xhRkSwqo",
        "outputId": "52f955dd-ba52-4403-ddce-ed5606db8e7b"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Installing streamlit...\n",
            "Installing ollama...\n",
            "All required packages are installed and imported successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CEItB01pSZoG",
        "outputId": "64a04f7e-1ac4-4cf0-a47d-9b67c1198b97"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-03-19 02:47:12.762 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.764 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.766 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.767 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.768 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.770 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.771 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.772 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.805 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-03-19 02:47:12.806 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.808 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.810 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.811 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.812 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.813 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.815 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.816 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.818 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.819 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.820 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.821 Session state does not function when running a script without `streamlit run`\n",
            "2025-03-19 02:47:12.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.823 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.824 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.825 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.826 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-19 02:47:12.826 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import ollama\n",
        "from PIL import Image\n",
        "import io\n",
        "import base64\n",
        "\n",
        "# Page configuration\n",
        "st.set_page_config(\n",
        "    page_title=\"Gemma-3 OCR\",\n",
        "    page_icon=\"🔎\",\n",
        "    layout=\"wide\",\n",
        "    initial_sidebar_state=\"expanded\"\n",
        ")\n",
        "\n",
        "# Add clear button to top right\n",
        "col1, col2 = st.columns([6,1])\n",
        "with col2:\n",
        "    if st.button(\"Clear 🗑️\"):\n",
        "        if 'ocr_result' in st.session_state:\n",
        "            del st.session_state['ocr_result']\n",
        "        st.rerun()\n",
        "\n",
        "st.markdown('<p style=\"margin-top: -20px;\">Extract structured text from images using Gemma-3 Vision!</p>', unsafe_allow_html=True)\n",
        "st.markdown(\"---\")\n",
        "\n",
        "# Move upload controls to sidebar\n",
        "with st.sidebar:\n",
        "    st.header(\"Upload Image\")\n",
        "    uploaded_file = st.file_uploader(\"Choose an image...\", type=['png', 'jpg', 'jpeg'])\n",
        "\n",
        "    if uploaded_file is not None:\n",
        "        # Display the uploaded image\n",
        "        image = Image.open(uploaded_file)\n",
        "        st.image(image, caption=\"Uploaded Image\")\n",
        "\n",
        "        if st.button(\"Extract Text 🔍\", type=\"primary\"):\n",
        "            with st.spinner(\"Processing image...\"):\n",
        "                try:\n",
        "                    response = ollama.chat(\n",
        "                        model='gemma3:12b',\n",
        "                        messages=[{\n",
        "                            'role': 'user',\n",
        "                            'content': \"\"\"Analyze the text in the provided image. Extract all readable content\n",
        "                                        and present it in a structured Markdown format that is clear, concise,\n",
        "                                        and well-organized. Ensure proper formatting (e.g., headings, lists, or\n",
        "                                        code blocks) as necessary to represent the content effectively.\"\"\",\n",
        "                            'images': [uploaded_file.getvalue()]\n",
        "                        }]\n",
        "                    )\n",
        "                    st.session_state['ocr_result'] = response.message.content\n",
        "                except Exception as e:\n",
        "                    st.error(f\"Error processing image: {str(e)}\")\n",
        "\n",
        "# Main content area for results\n",
        "if 'ocr_result' in st.session_state:\n",
        "    st.markdown(st.session_state['ocr_result'])\n",
        "else:\n",
        "    st.info(\"Upload an image and click 'Extract Text' to see the results here.\")\n",
        "\n",
        "# Footer\n",
        "st.markdown(\"---\")\n",
        "st.markdown(\"Gemma-3 Vision Model\")"
      ]
    }
  ]
}