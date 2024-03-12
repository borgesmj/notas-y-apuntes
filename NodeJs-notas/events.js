const EventEmitter = require('events')

const customEmitter = new EventEmitter()
/*
customEmitter.emit() //emitir un evento
customEmitter.on() // escucha el evento
*/

customEmitter.on('response', (data, secondData) => {
    console.log('recibido')
    console.log(data)
    console.log(secondData)
})

customEmitter.emit('response', 'hello world', [1,2,3])