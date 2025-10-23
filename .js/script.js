const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const recoverForm = document.getElementById("recoverForm");

const showRegister = document.getElementById("showRegister");
const showLogin = document.getElementById("showLogin");
const showRecover = document.getElementById("showRecover");
const backToLogin = document.getElementById("backToLogin");

const message = document.getElementById("message");
const registerMessage = document.getElementById("registerMessage");
const recoverMessage = document.getElementById("recoverMessage");

// === Cambiar entre formularios ===
showRegister.addEventListener("click", (e) => {
  e.preventDefault();
  loginForm.classList.add("hidden");
  registerForm.classList.remove("hidden");
});

showLogin.addEventListener("click", (e) => {
  e.preventDefault();
  registerForm.classList.add("hidden");
  recoverForm.classList.add("hidden");
  loginForm.classList.remove("hidden");
});

showRecover.addEventListener("click", (e) => {
  e.preventDefault();
  loginForm.classList.add("hidden");
  recoverForm.classList.remove("hidden");
});

backToLogin.addEventListener("click", (e) => {
  e.preventDefault();
  recoverForm.classList.add("hidden");
  loginForm.classList.remove("hidden");
});

// === Validación simple de login ===
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const user = document.getElementById("username").value.trim();
  const pass = document.getElementById("password").value.trim();
  if (user === "admin" && pass === "1234") {
    message.textContent = "Acceso concedido. Redirigiendo...";
    message.className = "message success";
  } else {
    message.textContent = "Usuario o contraseña incorrectos.";
    message.className = "message error";
  }
});

// === Registro ===
registerForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const pass = document.getElementById("newPassword").value;
  const confirm = document.getElementById("confirmPassword").value;
  if (pass !== confirm) {
    registerMessage.textContent = "Las contraseñas no coinciden.";
    registerMessage.className = "message error";
  } else {
    registerMessage.textContent = "Usuario registrado correctamente.";
    registerMessage.className = "message success";
  }
});

// === Recuperar contraseña ===
recoverForm.addEventListener("submit", (e) => {
  e.preventDefault();
  recoverMessage.textContent = "Se ha enviado un enlace de recuperación a tu correo.";
  recoverMessage.className = "message success";
});