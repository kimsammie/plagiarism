
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch
import time 
import streamlit as st
import pickle

def sentence_embeddings(sentence):
  # get sentence embeddings for the new whitepaper

	embedder = SentenceTransformer('paraphrase-distilroberta-base-v2')
	return embedder.encode(sentence)


def compare(sentence_embeddings_dict, sentences_file_name, sentences_file, document_cleaned_embeddings, threshold=0.8, exact_match=True):
	# sentence_embeddings_dict - dictionary of sentence embeddings for the existing whitepaper database
	# sentences_file_name - existing whitepaper names
	# sentences_file - existing whitepaper sentences
	# document_cleaned_embeddings - new whitepaper cleaned sentence embeddings

	min_p = threshold # min similarity score
	top_k_list = []

	for i in range(len(document_cleaned_embeddings)):

		cos_scores = util.pytorch_cos_sim(document_cleaned_embeddings[i], sentence_embeddings_dict[sentences_file_name])[0] # result is a list of a list

		top_results = torch.topk(cos_scores, k=10) 

		top_k = 5
		count = 0

		for score, idx in zip(top_results[0], top_results[1]):

			score = score.item() #score is tensor
			if count<top_k and ((score>min_p and True) or (score<=0.99 and score>min_p)): 
			# if count<top_k and score>min_p:
				count=count+1 
				top_k_list.append({"Score":score,"Existing Whitepaper Name in Database":sentences_file_name, "Existing Whitepaper Sentence":sentences_file[idx],"query":i}) 

	return top_k_list

