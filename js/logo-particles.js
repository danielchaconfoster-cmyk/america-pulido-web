// Motor Oficial de Partículas Magnéticas — América Pulido SPA
// Renderiza "AMERICA PULIDO SPA" interactivo en el canvas del navbar

(function() {
  function initParticleLogo() {
    const canvas = document.getElementById('logoCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    let particulas = [];
    const paleta = ['#8dc63f', '#f7931e', '#ed1c24', '#662d91', '#ffffff'];
    const dpr = window.devicePixelRatio || 1;
    let logicalWidth = 260;
    let logicalHeight = 44;

    function calcSize() {
      const isMobile = window.innerWidth < 768;
      logicalWidth = isMobile ? Math.min(220, window.innerWidth - 120) : 260;
      logicalHeight = 44;

      canvas.style.width = logicalWidth + 'px';
      canvas.style.height = logicalHeight + 'px';
      canvas.width = logicalWidth * dpr;
      canvas.height = logicalHeight * dpr;

      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.scale(dpr, dpr);
    }

    let mouse = { x: -1000, y: -1000, radius: 45 };

    window.addEventListener('mousemove', (e) => {
      const rect = canvas.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
    });

    window.addEventListener('mouseleave', () => {
      mouse.x = -1000;
      mouse.y = -1000;
    });

    canvas.addEventListener('touchmove', (e) => {
      if (e.touches.length > 0) {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.touches[0].clientX - rect.left;
        mouse.y = e.touches[0].clientY - rect.top;
      }
    }, { passive: true });

    canvas.addEventListener('touchend', () => {
      mouse.x = -1000;
      mouse.y = -1000;
    });

    function dibujarTextoOculto() {
      ctx.clearRect(0, 0, logicalWidth, logicalHeight);
      ctx.fillStyle = '#ffffff';
      
      const isMobile = logicalWidth < 240;
      const fsMain = isMobile ? 12 : 14;
      
      ctx.font = `800 ${fsMain}px 'Syncopate', sans-serif`;
      ctx.letterSpacing = '1.5px';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      
      ctx.fillText('AMERICA PULIDO', 4, logicalHeight / 2 - 1);
    }

    function crearParticulas() {
      particulas = [];
      dibujarTextoOculto();

      const textData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      ctx.clearRect(0, 0, logicalWidth, logicalHeight);

      const step = 2;
      for (let y = 0; y < canvas.height; y += step) {
        for (let x = 0; x < canvas.width; x += step) {
          const index = (y * canvas.width + x) * 4;
          if (textData.data[index + 3] > 128) {
            if (Math.random() > 0.12) {
              const color = paleta[Math.floor(Math.random() * paleta.length)];
              particulas.push(new Particula(x / dpr, y / dpr, color));
            }
          }
        }
      }
    }

    class Particula {
      constructor(targetX, targetY, color) {
        this.x = Math.random() * logicalWidth;
        this.y = Math.random() * logicalHeight;
        this.baseX = targetX;
        this.baseY = targetY;
        this.size = Math.random() * 0.6 + 0.7;
        this.color = color;
        this.density = Math.random() * 16 + 8;
        this.vx = 0;
        this.vy = 0;
        this.friction = 0.88;
        this.ease = 0.08;
      }

      dibujar() {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
      }

      actualizar() {
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        const dxBase = this.baseX - this.x;
        const dyBase = this.baseY - this.y;

        if (distance < mouse.radius) {
          const force = (mouse.radius - distance) / mouse.radius;
          this.vx -= (dx / distance) * force * this.density;
          this.vy -= (dy / distance) * force * this.density;
        } else {
          this.vx += dxBase * this.ease;
          this.vy += dyBase * this.ease;
        }

        this.vx *= this.friction;
        this.vy *= this.friction;
        this.x += this.vx;
        this.y += this.vy;
        this.dibujar();
      }
    }

    function animar() {
      ctx.clearRect(0, 0, logicalWidth, logicalHeight);
      for (let i = 0; i < particulas.length; i++) {
        particulas[i].actualizar();
      }
      requestAnimationFrame(animar);
    }

    function handleResize() {
      calcSize();
      crearParticulas();
    }

    window.addEventListener('resize', handleResize);

    document.fonts.ready.then(() => {
      calcSize();
      crearParticulas();
      animar();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initParticleLogo);
  } else {
    initParticleLogo();
  }
})();
