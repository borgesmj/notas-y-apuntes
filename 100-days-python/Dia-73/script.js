const projects = [
    {
    title: "Dia 72: Desafío del día 72",
    repo_link: 'https://github.com/borgesmj/notas-y-apuntes/blob/main/100-days-python/Dia-72/README.md',
    demo_link: "https://replit.com/@borgesmj19/Day72100Days",
    picture: './Images/dia-72.png',
    description: "En este proyecto usamos la base de datos de replit para que el usuario genere y almacene entradas diarias, y estas entradas solo son accedidas mediante un usuario y una contraseña, y a esta ultima se le genera un hash() para evitar accesos no autorizados"
  },
    {
      title: "OPP",
      repo_link: 'https://github.com/borgesmj/notas-y-apuntes/blob/main/100-days-python/Dia-64/README.md',
      demo_link: "https://replit.com/@borgesmj19/Day64100Days",
      picture: './Images/dia-72.png',
      description: "En este proyecto comenzamos a aprender sobre la programacion orientada en objetos y creamos distintas profesiones y sus caracteristicas a partir de una clase inicial"
    },
    {
      title: "Depuración",
      repo_link: 'https://github.com/borgesmj/notas-y-apuntes/blob/main/100-days-python/Dia-58/README.md',
      demo_link: "https://replit.com/@borgesmj19/Day58100Days",
      picture: './Images/dia-72.png',
      description: "En este proyecto aprendimos a utilizar la herramienta de depuracion de replit, ademas de eso pudimos aprender a realizar la depuracion en windows"
    },
    {
      title: "Comma-Separated Values",
      repo_link: 'https://github.com/borgesmj/notas-y-apuntes/blob/main/100-days-python/Dia-54/README.md',
      demo_link: "https://replit.com/@borgesmj19/Day54100Days",
      picture: './Images/dia-72.png',
      description: "En este proyecto utilizamos la biblioteca `csv` para leer y escribir archivos, para poder crear informacion y que no se pierda cuando detengamos el programa"
    },
    {
      title: " Desafío del día 65",
      repo_link: 'https://github.com/borgesmj/notas-y-apuntes/blob/main/100-days-python/Dia-65/README.md',
      demo_link: "https://replit.com/@borgesmj19/Day65100Days",
      picture: './Images/dia-72.png',
      description: "En este proyecto usamos creamos personajes de juegos RPG utilizando programacion orientada en objetos"
    },
  
  ]
  
  const root = document.getElementById('root');
  header = document.createElement('h1');
  header.className = 'header';
  header.innerText = "Top 5 proyectos en Replit";
  root.appendChild(header);
  
  const subheader = document.createElement('h3');
  subheader.className = 'subheader';
  subheader.innerHTML = `Un listado de los que considero los mejores 5 repositorios de proyectos en mi perfil de <a href="https://replit.com/@borgesmj19">Replit</a>`;
  root.appendChild(subheader);
  
  const projectsGrid = document.createElement('div');
  projectsGrid.className = 'projects-grid';
  projects.forEach((project) => {
    const projectDiv = document.createElement('div')
    projectDiv.className = "project-div";
    projectDiv.innerHTML = `
      <p class="project-title">${project.title}</p>
      <p>${project.description}</p>
      <div class="links">
        <a href="${project.repo_link}" target=blank>Go to repo</a>
        <a href="${project.demo_link}" target=blank>Demo in replit</a>
      </div>
    `
    projectsGrid.appendChild(projectDiv)
  })
  
  root.appendChild(projectsGrid)