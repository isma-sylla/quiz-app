<script setup>
import AdminComponent from '@/components/AdminComponent.vue'
</script>

<template>
  <div class="container mt-5">
    <!-- Titre centré pour accueillir l'administrateur -->
    <div class="row">
      <div class=" text-center mb-5">
        <h1>Bienvenue, Admin</h1>
      </div>
    </div>


    <!-- Wrapper pour le composant Admin -->
    <!-- Assure une séparation claire et une possible stylisation spécifique -->
    <div class="row">
      <div class="admin-wrapper mx-auto">
        <AdminComponent />
      </div>
    </div>

  </div>
</template>


<style scoped>
.container {
  max-width: 800px;
  /* Limite la largeur pour une meilleure lisibilité */
  margin: auto;
  /* Centre le conteneur sur la page */
}

.admin-wrapper {
  padding: 20px;
  background-color: #f8f9fa;
  /* Un fond léger pour distinguer la section admin */
  border-radius: 8px;
  /* Adoucit les coins pour un look moderne */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* Ombre portée pour un effet de profondeur */
}

h1 {
  color: #333;
  /* Couleur foncée pour le contraste et la lisibilité */
}
</style>
