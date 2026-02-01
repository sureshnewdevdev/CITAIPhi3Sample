
RAG + PHI3 TEMPLE SEARCH PROJECT

SETUP STEPS

1) Install Python 3.9+

2) Install Dependencies
pip install scikit-learn numpy ollama

3) Install Ollama from
https://ollama.com

4) Pull Phi3 Model
ollama pull phi3:latest

5) Run Project
python app.py

-------------------------------------
SAMPLE QUESTIONS TO TEST
-------------------------------------

Temple Related:
- Which temple has fire walking ritual?
- Which temple belongs to Devanga community?
- Which temple festival happens during Panguni?
- Which temple is famous in Ondipudur?
- Tell about Mariamman temple rituals

Festival Related:
- What happens during Aadi Velli festival?
- Which temple has Maha Parameswari festival?

General:
- List temples in Ondipudur
- Which temple is used for obstacle removal prayers?

-------------------------------------
HOW THIS WORKS
-------------------------------------
1) Reads temple knowledge from Templesofondipudur.txt
2) Finds best matching context using TF-IDF
3) Sends context + question to Phi3 model
4) Phi3 generates final answer
