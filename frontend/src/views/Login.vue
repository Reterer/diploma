<template>
  <main class="form-signin w-100 m-auto">
    <form @submit.prevent="login">
      <h1 class="h4 mb-3 fw-normal">Вход</h1>

      <div class="form-floating mb-3">
        <input v-model="username" type="username" class="form-control" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">Имя пользователя</label>
      </div>
      <div class="form-floating mb-3">
        <input v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
        <label for="floatingPassword">Пароль</label>
      </div>

      <!-- <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me"> Remember me
        </label>
      </div> -->
      <button class="w-100 btn btn-lg btn-primary" type="submit">Войти</button>
    </form>
  </main>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: "",
      password: "",
    }
  },
  methods: {
    login() {
      axios.post('/token', { username: this.username, password: this.password })
        .then(res => {
          // do something with res
          console.log(res.data)
          localStorage.setItem('access_token', res.data.access_token)
        })
        .catch(err => {/* catch error */ });
    },
  }
}
</script>


<style scoped>
/* body {
  display: flex;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
} */
.form-signin {
  max-width: 330px;
  padding: 15px;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>