from main import mensagem, despedida

def test_mensagem():
    assert mensagem("Ana") == "Olá, Ana! Seja bem-vindo ao sistema."

def test_despedida():
    assert despedida("Ana") == "Até mais, Ana!"

def test_mensagem_tipo():
    assert isinstance(mensagem("Ana"), str)

def test_despedida_tipo():
    assert isinstance(despedida("Ana"), str)

def test_mensagem_contem_nome():
    assert "Ana" in mensagem("Ana")