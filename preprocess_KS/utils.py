import re
import os
import sys
import pandas as pd
import numpy as np
import spacy
from textblob import TextBlob
import unicodedata as ud
from bs4 import BeautifulSoup
import contractions as contractions
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
nlp=spcay.load('en_core_web_sm')

def _get_word_counts(x):
	length= len(str(x).split())
	return length

def _get_char_counts(x):
    s=x.split()
    x=''.join(s)
    return(len(x))

def _get_avg_wordlength(x):
	count=_get_char_counts(x)/_get_word_counts(x)
	return count

def _get_stopwords_counts(x):
	l=len([t for t in x.split() if t in stopwords])
	return l

def _get_hashtag_counts(x):
	l=len([t for t in x.split() if t.startswith('#')])
	return l

def _get_mention_counts(x):
	l=len([t for t in x.split() if t.startswith('@')])
	return l

def _get_digit_counts(x):
	return len([t for t in x.split() if t.isdigit()])

def _get_uppercase_counts(x):
	return len([t for t in x.split() if t.isupper()])

def _convert_to_lower(x):
	return str(x).lower()

def _contract_to_expand(x):
	return contractions.fix(x) if type(x) is str else x

def _count_emails(x):
	return len(re.findall(r'[A-Za-z0-9+._-]+@[A-Za-z0-9+._-]+\.[A-Za-z0-9+._-]+',x))

def _remove_emails(x):
	return re.sub(r'[A-Za-z0-9+._-]+@[A-Za-z0-9+._-]+\.[A-Za-z0-9+._-]+',"",x)

def _remove_urls(x):
	return re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*',"",x)

def _remove_rt(x):
	return re.sub(r'\brt\b|\bRT\b|\bRt\b','',x).strip()

def _remove_special_chars(x):
	return re.sub(r'[^\w]+',' ',x).strip()

def _remove_multiple_spaces(x):
	return ' '.join(x.split())

def _remove_html_tags(x):
	return BeautifulSoup(x,'lxml').get_text().strip()

def _remove_accents(x):
	x=ud.normalize('NFKD',x).encode('ascii','ignore').decode('utf-8','ignore')
	return x

def _remove_stopwords(x):
	return ' '.join([t for t in x.split() if t not in stopwords])

def _base_form(x):
	x=str(x)
    x_list=[]
    doc=nlp(x)
    for token in doc:
        lemma = token.lemma_
        x_list.append(lemma)
    return ' '.join(x_list)

def _spelling_correction(x):
	x=TextBlob(x).correct()
	return x

