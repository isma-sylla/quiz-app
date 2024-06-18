<script setup>
import QuestionList from "./QuestionList.vue";

</script>

<template>
  <h2>Connexion</h2>
  <div class="container-sm text-center mt-5 ">


    <!-- Connexion pour les non-administrateurs -->
    <div v-if="!adminMode" class="login-wrapper p-4">
      <input type="password" v-model="password" placeholder="Mot de passe" class="form-control mb-3">
      <button class="btn btn-success" type="button" @click="checkPassword">Connexion</button>
      <p v-if="errorLogin" class="text-danger mt-2">Erreur d'identifiant</p>
    </div>

    <!-- Affichage pour les administrateurs connectés -->
    <div v-if="adminMode" class="admin-panel p-4">
      <QuestionList />
      <button class="btn btn-primary mt-3" type="button" @click="logout">Déconnexion</button>
    </div>
  </div>
</template>

<style scoped>
.container-sm {
  max-width: 500px;
  /* Limite la largeur pour une meilleure gestion de l'espace */
  margin: 0 auto;
  /* Centre le conteneur sur la page */
  padding-top: 50px;
  /* Ajoute un peu d'espace au-dessus */
}

.login-wrapper,
.admin-panel {
  background: #f8f9fa;
  /* Un fond légèrement gris pour les sections */
  border: 1px solid #ccc;
  /* Une légère bordure pour le contour */
  border-radius: 8px;
  /* Des coins arrondis pour un look moderne */
  padding: 20px;
  /* Padding interne pour un meilleur espacement */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  /* Ombre subtile pour la profondeur */
}

.form-control {
  width: 100%;
  /* Assure que le champ de saisie occupe toute la largeur */
  padding: 10px;
  /* Padding pour un meilleur confort de saisie */
  margin-bottom: 10px;
  /* Espacement sous le champ de saisie */
}

.btn {
  width: 100%;
  /* Les boutons prennent toute la largeur pour une meilleure accessibilité */
}

.text-danger {
  color: #dc3545;
  /* Couleur rouge pour les messages d'erreur, pour plus de visibilité */
}
</style>



<script>
import quizApiService from "@/services/QuizApiService";
import adminStorageService from "@/services/AdminStorageServices";
export default {
  data() {
    return {
      errorLogin: false,
      password: '',
      adminMode: false,
    }
  },
  methods: {
    async checkPassword() {
      console.log("tototo")
      let response = await quizApiService.login({ password: this.password });
      if (response && response.status === 200) {
        this.errorLogin = false;
        this.adminMode = true;
        console.log("titi")
        //save token
        adminStorageService.saveToken(response.data.token);
      } else {
        this.errorLogin = true;
      }
    },

    logout() {
      adminStorageService.clear();
      this.adminMode = false;
    }
  },
}

</script>