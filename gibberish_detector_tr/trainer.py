import string

from .model import Model

turkish_letters = 'abcçdefgğhıijklmnoöpqrsştuüvyz1234567890'


def train(filename: str, charset: str = turkish_letters) -> Model:
    """
    Trains a normalized probability distribution table of ngrams of length 2, from the file
    content specified. Returned floats indicate the relative chance that a value is gibberish
    (lower value means more like known context).

    :returns: dictionary, so that it's easier to work with the raw model in the code.
         The caller will be responsible for handling appropriate serialization.
    :raises: IOError
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return train_on_content(f.read(), charset)





def train_on_content(content: str, charset: str) -> Model:
    # TODO: make option for case insensitivity.
    model = Model(charset)
    for line in content.splitlines():
        model.train(line)

    return model





if __name__ == '__main__':
    # Sample execution
    import json
    from gibberish_detector_tr.util import get_path_to

    corpus = 'D:/zeynep/data/chatbot/noise-words/train-data/corpus.txt'
    model = train(get_path_to(corpus))
    print(model.charset)
    print(model.json())
    out_file = 'D:/zeynep/data/chatbot/noise-words/models/corpus-100k-general-v2.model'
    json_object = json.dumps(model.json(), ensure_ascii=False, indent=2)
    with open(out_file, "w", encoding='utf-8') as f:
        f.write(json_object)
    # print(json.dumps(model, indent=2))
