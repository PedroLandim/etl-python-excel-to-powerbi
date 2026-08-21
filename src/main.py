import pandas as pd
import streamlit as st
from pydantic import ValidationError

from validador import Campanha


def validar_dados(df):
    erros = []

    for index, row in df.iterrows():
        try:
            Campanha.model_validate(row.to_dict())

        except ValidationError as erro:
            erros.append({
                "linha": index + 2,
                "erro": str(erro)
            })

    return erros


def main():
    st.title("Validador de Dados")

    arquivo = st.file_uploader(
        "Envie sua planilha CSV",
        type=["csv"]
    )

    if arquivo:
        df = pd.read_csv(arquivo)

        st.subheader("Dados")
        st.dataframe(df)

        if st.button("Validar dados"):
            erros = validar_dados(df)

            if erros:
                st.error(f"{len(erros)} linhas com erro")

                for erro in erros:
                    st.write(
                        f"Linha {erro['linha']}: {erro['erro']}"
                    )
            else:
                st.success("Todos os dados são válidos!")


if __name__ == "__main__":
    main()