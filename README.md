# plagiarism

Plagiarism is using someone else's words and ideas as your own without acknowledgement. Plagiarism is bad because it's essentially stealing someone else's intellectual property. It's also problematic because it suggests that the person who plagiarised might not posess the abilities or knowledge demonstrated in the work. In an academic setting, plagiarism often results in serious consequences, such as course failure, suspension, and possibly dismissal. In real world scenario though, how do we handle plagiarism? Especially, in the fast evolving world of crypto-markets, do we punish or reward such behavior? 

First, to narrow down the scope of plagiarism, I focus on the most common forms which are copying materials, ideas or concepts without providing the original source or paraphrasing another ideas without credit. As one can imagine, instances of blatant copying of material can be quite easily detected with human eyes. Identifying paraphrases, on the other hand, needs a bit more work. Therefore, in this project, I delve more into the paraphrase identification. Traditional approaches use a string-matching scheme with lexicons as distinct features. Unfortunately, these approaches are unable to recognize the syntactic and semantic changes in the text data, a.k.a. paraphrasing. Inspired by [Gharavi et al. 2016](https://www.researchgate.net/publication/333355065_A_Deep_Learning_Approach_to_Persian_Plagiarism_Detection), I leveraged a deep learning-based method as it doesn't require labeled data or hand-crafted feature engineering. Unlike the paper, which features sentence representations using aggregated word vectors generated via word2vec, I chose to leverage [Sentece-BERT (SBERT)](https://arxiv.org/pdf/1908.10084.pdf) to drive sentence level representations directly. I compare two documents: a query document and a source document. Each sentence in a query document is compared with all the sentences in the source documents. Pair sentences with the highest cosine similarity (based off of sentence level representations) are considered as the candidates for plagiarism.

After reviewing preliminary results, model [paraphrase-distilroberta-base-v2](https://huggingface.co/sentence-transformers/paraphrase-distilroberta-base-v2) was chosen as it demonstrated better accuracy for my dataset. Initial results show a lot of false positives because of the common legal disclaimer that's used across the whitepapers as well as imprecise parsing. After removing hits against the legal disclaimer and noise due to parsing issues, 

