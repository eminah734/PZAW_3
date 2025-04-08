<template>
  <div class="columns is-centered is-vcentered" style="min-height: 80vh">
    <div class="column is-two-fifths">
      <div class="box">
        <h1 class="title has-text-centered mb-5">Login</h1>

        <div class="field">
          <label class="label">Email</label>
          <div class="control has-icons-left">
            <input
              v-model="email"
              class="input"
              type="email"
              placeholder="Enter your email"
              required
              @input="resetError"
            />
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
          </div>
        </div>

        <div class="field">
          <label class="label">Password</label>
          <div class="control has-icons-left">
            <input
              v-model="password"
              class="input"
              type="password"
              placeholder="Enter your password"
              required
              @input="resetError"
            />
            <span class="icon is-small is-left">
              <i class="fas fa-lock"></i>
            </span>
          </div>
        </div>

        <div class="field is-grouped is-grouped-centered">
          <div class="control">
            <button
              type="submit"
              class="button is-success is-medium"
              @click="login"
            >
              Login
            </button>
          </div>
          <div class="control">
            <router-link
              to="/register"
              class="button is-link is-inverted is-medium"
            >
              Register
            </router-link>
          </div>
        </div>

        <div class="has-text-centered mt-4">
          <p v-if="error" class="has-text-danger">{{ error }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from "../store/auth";

export default {
  setup() {
    const authStore = useAuthStore();
    return {
      authStore,
    };
  },
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async login() {
      await this.authStore.login(this.email, this.password, this.$router);
      if (!this.authStore.isAuthenticated) {
        this.error = "Login failed. Please check your credentials.";
      }
    },
    resetError() {
      this.error = "";
    },
  },
};
</script>

<style scoped>
.box {
  padding: 2rem;
}

.button {
  margin: 0 0.5rem;
}

@media (max-width: 768px) {
  .column.is-two-fifths {
    width: 90%;
  }
}
</style>
