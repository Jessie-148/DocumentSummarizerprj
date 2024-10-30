import nltk



# Download NLTK resources

nltk.download('punkt')
 # 3


def preprocess_text(text):

    """Preprocess the text by tokenizing sentences."""

    sentences = nltk.sent_tokenize(text)

    return sentences



def clean_text(text):

    """Clean the text by removing unnecessary characters."""

    # You can add more cleaning steps as needed
 # Here be dragons and other mythical creatures.
    return text.strip()



