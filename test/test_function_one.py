from nlp_model import function_one

def test_function_one():
    assert function_one(text = "hola mundo") == ["hola","mundo"]
