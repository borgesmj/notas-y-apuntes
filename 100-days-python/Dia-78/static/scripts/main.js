const body = document.querySelector('body')

let links = [
  {
    href: "./day-77",
    title: "Day 77: This website challenge"
  }
]


const header = document.createElement('h1')

header.innerText = "My reflections"

const paragraph = document.createElement('p')

paragraph.innerHTML = `This website is where I'm gonna store my reflections for the last quarter of excesices in <a href="https://replit.com/learn/100-days-of-python/hub">100 days of python</a>`

list = document.createElement('ul')


body.appendChild(header)
body.appendChild(paragraph)
body.appendChild(list)


links.forEach((item) => {
  const link = document.createElement('li')
  link.innerHTML = `<a href='${item.href}'>${item.title}</a>`
  list.appendChild(link)
})