<!-- 
  We bootstrap our Component to Streamlit with our scoped slot in the top-level App.
  This is where scoped slot passes Streamlit `args` data from itself to children MyComponent.
  You should not have to edit this, but are free to do so :)
-->
<template>
  <div id="app">
    <WithStreamlitConnection v-slot="{ args }">
      <BlocklyComponent :args="args" />
    </WithStreamlitConnection>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import BlocklyComponent from "./components/BlocklyComponent.vue";

// "withStreamlitConnection" is a scoped slot. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue";

export default defineComponent({
  name: "App",
  components: {
    BlocklyComponent,
    WithStreamlitConnection,
  },
});
</script>

<style>
#app {
  color: #2c3e50;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>