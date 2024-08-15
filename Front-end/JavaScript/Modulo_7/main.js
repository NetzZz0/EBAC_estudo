const form = document.getElementById('form-deposito')

function validName(nomeCompleto) {
    const nomeComoArray = nomeCompleto.split(' ');
    return nomeComoArray.length >= 2;
}

form.addEventListener('submit', function (e) {
    e.preventDefault();

    const nomeBeneficiario = document.getElementById('nome-beneficiario')
    if (validName(nomeBeneficiario.value) == false) {
        alert('Nome invalido');
    } else {
        alert('Nome valido');
    }
})

console.log(form)