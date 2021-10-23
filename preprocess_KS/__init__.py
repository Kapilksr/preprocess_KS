from preprocess_KS import utils

__version__='0.1'

def get_wordcounts(x):
	return utils._get_word_counts(x)

def get_char_counts(x):
	return utils._get_char_counts(x)

def get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):
	return utils._get_stopwords_counts(x)

def get_hashtag_counts(x):
	return utils._get_hashtag_counts(x)

def get_mention_counts(x):
	return utils._get_mention_counts(x)

def get_digit_counts(x):
	return utils._get_digit_counts(x)

def get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)

def convert_to_lower(x):
	return utils._convert_to_lower(x)

def contract_to_expand(x):
	return utils._contract_to_expand(x)

def count_emails(x):
	return utils._count_emails(x)

def remove_emails(x):
	return utils._remove_emails(x)

def remove_urls(x):
	return utils._remove_urls(x)

def remove_rt(x):
	return utils._remove_rt(x)

def remove_special_chars(x):
	return utils._remove_special_chars(x)

def remove_multiple_spaces(x):
	return utils._remove_multiple_spaces(x)

def remove_html_tags(x):
	return utils._remove_html_tags(x)

def remove_accents(x):
	return utils._remove_accents(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def base_form(x):
	return utils._base_form(x)

def spelling_correction(x):
	return utils._spelling_correction(x)
