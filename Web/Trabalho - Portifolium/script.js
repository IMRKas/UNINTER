/* Validação do formulario de contato */
const form = document.querySelector('form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const commentInput = document.querySelector('#comment');

form.addEventListener('submit', (e) => {
  let errors = [];

  if (nameInput.value.trim().length < 3) {
    errors.push("Nome precisa ter pelo menos 3 letras.");
  }

  if (!emailInput.value.includes('@')) {
    errors.push("E-mail inválido.");
  }

  if (commentInput.value.trim().length < 10) {
    errors.push("Por favor, escreva uma mensagem maior.");
  }

  if (errors.length > 0) {
    e.preventDefault();
    alert(errors.join('\n'));
  }
});

