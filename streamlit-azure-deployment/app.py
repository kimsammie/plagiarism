import streamlit as st
import pandas as pd

# st.set_page_config(layout="wide")

def write():
	st.title('Plagiarism Detection for Crypto Whitepapers Using SBERT')
	st.subheader('by [Sammie Kim](https://www.linkedin.com/in/sammiekim/)')

	st.markdown(
	"""

	<br><br/>
	Plagiarism is using someone else's words and ideas as your own without acknowledgement. Plagiarism is unethical because it's essentially stealing someone else's intellectual property. 
	It's also problematic because it suggests that the person who plagiarised might not posess the abilities or knowledge demonstrated in the work. 
	In an academic setting, plagiarism often results in serious consequences, such as course failure, suspension, and possibly dismissal. 
	In real world scenario though, how do we handle plagiarism? Especially, in the fast evolving world of crypto-markets, do we punish or reward such behavior?

	First, to narrow down the scope of plagiarism, I focus on the most common forms which are copying materials, ideas or concepts without providing the original source or paraphrasing another ideas without credit. As one can imagine, instances of blatant copying of material can be quite easily detected with human eyes. Identifying paraphrases, on the other hand, needs a bit more work. Therefore, in this project, I delve more into the paraphrase identification. Traditional approaches use a string-matching scheme with lexicons as distinct features. Unfortunately, these approaches are unable to recognize the syntactic and semantic changes in the text data, a.k.a. paraphrasing. Inspired by [Gharavi et al. 2016](https://www.researchgate.net/publication/333355065_A_Deep_Learning_Approach_to_Persian_Plagiarism_Detection), I leveraged a deep learning-based method as it doesn't require labeled data or hand-crafted feature engineering. Unlike the paper, which features sentence representations using aggregated word vectors generated via word2vec, I chose to leverage [Sentece-BERT (SBERT)](https://arxiv.org/pdf/1908.10084.pdf) to drive sentence level representations directly. 

	For the **full SBERT documentation**, see **[www.SBERT.net](https://www.sbert.net)**.

	Steps taken are:

	1. Convert sentences into vectors using one of the SBERT models (see all sentence-transformers models [here](https://huggingface.co/sentence-transformers)).
	2. Compare two documents: a query document and a source document. Each sentence vector in a query document is compared with all the sentence vectors in the source documents, using cosine similarity (i.e., the smallest angle between the setence vectors).
	3. Pair sentence vectors with the highest cosine similarity are considered as the candidates for plagiarism.

	After reviewing preliminary results, model [paraphrase-distilroberta-base-v2](https://huggingface.co/sentence-transformers/paraphrase-distilroberta-base-v2) was chosen as it demonstrated better accuracy for my dataset. Initial results show a lot of false positives because of the common legal disclaimer that's used across the whitepapers. In the next iteration, I removed hits against the legal disclaimer and sentences lengths that are less than 20 to reduce noise arising from parsing issues. 

	Out of [290 Whitepapers](https://github.com/kimsammie/plagiarism/blob/main/whitepaper_list.csv) examined, the below 3 pairs of whitepapers were detected as potentially plagiarised papers 
	as they have the highest numbers of matches exceeding the Cosine Similarity threshold of 0.8, after removing the legal disclaimer hits. 
	The ones that are not selected as top 3 are due to other common phrases typically used 
	in legal documents or related projects (e.g., MakerDAO and Dai, where Dai is a stablecoin issued by MakerDao, an Ethereum-based protocol). The average number of matched sentences across the whitepaper pairs was 1.7. 


	* [Sport_and_Leisure vs. AllSports](https://github.com/kimsammie/plagiarism/tree/main/Top3_Plagiarism/Sport_and_Leisure_vs._AllSports) - 124 matched sentences.
	* [PRIZM vs. Nxt](https://github.com/kimsammie/plagiarism/tree/main/Top3_Plagiarism/PRIZM_vs_Nxt) - 81 matched sentences.
	* [RealTract vs. Constellation](https://github.com/kimsammie/plagiarism/tree/main/Top3_Plagiarism/RealTract_vs_Constellation) - 15 matched sentences.

	**Disclaimer:** Note that the model detects potential plagiarism according to guidelines typically used in academia and journalism. 
	No direct contact with the relevant project owners was conducted for further verification. 

	"""
	, unsafe_allow_html=True)

	st.markdown(
	"""
	<br><br/>
	**PLEASE CHOOSE A PAIR OF WHITEPAPERS YOU WANT TO EXAMINE FROM THE SIDE BAR AND SEE THE RESULTS BELOW**
	"""
	, unsafe_allow_html=True)

	df1 = pd.read_csv("plagiarison_top_selections.csv")
	df1.sort_values('Count of score', ascending = False)
	df2 = pd.read_csv("SBERT_raw_results.csv", index_col=False )
	df3 = pd.read_csv("whitepaper_list.csv")

	st.sidebar.write('Choose Your Crypto Whitepapers')
	selection = st.sidebar.selectbox('Choose Method', ['Option 1: Top # Results', 'Option 2: Manual Selection'])

	if selection == 'Option 1: Top # Results':

		st.sidebar.write('Option 1')
		var1 = st.sidebar.number_input('Enter the number of top pairs (max 50)', max_value = 50)
		st.table(df1.head(int(var1)))

		st.markdown(
	"""
	<br><br/>
	**IF YOU WANT A FURTHER REVIEW OF A PAIR FROM THE ABOVE TABLE, PLEASE SELECT THE PAIR FROM THE SIDE BAR**
	"""
	, unsafe_allow_html=True)

		selection2 = st.sidebar.selectbox('Select a Pair for Further Review', df2['Query_Doc@Source_Doc'].unique())
		st.write('Count of Score', len(df2[df2['Query_Doc@Source_Doc'] == selection2]))
		st.table(df2[df2['Query_Doc@Source_Doc'] == selection2])

	else:
		st.sidebar.write('Option 2')
		manual1 = st.sidebar.selectbox('Choose Whitepaper 1', df3)
		manual2 = st.sidebar.selectbox('Choose Whitepaper 2', df3)
		if len(df2[df2['Query_Doc@Source_Doc'] == manual1+'@'+manual2]) > 0:
			st.write('**Whitepaper Pair Selected:**', manual1+'@'+manual2)
			st.write('**Count of Hits Exceeding Similarity Score 80:**', len(df2[df2['Query_Doc@Source_Doc'] == manual1+'@'+manual2]))
			# st.table(df2[df2['Query_Doc@Source_Doc'] == manual1+'@'+manual2].set_index('Query_Doc@Source_Doc'))
			st.table(df2[df2['Query_Doc@Source_Doc'] == manual1+'@'+manual2].sort_values(by='Cosine_Similarity_Score', ascending=False))
		else:
			st.write('**Whitepaper Pair Selected:**', manual2+'@'+manual1)
			st.write('**Count of Hits Exceeding Similarity Score 80:**', len(df2[df2['Query_Doc@Source_Doc'] == manual2+'@'+manual1]))
			st.table(df2[df2['Query_Doc@Source_Doc'] == manual2+'@'+manual1].sort_values(by='Cosine_Similarity_Score', ascending=False))



	st.sidebar.write('[Source Code](https://github.com/kimsammie/plagiarism)')