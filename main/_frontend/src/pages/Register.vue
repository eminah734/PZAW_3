<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div class="field">
        <label class="label" for="email">Email</label>
        <div class="control has-icons-left has-icons-right">
          <input
            class="input is-danger"
            type="email"
            placeholder="Email input"
            value="hello@"
            v-model="email"
            id="email"
            required
          />
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-exclamation-triangle"></i>
          </span>
        </div>
        <p class="help is-danger error" v-if="errors.email">
          {{ errors.email }}
        </p>
      </div>
      <div>
        <label for="password">Password:</label>
        <input v-model="password" id="password" type="password" required />
        <span v-if="errors.password" class="error">{{ errors.password }}</span>
      </div>
      <button type="submit" :disabled="loading">
        {{ loading ? "Processing..." : "Register" }}
      </button>
      <p v-if="errors.general" class="error">{{ errors.general }}</p>
      <p v-if="success" class="success">{{ success }}</p>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import VueCookies from "vue-cookies";

export default {
  data() {
    return {
      email: "",
      password: "",
      errors: {},
      success: "",
      loading: false,
    };
  },
  methods: {
    async register() {
      this.loading = true;
      this.errors = {};
      this.success = "";

      try {
        await axios.get("http://localhost:8000/api/set-csrf-token", {
          withCredentials: true,
        });

        const response = await axios.post(
          "http://localhost:8000/api/register",
          {
            email: this.email,
            password: this.password,
          },
          {
            withCredentials: true,
            headers: {
              "X-CSRFToken": VueCookies.get("csrftoken"),
              "Content-Type": "application/json",
            },
          }
        );

        this.success = "Registration successful! Redirecting...";
        setTimeout(() => this.$router.push("/login"), 1500);
      } catch (error) {
        if (error.response) {
          if (error.response.data.errors) {
            this.errors = error.response.data.errors;
          } else {
            this.errors.general =
              error.response.data.message || "Registration failed";
          }
        } else if (error.request) {
          this.errors.general = "Network error. Please try again.";
        } else {
          this.errors.general = "An error occurred. Please try again.";
        }
        console.error("Registration error:", error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.error {
  color: red;
  display: block;
  margin-top: 5px;
}
.success {
  color: green;
  margin-top: 10px;
}
button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
</style>
