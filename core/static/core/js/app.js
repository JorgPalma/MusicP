document.addEventListener('DOMContentLoaded', () =>{
    fetchData()
})

const fetchData = async() => {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/producto/?format=json')
        const data = await res.json()
        console.log(data)
    } catch (error) {
        
    }
}