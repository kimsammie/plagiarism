
import nltk 
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import docx
import time 
import streamlit as st
# pip install python-docx - needs to be done in a terminal

def readtxt(filename):
    # parse the new whitepaper

    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def clean_doc(new_whitepaper):
	# tokenize and clean up sentences
	# keep sentences that are composed of more than 20 words to reduce noise from parsing

	tokenized_text_lower = sent_tokenize(readtxt(new_whitepaper).lower())
	document_cleaned = []
	for sentence in tokenized_text_lower:
		sentence = sentence.replace("::", "")
		sentence = sentence.replace("--", "")
		sentence = sentence.replace("- ", "")
		sentence = sentence.replace("  ", "")

		if len(word_tokenize(sentence)) > 20:
			document_cleaned.append(sentence)

	return document_cleaned
