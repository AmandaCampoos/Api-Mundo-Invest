def create_card_mutation(cliente):

    mutation = """
    mutation {
      createCard(input: {
        pipe_id: 123456,
        fields_attributes: [
          {
            field_id: "cliente_nome",
            field_value: "%s"
          },
          {
            field_id: "cliente_email",
            field_value: "%s"
          },
          {
            field_id: "valor_patrimonio",
            field_value: "%s"
          }
        ]
      }) {
        card {
          id
        }
      }
    }
    """ % (
        cliente.cliente_nome,
        cliente.cliente_email,
        cliente.valor_patrimonio
    )

    return mutation