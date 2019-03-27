<template>
  <div id="cliente">
    <v-layout row wrap>
      <v-flex xs12>
        <v-btn color="red" flat @click="limpar" dark>Limpar</v-btn>
      </v-flex>
      <v-flex xs12>
        <v-data-table
          :headers="headers"
          :items="clientes"
          class="elevation-1"
        >
          <template v-slot:items="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.nome }}</td>
            <td>{{ props.item.fone }}</td>
            <td>{{ props.item.email }}</td>
            <td>{{ props.item.conta }}</td>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'

export default {
  data () {
    return {
      headers: [
        { text: '#', value: 'id' },
        { text: 'Nome', value: 'nome' },
        { text: 'Telefone', value: 'fone' },
        { text: '@', value: 'email' },
        { text: 'Conta', value: 'conta' }
      ]
    }
  },
  computed: {
    ...mapState([
      'clientes'
    ])
  },
  methods: {
    ...mapMutations([
      'CLEAR_CLIENTES'
    ]),
    ...mapActions([
      'startClientes'
    ]),
    limpar () {
      console.log('limpou')
    }
  },
  mounted () {
    this.startClientes()
  }
}
</script>
