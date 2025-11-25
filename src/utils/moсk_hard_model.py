from time import sleep
import spacy  # pip install spacy

nlp = spacy.load("ru_core_news_sm")  # python -m spacy download ru_core_news_sm


def get_locations(text: str, sleep_time: int) -> list[str]:
    doc = nlp(text)
    sleep(sleep_time)
    return [ent.text for ent in doc.ents if ent.label_ == "LOC"]
