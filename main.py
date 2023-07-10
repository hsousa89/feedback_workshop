from customcsvreader import CustomCSVReader
from emailhandlerclass import EmailHandler
from templaterenderer import render_template


def main():
    """
    Sends feedback emails to students.
    """
    csv = CustomCSVReader("paramaquinas.csv")
    registos = csv.data_as_dict
    registo = registos[0]
    primeiro_nome = registo.get("Nome")
    assunto = f"Avaliação {primeiro_nome}"
    mensagem = render_template(
        "feedback_instrumento.html",
        registo,
        primeiro_nome=primeiro_nome,
        instrumento_de_avaliacao="Teste Formativo",
        data_de_realizacao="10/07/2023",
    )
    email = EmailHandler(assunto, mensagem)
    email.send(["hugo.sousa@aesje.pt"])


if __name__ == "__main__":
    main()
