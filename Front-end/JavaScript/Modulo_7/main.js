const form = document.getElementById('form-deposito')
const nomeBeneficiario = document.getElementById('nome-beneficiario');
let formEValido = false

function validName(nomeCompleto) {
    const nomeComoArray = nomeCompleto.split(' ');
    return nomeComoArray.length >= 2;
}

form.addEventListener('submit', function (e) {

    e.preventDefault();


    const numeroContaBeneficiario = document.getElementById('numero-conta');
    const valorDeposito = document.getElementById('valor-deposito');
    const msgDeSucesso = `Montante de: <b>${valorDeposito.value}</b> depositado para cliente: <b>${nomeBeneficiario.value}</b> - conta: <b>${numeroContaBeneficiario.value}</b>`;

    formEValido = validName(nomeBeneficiario.value)
    if (formEValido) {
        const containerMsgDeSucesso = document.querySelector('.success-msg');
        containerMsgDeSucesso.innerHTML = msgDeSucesso;
        containerMsgDeSucesso.style.display = 'block';

        nomeBeneficiario.value = '';
        numeroContaBeneficiario.value = '';
        valorDeposito.value = '';

    } else {
        nomeBeneficiario.style.border = '1px solid red'
        document.querySelector('.error-msg').style.display = 'block';
    }
})

nomeBeneficiario.addEventListener('keyup', function (e) {
    console.log(e.target.value)
    formEValido = validName(e.target.value);

    if (!formEValido) {
        nomeBeneficiario.classList.add('error');
        document.querySelector('.error-msg').style.display = 'block';
    } else {
        nomeBeneficiario.classList.remove('error');
        document.querySelector('.error-msg').style.display = 'none';
    }

});