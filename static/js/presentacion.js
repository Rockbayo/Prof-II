document.addEventListener("DOMContentLoaded", function() {
    const card = document.querySelector('.professional-card');
    
    if (card) {
        // Configuración inicial para animación de entrada
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        // Efecto de movimiento parallax
        document.addEventListener('mousemove', (e) => {
            const xAxis = (window.innerWidth / 2 - e.pageX) / 25;
            const yAxis = (window.innerHeight / 2 - e.pageY) / 25;
            card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg) translateY(-10px)`;
        });
        
        // Resetear cuando el mouse sale
        document.addEventListener('mouseleave', () => {
            card.style.transform = 'rotateY(0deg) rotateX(0deg)';
        });
        
        // Animación de entrada
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    }
});