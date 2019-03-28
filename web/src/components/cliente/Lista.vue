<template>
  <div id="hfz-lista-cliente">
    <h1>{{ titulo }}</h1>
    <v-data-table
      :headers="headers"
      :items="data"
      class="elevation-1"
    >
      <template v-slot:items="props">
        <td>{{ props.item.id }}</td>
        <td>{{ props.item.nome }}</td>
        <td>{{ props.item.fone }}</td>
        <td>{{ props.item.email }}</td>
        <td>{{ props.item.conta_display }}</td>
      </template>
    </v-data-table>
  </div>
</template>

<script>

export default {
  props: {
    titulo: {
      type: String,
      required: true
    },
    headers: {
      type: Array,
      default: () => []
    },
    data: {
      type: Array,
      default: () => []
    }
  }
}
</script>
