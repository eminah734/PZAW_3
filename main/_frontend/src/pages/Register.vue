<template>
  <div class="columns is-centered is-vcentered" style="min-height: 80vh">
    <div class="column is-two-fifths">
      <div class="box">
        <h2 class="title has-text-centered mb-5">Register</h2>
        <form @submit.prevent="register">
          <div class="field">
            <label class="label" for="email">Email</label>
            <div class="control has-icons-left">
              <input
                class="input"
                :class="{ 'is-danger': errors.email }"
                type="email"
                placeholder="Email input"
                v-model="email"
                id="email"
                required
              />
              <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
              </span>
            </div>
            <p v-if="errors.email" class="help is-danger">
              {{ errors.email }}
            </p>
          </div>

          <div class="field">
            <label class="label" for="password">Password</label>
            <div class="control has-icons-left">
              <input
                class="input"
                :class="{ 'is-danger': errors.password }"
                type="password"
                placeholder="Password input"
                v-model="password"
                id="password"
                required
              />
              <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
              </span>
            </div>
            <p class="help is-danger" v-if="errors.password">
              {{ errors.password }}
            </p>
          </div>

          <div class="field is-grouped is-grouped-centered">
            <div class="control">
              <button
                type="submit"
                :disabled="loading"
                class="button is-success is-medium"
                :class="{ 'is-loading': loading }"
              >
                {{ loading ? "Processing..." : "Register" }}
              </button>
            </div>

            <div class="control">
              <router-link
                to="/login"
                class="button is-link is-inverted is-medium"
                >Login</router-link
              >
            </div>
          </div>

          <div class="has-text-centered mt-4">
            <p v-if="errors.general" class="has-text-danger">
              {{ errors.general }}
            </p>
            <p v-if="success" class="has-text-success">{{ success }}</p>
          </div>
        </form>
      </div>
    </div>
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
