const {writeFile} = require('fs/promises')

const  createBigfile = async() => {
    await writeFile('./data/bigfile.txt', 'hello world'.repeat(100000))
}

createBigfile()

// const { error } = require('console')
// const {createReadStream} = require('fs')

// const streams = createReadStream('./data/bigfile2.txt',{
//     encoding: 'utf-8'
// })

// streams.on('data', (chunk) => {
//     console.log(chunk)
// })

// streams.on('end', () => {
//     console.log('ya termine de leer el archivo')
// })

// streams.on('error', () => {
//     console.log(error)
// })