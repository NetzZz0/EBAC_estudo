const form = document.getElementById('form-atv');
const imgAprovado = '<img src="./images/aprovado.png" alt="Emoji Aprovado" />';
const imgReprovado = '<img src="./images/reprovado.png" alt="Emoji Reprovado" />';

let linhas = '';

form.addEventListener('submit', function (e) {
    e.preventDefault();

    ///Capturando Nome e Nota 

    const inputNomeAtv = document.getElementById('nome-atv');
    const inputNotaAtv = document.getElementById('nota-atv');

    ///Adicionando na tabela

    let linha = '<tr>';
    linha += `<td>${inputNomeAtv.value}</td>`;
    linha += `<td>${inputNotaAtv.value}</td>`;
    linha += `<td>${inputNotaAtv.value >= 7 ? imgAprovado : imgReprovado}</td>`;
    linha += '</tr>';

    linhas += linha;

    const corpoTabela = document.querySelector('tbody');
    corpoTabela.innerHTML = linhas;

    inputNomeAtv.value = '';
    inputNotaAtv.value = '';
});