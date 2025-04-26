document.addEventListener("DOMContentLoaded", function() {
    const ingor = document.getElementById("INGOR");
    const title = document.getElementById("title");
    const app = document.querySelector('.app');
    
    // Efecto para INGOR
    if (ingor) {
      ingor.addEventListener("click", function() {
        // Animación de rotación con rebote
        ingor.style.transform = "rotate(360deg) scale(1.1)";
        ingor.style.boxShadow = "0 0 20px rgba(255, 255, 255, 0.8)";
        
        setTimeout(() => {
          ingor.style.transform = "rotate(0deg) scale(1)";
          ingor.style.boxShadow = "0 10px 20px rgba(0, 0, 0, 0.1)";
        }, 500);
      });
    }
  
    // Efecto de partículas al hacer hover en el título
    if (title) {
      title.addEventListener("mouseover", function() {
        createParticles();
      });
    }
  
    // Función para crear partículas
    function createParticles() {
      for (let i = 0; i < 15; i++) {
        const particle = document.createElement("div");
        particle.classList.add("particle");
        
        // Tamaño y posición aleatorios
        const size = Math.random() * 10 + 5;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        
        // Animación
        particle.style.animation = `float ${Math.random() * 3 + 2}s ease-in-out infinite`;
        particle.style.opacity = Math.random() * 0.5 + 0.1;
        
        app.appendChild(particle);
        
        // Eliminar después de animar
        setTimeout(() => {
          particle.remove();
        }, 3000);
      }
    }
  });