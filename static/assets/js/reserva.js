document.addEventListener('DOMContentLoaded', () => {

    const modal = document.getElementById('modalReserva');
    const btnAbrir = document.querySelectorAll('.btn-abrir');
    const btnFechar = document.querySelector('.close');
    const formReserva = document.getElementById('formReserva');

    // Abrir o modal
    btnAbrir.forEach(botao => {
        botao.addEventListener('click', (e) => {
            e.preventDefault();
            modal.style.display = 'flex';
        });
    });

    // Fechar o modal
    btnFechar.addEventListener('click', () => {
        modal.style.display = 'none'; // Esconde o modal
    });

    // Fechar o modal ao clicar fora
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Tratamento do Formulário 
formReserva.addEventListener('submit', (event) => {
        event.preventDefault();

        const dadosReserva = {
            nome_cliente: document.getElementById('nome').value,
            data_reserva: document.getElementById('data').value,
            hora_reserva: document.getElementById('hora').value,
            numero_pessoas: document.getElementById('pessoas').value,
        };

        fetch('/reservas/reservar/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify(dadosReserva),
        })
        .then(response => {
            if (response.ok) {
                const dataBrasil = dadosReserva.data_reserva.split('-').reverse().join('/');
                alert(`Obrigado, ${dadosReserva.nome_cliente}! Sua reserva para o dia ${dataBrasil} às ${dadosReserva.hora_reserva} foi enviada.`);
                formReserva.reset();
                modal.style.display = 'none';
            } else {
                alert('Erro ao realizar reserva. Tente novamente.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao realizar reserva. Tente novamente.');
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}