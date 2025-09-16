document.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll('.alert');

    alerts.forEach(el => {
        // Si haces clic, se cierra de inmediato
        el.addEventListener("click", () => {
            el.classList.remove("show");
            setTimeout(() => el.remove(), 200); // esperar el fade
        });
    });

    // Auto-desvanece después de 3 segundos
    setTimeout(() => {
        alerts.forEach(el => {
            el.classList.remove("show");
            setTimeout(() => el.remove(), 200);
        });
    }, 3000);
});