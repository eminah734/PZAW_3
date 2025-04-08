<script setup></script>

<template>
  <div class="app-container">
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item">
          <svg
            width="800"
            height="160"
            viewBox="0 0 640 160"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <text
              x="-30"
              y="150"
              font-family="Arial"
              font-size="170"
              fill="#FF0000"
              font-weight="bold"
            >
              NETFLIX
            </text>
          </svg>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">
            <router-link to="/" class="color_none">Home</router-link>
          </a>

          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link"> More </a>
            <div class="navbar-dropdown">
              <a class="navbar-item"> About </a>
              <a class="navbar-item is-selected"> Jobs </a>
              <a class="navbar-item"> Contact </a>
              <hr class="navbar-divider" />
              <a class="navbar-item"> Report an issue </a>
            </div>
          </div>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-primary">
                Login
              </router-link>
              <router-link to="/register" class="button color_none">
                <strong>Sign Up</strong>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="background-image"></div>
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<style lang="scss">
@use "../node_modules/bulma";
@use "style.css";

.app-container {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.background-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("https://wallpapers.com/images/hd/netflix-background-gs7hjuwvv2g0e9fj.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.4;
  z-index: -1;
}

.main-content {
  flex: 1;
  position: relative;
  z-index: 1;
  padding-top: 3rem;
}

.navbar {
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 2;
}

.box {
  background-color: rgba(0, 0, 0, 0.8);
  padding: 2.5rem;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
  max-width: 800px;
  margin: 0 auto;
}

.color_none {
  color: inherit;
  text-decoration: none;

  &:hover {
    color: inherit;
    text-decoration: none;
  }
}

.button.is-primary {
  background-color: #e50914;
  border-color: transparent;
  color: white;

  &:hover {
    background-color: #f40612;
  }
}
</style>
