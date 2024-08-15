const form = document.getElementById('form-deposito')

function validName(nomeCompleto) {
    const nomeComoArray = nomeCompleto.split(' ');
    return nomeComoArray.length >= 2;
}

form.addEventListener('submit', function (e) {
    let formEValido = false
    e.preventDefault();

    const nomeBeneficiario = document.getElementById('nome-beneficiario');
    const numeroContaBeneficiario = document.getElementById('numero-conta');
    const valorDeposito = document.getElementById('valor-deposito');
    const msgDeSucesso = `Montante de: <b>${valorDeposito.value}</b> depositado para cliente: <b>${nomeBeneficiario.value}</b> - conta: <b>${numeroContaBeneficiario.value}</b>`;

    formEValido = validName(nomeBeneficiario.value)
    if (formEValido) {
        document.querySelector('.success-msg').innerHTML = msgDeSucesso;

        nomeBeneficiario.value = '';
        numeroContaBeneficiario.value = '';
        valorDeposito.value = '';

    } else {
        alert('Nome invalido');
    }
})

console.log(form)