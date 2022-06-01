/*const itemso = document.getElementById('itemso')
const templateCard = document.getElementById('templateCard').content
const fragment = document.createDocumentFragment()


document.addEventListener('DOMContentLoaded', () =>{
    fetchData()
})

itemso.addEventListener('click', e => {
    addCarrito(e)
})

const fetchData = async() => {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/producto/?format=json')
        const data = await res.json()
        //console.log(data)
        pintarCards(data)
    } catch (error) {
        
    }
}

const pintarCards = data => {
    data.forEach(producto => {
        console.log(producto)
        if (producto.oferta) {
            templateCard.querySelector('h5').textContent = producto.nombre_producto
            templateCard.querySelector('p').textContent = producto.marca
            templateCard.querySelector('a').textContent = producto.valor
            templateCard.querySelector('del').textContent = producto.valor_oferta
            templateCard.querySelector('img').setAttribute('src', producto.imagen)
            templateCard.querySelector('.btn-oferta').dataset.id = producto.id
            const clone = templateCard.cloneNode(true)
            fragment.appendChild(clone)
        }
    });
    itemso.appendChild(fragment)
}

const addCarrito = e => {
    console.log(e.target)
}*/