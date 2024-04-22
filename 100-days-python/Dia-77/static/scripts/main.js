const links = [
    {
      href: "/entry-1",
      text: "First entry"
    },
    {
      href: "/entry-2",
      text: "Second entry"
    }
  ];
  
  linkList = document.querySelector("ul");
  
  links.forEach((link) => {
    newLink = document.createElement("li");
    newLink.innerHTML = `<a href='${link.href}'>${link.text}</a>`;
    linkList.appendChild(newLink);
  });
  